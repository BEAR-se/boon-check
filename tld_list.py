# Top Level Domains (TLDs) organized by categories

GENERIC_TLDS = [
    'com', 'net', 'org', 'info', 'biz', 'xyz', 'name', 'pro', 'edu', 'gov', 'int', 'mil',
    'mobi', 'jobs', 'tel', 'asia', 'cat', 'coop', 'post', 'aero', 'museum', 'travel',
    'xxx', 'win', 'bid', 'loan', 'top', 'icu', 'vip', 'fun', 'online', 'site', 'wang',
    'world', 'link', 'click', 'space', 'press', 'host', 'website', 'buzz', 'date',
    'review', 'today', 'news', 'works', 'email', 'zone'
]

COUNTRY_TLDS = [
    'uk', 'us', 'eu', 'ca', 'au', 'de', 'fr', 'nl', 'es', 'it', 'ch', 'br', 'mx', 'jp',
    'cn', 'in', 'ru', 'ua', 'pl', 'no', 'se', 'dk', 'fi', 'ie', 'at', 'nz', 'sg', 'kr',
    'za', 'tr', 'ar', 'cl', 'co', 'pe', 'ph', 'th', 'vn', 'be', 'cz', 'gr', 'hu', 'pt',
    'ro', 'sk', 'hr', 'ee', 'lt', 'lv', 'si', 'bg', 'mt', 'is', 'li', 'lu', 'mc', 'sm',
    'va', 'ad', 'gi', 'im', 'je', 'gg', 'fo', 'gl', 'ai', 'ky', 'vg', 'tc', 'bm', 'ms',
    'io', 'sh', 'tv', 'fm', 'am', 'as', 'cc', 'me', 'nu', 'tk', 'ws', 'vc', 'bz', 'mx',
    'cx', 'gs', 'mn', 'kz', 'su', 'kg', 'tm', 'uz', 'tj', 'by', 'md', 'ge', 'az', 'am'
]

TECH_TLDS = [
    'tech', 'app', 'dev', 'cloud', 'software', 'systems', 'network', 'digital', 'computer',
    'ai', 'bot', 'crypto', 'data', 'iot', 'mobile', 'phone', 'security', 'hosting', 'code',
    'technology', 'engineering', 'analytics', 'compute', 'cyber', 'database', 'hosting',
    'linux', 'programming', 'server', 'web'
]

BUSINESS_TLDS = [
    'business', 'company', 'enterprise', 'inc', 'ltd', 'limited', 'corp', 'gmbh', 'llc',
    'industries', 'ventures', 'holdings', 'group', 'agency', 'consulting', 'management',
    'partners', 'capital', 'finance', 'financial', 'fund', 'investments', 'market',
    'markets', 'money', 'services', 'solutions', 'consulting', 'international', 'global',
    'worldwide', 'corporate', 'commerce', 'enterprises', 'firm', 'institute', 'labor',
    'careers', 'work', 'works', 'jobs', 'employment', 'hire', 'recruiting', 'staff'
]

CREATIVE_TLDS = [
    'design', 'studio', 'art', 'photography', 'photos', 'pics', 'pictures', 'gallery',
    'graphics', 'image', 'camera', 'media', 'video', 'film', 'movie', 'music', 'band',
    'radio', 'audio', 'sound', 'voice', 'podcast', 'fashion', 'style', 'beauty',
    'creative', 'entertainment', 'games', 'gaming', 'play', 'fun'
]

ECOMMERCE_TLDS = [
    'shop', 'store', 'sale', 'buy', 'deals', 'auction', 'market', 'shopping', 'cheap',
    'discount', 'promo', 'products', 'goods', 'mall', 'marketplace', 'price', 'retail',
    'warehouse', 'outlet', 'bazaar', 'boutique', 'deal', 'ecommerce', 'trade', 'trading'
]

CONTENT_TLDS = [
    'blog', 'wiki', 'forum', 'community', 'social', 'chat', 'talk', 'portal', 'search',
    'guide', 'help', 'info', 'directory', 'list', 'review', 'news', 'press', 'media',
    'magazine', 'journal', 'paper', 'post', 'article', 'content', 'write', 'writer',
    'author', 'book', 'read', 'publishing'
]

LIFESTYLE_TLDS = [
    'life', 'live', 'living', 'lifestyle', 'family', 'home', 'house', 'apartment',
    'estate', 'realty', 'property', 'properties', 'rent', 'lease', 'housing', 'food',
    'cooking', 'recipe', 'restaurant', 'cafe', 'bar', 'pub', 'club', 'fitness',
    'health', 'healthcare', 'medical', 'care', 'dental', 'doctor', 'hospital',
    'clinic', 'pharmacy', 'diet', 'organic', 'natural', 'eco', 'green'
]

GEOGRAPHIC_TLDS = [
    'city', 'town', 'village', 'region', 'state', 'country', 'continent', 'world',
    'africa', 'america', 'asia', 'europe', 'pacific', 'vegas', 'miami', 'nyc',
    'london', 'paris', 'tokyo', 'berlin', 'moscow', 'dubai', 'sydney'
]

# Combine all TLDs into one list
ALL_TLDS = list(set(
    GENERIC_TLDS +
    COUNTRY_TLDS +
    TECH_TLDS +
    BUSINESS_TLDS +
    CREATIVE_TLDS +
    ECOMMERCE_TLDS +
    CONTENT_TLDS +
    LIFESTYLE_TLDS +
    GEOGRAPHIC_TLDS
))

# Sort the list alphabetically
ALL_TLDS.sort()

# Dictionary of TLD categories for reference
TLD_CATEGORIES = {
    'Generic': GENERIC_TLDS,
    'Country': COUNTRY_TLDS,
    'Technology': TECH_TLDS,
    'Business': BUSINESS_TLDS,
    'Creative': CREATIVE_TLDS,
    'E-commerce': ECOMMERCE_TLDS,
    'Content': CONTENT_TLDS,
    'Lifestyle': LIFESTYLE_TLDS,
    'Geographic': GEOGRAPHIC_TLDS
}