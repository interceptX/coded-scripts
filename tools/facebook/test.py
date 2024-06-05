import subprocess

website = "godaddy.com"
filetext = "/home/interceptX/notes/tools/facebook/data/subdomains.txt"
webapp = f"\n[+] getting subdomain: {website}\n[+] subdomain lists\n"
command = f"curl -s 'https://crt.sh/?q=%25.{website}&output=json' | jq -r '.[].name_value' | sort -u "
data = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = data.communicate()
if output:
    with open(filetext, 'w') as file:
        file.write(output.decode())
        file.close()
    with open(filetext, 'r') as file:
        data = file.read()

    goodresponse = webapp + data
    print(goodresponse)

if error:
    badresponse = webapp + error.decode()
    print(badresponse)
