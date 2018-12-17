##################################################
# Tool    : whatsmypublicip                      #
# Version : 1.0                                  #
# Bash Scripting                                 #
# Source  : https://github.com/pr2h/             #
##################################################
#!/bin/bash
while true
do
	echo "My Public IP : "$(dig @resolver1.opendns.com ANY myip.opendns.com +short)", Date and Time : "$(date '+%d/%m/%Y %H:%M:%S')
	sleep 10
done