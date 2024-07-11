#!/bin/bash

yum install epel-release @development-tools -y
yum install radare2 readline-devel git gcc vim make pkg-config rpm-build python3-devel gobject-introspection-devel cairo-gobject-devel gtk3 libcanberra-gtk3 -y

yum update

python -m venv python-libraries
source ~/python-libraries/bin/activate
pip install briefcase fbchat selenium scapy requests toga
deactivate

git clone --depth=1 https://github.com/interceptX/coded-scripts
git clone --depth=1 https://github.com/interceptX/aeonflux
git clone --depth=1 https://github.com/interceptX/Villain

cp coded-scripts/tmux.conf > ~/.tmux.conf
cp coded-scripts/vimrc > ~/.vimrc
mkdir -p ~/.vim/colors
cp coded-scripts/monokai-soda.vim


curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
chmod 755 msfinstall && \
./msfinstall

dnf install dnf-plugins-core
dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo
rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc
dnf install brave-browser
