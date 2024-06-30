#!/bin/bash

airmon-ng start wlp1s0 > /dev/null
ifconfig wlp1s0mon down
macchanger -a wlp1s0mon > /dev/null
ifconfig wlp1s0mon up

python coded-scripts/python-scripts/exploits/deauth.py

airmon-ng stop wlp1s0mon > /dev/null
ifconfig wlp1s0 down
macchanger -a wlp1s0 > /dev/null
ifconfig wlp1s0 up
ifconfig wlp1s0 | grep ether
