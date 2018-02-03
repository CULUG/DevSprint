#!/usr/bin/bash
UT=$(($(date +%s%N)/1000000))
USN=
PSWD=
curl -d "mode=191&username="$USN"&password="$PSWD"&a="$UT"&producttype=0" —dump-header headers http://192.168.100.100:8090/login.xml
curl -L -b headers http://192.168.100.100:8090

while [ : ]
do
        UT=$(($(date +%s%N)/1000000))
        curl -i "http://192.168.100.100:8090/live?mode=192&username="$USN"&a="$UT"&producttype=0"
        sleep 180
done
