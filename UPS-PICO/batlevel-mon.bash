#!/bin/bash

function LOGBAT {
	printf "=== %s ===\n%s\n%s\n" "$(date)" "$(./upspico-cli batlevel)" "$(./upspico-cli charge)"
	sleep 30
	LOGBAT
}
LOGBAT
