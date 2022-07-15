#!/usr/bin/bash -xv
srcdir="$1"
apiinfo="$HOME/.wigle"

if [ -z "$srcdir" -o ! -d "$srcdir" ]; then
	printf "Need to state the directory where the kismet logs are.\n\n"
	exit 1
fi

for wiglecsv in $(find $srcdir -type f -name "*.wiglecsv"); do
	source $apiinfo
	#curl --include --verbose -H 'Accept:application/json' -u $apiname:$apitoken --basic https://api.wigle.net/api/v2/profile/user
	#curl --include -H 'Accept:application/json' -u $apiname:$apitoken --basic https://api.wigle.net/api/v2/profile/user
	httpcode="$(curl --silent --include -H 'Accept:application/json' -u $apiname:$apitoken --basic https://api.wigle.net/api/v2/profile/user | head -n 1 | awk '{print $2}')"
	case $httpcode in
		200)
			curl -i -H 'Accept:application/json' -u $apiname:$apitoken --basic  -F file=@$wiglecsv -F donate=true https://api.wigle.net/api/v2/file/upload
			echo $?
		;;
	esac
done
