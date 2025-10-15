# 🔒 SSL Validator

Scripts to check SSL certificate expiration across single or multiple domains. Built for uptime monitoring and cert hygiene.

---

## 🔧 Tools Included

| File | Description |
|------|-------------|
| `check_ssl.py` | Checks expiry for one domain. |
| `multi_domain_check.sh` | Loops through domains and prints expiry dates. |
| `domains.txt` | List of domains to check (one per line). |

---

## 🚀 Usage

bash

python3 check_ssl.py

bash multi_domain_check.sh

• 	Replace  with your actual domain.
• 	Add domains to file for batch checks.

 ---
 
🧠 Notes
• 	Extend with Slack/email alerts for certs expiring in < 30 days.
• 	Ideal for cron jobs or CI/CD pipelines.
