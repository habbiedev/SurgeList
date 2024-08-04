import requests

# URLs to fetch domains from
urls = [
  "https://ruleset.skk.moe/List/non_ip/ai.conf",
  "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Claude/Claude.list",
  "https://raw.githubusercontent.com/yuumimi/rules/release/surge/openai.txt"
]

# Additional Google domains to be included
google_domains = [
  ".google.ad", ".google.ae", ".google.al", ".google.am", ".google.as", ".google.at", ".google.az", 
  ".google.ba", ".google.be", ".google.berlin", ".google.bf", ".google.bg", ".google.bi", ".google.bj", 
  ".google.bs", ".google.bt", ".google.by", ".google.ca", ".google.cat", ".google.cd", ".google.cf", 
  ".google.cg", ".google.ch", ".google.ci", ".google.cl", ".google.cm", ".google.cn", ".google.co", 
  ".google.co.ao", ".google.co.bw", ".google.co.ck", ".google.co.cr", ".google.co.id", ".google.co.il", 
  ".google.co.in", ".google.co.jp", ".google.co.ke", ".google.co.kr", ".google.co.ls", ".google.co.ma", 
  ".google.co.mz", ".google.co.nz", ".google.co.th", ".google.co.tz", ".google.co.ug", ".google.co.uk", 
  ".google.co.uz", ".google.co.ve", ".google.co.vi", ".google.co.za", ".google.co.zm", ".google.co.zw", 
  ".google.com", ".google.com.af", ".google.com.ag", ".google.com.ai", ".google.com.ar", ".google.com.au", 
  ".google.com.bd", ".google.com.bh", ".google.com.bn", ".google.com.bo", ".google.com.br", ".google.com.bz", 
  ".google.com.co", ".google.com.cu", ".google.com.cy", ".google.com.do", ".google.com.ec", ".google.com.eg", 
  ".google.com.et", ".google.com.fj", ".google.com.gh", ".google.com.gi", ".google.com.gt", ".google.com.hk", 
  ".google.com.jm", ".google.com.kh", ".google.com.kw", ".google.com.lb", ".google.com.ly", ".google.com.mm", 
  ".google.com.mt", ".google.com.mx", ".google.com.my", ".google.com.na", ".google.com.ng", ".google.com.ni", 
  ".google.com.np", ".google.com.om", ".google.com.pa", ".google.com.pe", ".google.com.pg", ".google.com.ph", 
  ".google.com.pk", ".google.com.pr", ".google.com.py", ".google.com.qa", ".google.com.sa", ".google.com.sb", 
  ".google.com.sg", ".google.com.sl", ".google.com.sv", ".google.com.tj", ".google.com.tr", ".google.com.tw", 
  ".google.com.ua", ".google.com.uy", ".google.com.vc", ".google.com.vn", ".google.cv", ".google.cz", 
  ".google.de", ".google.dev", ".google.dj", ".google.dk", ".google.dm", ".google.dz", ".google.ee", 
  ".google.es", ".google.fi", ".google.fm", ".google.fr", ".google.ga", ".google.ge", ".google.gg", 
  ".google.gl", ".google.gm", ".google.gr", ".google.gy", ".google.hn", ".google.hr", ".google.ht", 
  ".google.hu", ".google.ie", ".google.im", ".google.iq", ".google.is", ".google.it", ".google.je", 
  ".google.jo", ".google.kg", ".google.ki", ".google.kz", ".google.la", ".google.li", ".google.lk", 
  ".google.lt", ".google.lu", ".google.lv", ".google.md", ".google.me", ".google.mg", ".google.mk", 
  ".google.ml", ".google.mn", ".google.ms", ".google.mu", ".google.mv", ".google.mw", ".google.ne", 
  ".google.net", ".google.nl", ".google.no", ".google.nr", ".google.nu", ".google.org", ".google.pl", 
  ".google.pn", ".google.ps", ".google.pt", ".google.ro", ".google.rs", ".google.ru", ".google.rw", 
  ".google.sc", ".google.se", ".google.sh", ".google.si", ".google.sk", ".google.sm", ".google.sn", 
  ".google.so", ".google.sr", ".google.st", ".google.td", ".google.tg", ".google.tl", ".google.tm", 
  ".google.tn", ".google.to", ".google.tt", ".google.ventures", ".google.vg", ".google.vu", ".google.ws"
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
