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
            if 'DIRECT' in line or 'REJECT' in line or 'httpdns' in line or 'httpsdns' in line or '#' in line:
                continue
            if line.startswith('DOMAIN-SUFFIX,'):
                domain = line.split(',')[1].strip()
                domain_set.add('.' + domain)
            elif line.startswith('DOMAIN,'):
                domain = line.split(',')[1].strip()
                domain_set.add(domain)
    except requests.RequestException as e:
        print(f"请求 {url} 时发生错误: {e}")

with open('Anti_IP.txt', 'w') as f:
    for domain in sorted(domain_set):
        f.write(domain + '.mail.me.com' + '\n')
