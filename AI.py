import requests

# URLs to fetch domains from
urls = [
  "https://ruleset.skk.moe/List/non_ip/ai.conf",
  "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Claude/Claude.list",
  "https://raw.githubusercontent.com/yuumimi/rules/release/surge/openai.txt"
]

# Additional Google domains to be included
google_domains = [
  "google.ws"
]

# Set to store unique domains
domain_set = set(google_domains)

# Fetch and process domains from URLs
for url in urls[:-1]:
  response = requests.get(url)
  lines = response.text.splitlines()
  for line in lines:
    if 'DOMAIN,' in line:
      domain_set.add(line.split('DOMAIN,')[1])
    elif 'DOMAIN-SUFFIX,' in line:
      domain_set.add('.' + line.split('DOMAIN-SUFFIX,')[1])

response = requests.get(urls[-1])
existing_domains = set(response.text.splitlines())
combined_domains = domain_set.union(existing_domains)

# Write unique domains to AI.txt file
with open('AI.txt', 'w') as f:
  for domain in sorted(combined_domains):
    f.write(domain + '\n')
