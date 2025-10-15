#!/bin/bash
DOMAINS_FILE="domains.txt"

while read -r domain; do
  expiry=$(echo | openssl s_client -connect "$domain:443" -servername "$domain" 2>/dev/null \
    | openssl x509 -noout -dates | grep notAfter | cut -d= -f2)
  echo "$domain expires on $expiry"
done < "$DOMAINS_FILE"
