#!/bin/sh

sudocmd=

recurse(){
    for f in $(ls -A "$1"); do
		n=0
		indent=
		while [ "$n" -lt "$3" ]; do
			indent="$indent  "
			n="$(( n + 1 ))"
		done
		if [ -d "$1/$f" ]; then
			confirm "mkdir -p $1/$f"
			recurse "$1/$f" "$2/$f" "$(( $3 + 1 ))"
		else
			confirm "ln -srf $1/$f $2/$f"
		fi
    done
}

confirm(){
	cmd="$1"
	[ "$sudocmd" ] && cmd="$sudocmd $cmd"
	while printf "%s? [Y/n] " "$indent$1"; do
		read -r ans
		if echo "$ans" | grep -iq '^no\?$'; then
			break
		elif echo "$ans" | grep -iq '^y\?e\?s\?$'; then
			$cmd
			break
		else
			printf "\nCouldn't parse %s.\n" "$ans"
		fi
	done
}

recurse "$PWD/home" "$HOME" 0

sudocmd=sudo
recurse "$PWD/root" "/" 0

gpghome="$HOME/.config/gnupg"
if [ -d "$gpghome" ]; then
    sudo chown "$(whoami)" "$gpghome"
    find "$gpghome" -type f -exec chmod 600 {} \;
    find "$gpghome" -type d -exec chmod 700 {} \;
fi
