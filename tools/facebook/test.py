import subprocess

website = "icanhazip.com"
webapp = f"\n[+] getting subdomain: {website}\n[+] subdomain lists\n"
command = f"curl -s 'https://crt.sh/?q=%25.{website}&output=json' | jq -r '.[].name_value' | sort -u "
data = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = data.communicate()
if output:
    goodresponse = webapp + output.decode()
    print(goodresponse)
if error:
    badresponse = webapp + error.decode()
    print(badresponse)
