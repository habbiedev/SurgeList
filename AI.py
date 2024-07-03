import requests

urls = [
  "https://ruleset.skk.moe/List/non_ip/ai.conf",
  "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Claude/Claude.list",
  "https://raw.githubusercontent.com/yuumimi/rules/release/surge/openai.txt"
]

domain_set = set()
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

with open('AI.txt', 'w') as f:
  for domain in sorted(combined_domains):
    f.write(domain + '\n')

