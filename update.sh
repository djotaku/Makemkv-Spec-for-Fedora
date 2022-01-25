#!/bin/sh

if   [ "$1" != "nobuild" ] \
  && [ "$1" != "n" ] \
  && [ "$1" != "--nobuild" ]; then

	git pull --ff-only
	
	spectool -g makemkv.spec
	
	if [ "$1" == "frel" ] && [ "$2" != "" ]; then
		frel=$2
		echo "Fedora Release version specified. Using $frel."
	else
		frel=$(rpm -E %fedora)
		echo "No Fedora Release version specified. Using default $frel."
	fi;

	# delimited by spaces, every space is a new "field" for cut, hence field 9 for the version/release
	mver=$(cat makemkv.spec | grep Version\: | cut -d" " -f9)
	rver=$(cat makemkv.spec | grep Release\: | cut -d" " -f9 | sed -e 's/%{?dist}//')
	
	mock -r fedora-$frel-x86_64-rpmfusion_nonfree --sources=. --spec=makemkv.spec
	
	cp /var/lib/mock/fedora-$frel-x86_64/result/makemkv-$mver-$rver.fc$frel.*.rpm .
	echo "Copied RPM to current directory. Enter sudo-password to install using DNF. Press Ctrl-c to cancel installation."
	sudo dnf install makemkv-$mver-$rver.fc$frel.x86_64.rpm
else
	echo "--nobuild argument provided - updating key only";
fi;

# extract current beta "license" key from the buy website and put it in the settings file
if [ ! -f ~/.MakeMKV/settings.conf ]; then
	echo "CREATE settings.conf using current beta key."
	mkdir -p ~/.MakeMKV
	echo "app_Key = \"$(curl "https://forum.makemkv.com/forum/viewtopic.php?f=5&t=1053" \
	| grep \<code\> \
	| sed -e "s/.*<code>//; s/<\/code>.*//")\"" \
	> ~/.MakeMKV/settings.conf

else
	echo "UPDATE settings.conf using current beta key."
	sed -i "s/^app_Key.*/app_Key = \"$(curl "https://forum.makemkv.com/forum/viewtopic.php?f=5&t=1053" \
	| grep \<code\> \
	| sed -e "s/.*<code>//; s/<\/code>.*//")\"/" \
	~/.MakeMKV/settings.conf
fi;

echo "All done!"
