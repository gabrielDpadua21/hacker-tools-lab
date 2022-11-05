import dns.resolver

target = input("set the dns target: ")

file = open("./wordlist.txt", "r")
subdomains = file.read().splitlines()

for subdomain in subdomains:
    try:
        res = dns.resolver.Resolver()
        target_complet = subdomain + "." + target
        response = res.resolver(target_complet, "A")
        print("Target IPS: ")
        for ip in response:
            print(ip)
    except:
        print("subdomain", subdomain)
        print("DNS error")
