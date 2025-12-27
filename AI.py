import requests

# URLs to fetch domains from
urls = [
    "https://ruleset.skk.moe/List/non_ip/ai.conf",
    "https://raw.githubusercontent.com/yuumimi/rules/refs/heads/release/surge/category-ai-!cn.txt"
]

# 1. Initialize set with your manual domains
# Note: logical duplicates (like google.com and .google.com) are kept if you specifically want both formats.
manual_domains = {
    "google.ws", 
    "chatgpt.com", 
    ".google.com",
    ".withgoogle.com",
    ".lmsudio.ai"
}

domain_set = set(manual_domains)

# 2. Function to parse lines to handle DOMAIN/DOMAIN-SUFFIX or plain text
def parse_line(line):
    line = line.strip()
    # Skip empty lines or comments
    if not line or line.startswith('#') or line.startswith('//'):
        return None
    
    # Handle Rule format (Surge/Clash)
    if ',' in line:
        parts = line.split(',')
        if len(parts) >= 2:
            rule_type = parts[0].strip()
            domain = parts[1].strip()
            
            if 'DOMAIN-SUFFIX' in rule_type:
                return '.' + domain
            elif 'DOMAIN' in rule_type:
                return domain
    else:
        # Fallback: assume the line is just a domain
        return line
    return None

# 3. Fetch and process ALL URLs
print("Fetching domains...")
for url in urls:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Check for HTTP errors
        lines = response.text.splitlines()
        
        for line in lines:
            parsed_domain = parse_line(line)
            if parsed_domain:
                domain_set.add(parsed_domain)
                
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# 4. Write unique domains to AI.txt file
output_file = 'AI.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for domain in sorted(domain_set):
        f.write(domain + '\n')

print(f"Done! Saved {len(domain_set)} unique domains to {output_file}")
