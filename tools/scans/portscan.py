import socket

domain = input("set the domain to scan: ")

ports = []
most_used = [21, 22, 23, 25, 80, 443, 445, 3306, 8080]

print("Scanning ... await")

for port in most_used:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    code = client.connect_ex((domain, port))
    if code == 0:
        ports.append(port)


print("OPEN DORS IN DOMAIN: ", domain)
print(ports)


