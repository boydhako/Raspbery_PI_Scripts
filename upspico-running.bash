#!/bin/bash 
bus="1"

function OLEDON {
	i2cset -y $bus 0x6b 0x09 0x01
}
function OLEDOFF {
	i2cset -y $bus 0x6b 0x09 0x00
}
function INITUPSPICORUNNING {
	OLEDOFF
	sleep 30
}
function UPSPICORUNNING {
	if [ "$(i2cget -y $bus 0x69 0x22 w)" != "$(i2cget -y $bus 0x69 0x22 w)" ]; then
		OLEDON
	else
		OLEDOFF
	fi
	sleep 2
	OLEDOFF
	sleep 2
	UPSPICORUNNING
}
INITUPSPICORUNNING
UPSPICORUNNING
