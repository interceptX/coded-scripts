#!/bin/bash

clear
#rm ./firstname.txt
#rm ./lastname.txt
#rm ./phonenumber.txt
#rm ./email.txt

while true;
do
    cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1 >> ./firstname.txt; 
    cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1 >> ./lastname.txt;
    shuf -i10000000000-99999999999 -n1 >> ./phonenumber.txt;
    email=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1)@kingdomofjesuschrist.org
    echo $email >> ./email.txt
done

