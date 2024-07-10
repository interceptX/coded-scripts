#!/bin/bash

yum install epel-release
yum install git gcc vim make pkg-config rpm-build python3-devel gobject-introspection-devel cairo-gobject-devel gtk3 libcanberra-gtk3

yum update

python -m venv python-libraries
source ~/python-libraries/bin/activate
pip install briefcase fbchat selenium scapy requests toga
deactivate

git clone --depth=1 https://github.com/interceptX/coded-scripts
git clone --depth=1 https://github.com/interceptX/aeonflux
git clone --depth=1 https://github.com/interceptX/Villain

curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
chmod 755 msfinstall && \
./msfinstall