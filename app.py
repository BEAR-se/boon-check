from flask import Flask, render_template, request, jsonify
import socket
import dns.resolver

app = Flask(__name__)

def is_domain_available(domain):
    try:
        # Try to get the A record
        dns.resolver.resolve(domain, 'A')
        return False  # Domain exists
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        return True  # Domain might be available
    except Exception as e:
        print(f"Error checking domain: {e}")
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_domain', methods=['POST'])
def check_domain():
    domain = request.json.get('domain', '')
    if not domain:
        return jsonify({'error': 'Domain is required'}), 400
    
    available = is_domain_available(domain)
    return jsonify({
        'available': available,
        'domain': domain
    })

if __name__ == '__main__':
    app.run(debug=True)