#!/bin/bash
echo "[+] Ransomware Decryptor Source : NOMORERANSOM.ORG => DOWNLOADING!"
curl -s https://www.nomoreransom.org/en/decryption-tools.html > index.html
cat index.html | grep -o 'https://[^"]*.exe' | sed "s/'//g" | sort | uniq | awk '!seen[$0]++' > exefile.txt
cat index.html | grep -o 'https://[^"]*.zip' | sed "s/'//g" | sort | uniq | awk '!seen[$0]++' > zipfile.txt
cat exefile.txt | while read exefile; do wget -P /home/hackerone/Downloads/ -q $exefile; echo -e "[+] File Downloaded ...." $exefile; done;
cat zipfile.txt | while read zipfile; do wget -P /home/hackerone/Downloads/ -q $zipfile; echo -e "[+] File Downloaded ...." $zipfile; done;
echo "[+] Ransomware Decryptor Source : EMSISOFT.COM => DOWNLOADING!"
curl -s https://www.emsisoft.com/en/ransomware-decryption/ > index.html
cat index.html | grep -o 'https://[^"]*/download[^"]*' | sed "s/'//g" | sort | uniq | awk '!seen[$0]++' > emsisoft.txt
cat emsisoft.txt | while read emexe; do wget -P /home/hackerone/Downloads/ -q $emexe; echo -e "[+] File Downloaded ...." $emexe; done;

