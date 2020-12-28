#!/bin/bash
# Source file with api key
source ./SECRET

OPRINT="/home/pi/oprint/bin/octoprint"

PRINTING="$(octoprint client -a $API get api/printer | sed -e 's/,/\n/g' -e 's/"//g' | awk -F: '$1 == "printing" {printf $NF}')"

echo $PRINTING
