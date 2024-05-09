import requests

urls = [
    "https://raw.githubusercontent.com/lwd-temp/anti-ip-attribution/main/generated/surge.list",
    "https://raw.githubusercontent.com/bunizao/TutuBetterRules/tutu/RuleList/DOMAlN/Anti-IPCheck.list",
]

domain_set = set()
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        lines = response.text.splitlines()
        for line in lines:
            if line.startswith('DOMAIN-SUFFIX,'):
                parts = line.split(',')
                if len(parts) == 3 and parts[2] == 'DIRECT':
                    continue
                domain_set.add('.' + parts[1].strip())
            elif line.startswith('DOMAIN,'):
                domain_set.add(line.split('DOMAIN,')[1].strip())
    except requests.RequestException as e:
        print(f"请求 {url} 时发生错误: {e}")

with open('Anti_IP.txt', 'w') as f:
    for domain in sorted(domain_set):
        f.write(domain + '\n')
