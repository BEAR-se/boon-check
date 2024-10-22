from flask import Flask, render_template, request, jsonify
from tld_list import ALL_TLDS, TLD_CATEGORIES

import dns.resolver
import asyncio
import concurrent.futures
import time

app = Flask(__name__)

# Common TLDs list
TLDS = ALL_TLDS

def check_single_domain(domain_with_tld):
    try:
        dns.resolver.resolve(domain_with_tld, 'A')
        return {'domain': domain_with_tld, 'available': False}
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return {'domain': domain_with_tld, 'available': True}
    except Exception as e:
        print(f"Error checking {domain_with_tld}: {e}")
        return {'domain': domain_with_tld, 'available': False, 'error': True}

def check_domain_availability(domain):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_domain = {
            executor.submit(check_single_domain, f"{domain}.{tld}"): tld 
            for tld in TLDS
        }
        
        for future in concurrent.futures.as_completed(future_to_domain):
            result = future.result()
            results.append(result)
    
    # Sort results: available domains first, then by TLD length
    results.sort(key=lambda x: (not x.get('available'), len(x['domain'])))
    return results

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_domain', methods=['POST'])
def check_domain():
    domain = request.json.get('domain', '').lower().strip()
    
    if not domain:
        return jsonify({'error': 'Domain name is required'}), 400
    
    # Remove any TLD if user included it
    domain = domain.split('.')[0]
    
    # Check for valid domain name characters
    if not all(c.isalnum() or c == '-' for c in domain):
        return jsonify({'error': 'Invalid domain name. Use only letters, numbers, and hyphens.'}), 400
    
    results = check_domain_availability(domain)
    
    return jsonify({
        'results': results,
        'base_domain': domain,
        'timestamp': time.time()
    })

if __name__ == '__main__':
    app.run(debug=True)