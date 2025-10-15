import ssl, socket
from datetime import datetime

host = "yourdomain.com"  # Replace with target domain
port = 443

ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
    s.connect((host, port))
    cert = s.getpeercert()
    expiry = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    days_left = (expiry - datetime.utcnow()).days

    print(f"[✓] {host} SSL expires in {days_left} days")
    if days_left < 30:
        print(f"[!] Certificate for {host} expires soon!")
