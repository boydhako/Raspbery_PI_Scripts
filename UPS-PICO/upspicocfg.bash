#!/bin/bash 
cmd="$1"
setthres="3.6"
pid="$$"
pidfile="/run/upspicocfg.pid"

function GLEDON {
	i2cset -y 1 0x6b 0x0A 0x01
}
function GLEDOFF {
	i2cset -y 1 0x6b 0x0A 0x00
}
function GETBATTTHRES {
	batthex="$(i2cget -y 1 0x6b 0x1e)"
	case $batthex in
		0x00)
			batthres="2.9"
			;;
		0x01)
			batthres="2.95"
			;;
		0x02)
			batthres="3.0"
			;;
		0x03)
			batthres="3.1"
			;;
		0x04)
			batthres="3.2"
			;;
		0x05)
			batthres="3.3"
			;;
		0x06)
			batthres="3.4"
			;;
		0x07)
			batthres="3.5"
			;;
		0x08)
			batthres="3.6"
			;;
		*)
			batthres="0"
			;;
	esac

	case $setthres in
		3.6)
			threshex="0x08"
			;;
		3.5)
			threshex="0x07"
			;;
		3.4)
			threshex="0x06"
			;;
		3.3)
			threshex="0x05"
			;;
		3.2)
			threshex="0x04"
			;;
		3.1)
			threshex="0x03"
			;;
		3.0)
			threshex="0x02"
			;;
		2.95)
			threshex="0x01"
			;;
		2.9)
			threshex="0x00"
			;;
	esac
}
function RUNCFG {
	echo $pid > $pidfile
	GETBATTTHRES
	if [ "$batthres" != "$setthres" ]; then
		GLEDOFF
		i2cset -y 1 0x6b 0x1e $threshex
	else
		GLEDON
	fi
	sleep 3
	GLEDOFF
	sleep 3
	RUNCFG
}
function CFGUPSPICO {
	if [ "$cmd" == "start" ]; then
		RUNCFG
	elif [ "$cmd" == "stop" ]; then
		GLEDOFF
		kill $(cat $PIDFile)
	else
		RUNCFG
	fi
}
CFGUPSPICO
