#!/bin/sh

SUDOCMD=sudo
GPGHOME="$HOME/.config/gnupg"

recurse(){
	# shellcheck disable=SC2045
	for f in $(ls -A "$1"); do
		n=0
		indent=$3
		if [ -d "$1/$f" ]; then
			echo recursing "$1/$f" "$2/$f" "  $3"
			recurse "$1/$f" "$2/$f" "  $3"
		elif [ -L "$2/$f" ] && [ "$(realpath "$2/$f")" = "$1/$f" ]; then
			printf 'file %s is already tracked.\n' "$2/$f"
		else
			confirm "Would you like to sync $2/$f?"
			sync "$1" "$2" "$f"
		fi
	done
}

run(){
	cmd="$1"
	[ "$USE_SUDO" ] && cmd="$SUDOCMD $cmd"
	$cmd
}

sync(){
	if [ ! -d "$2" ]; then
		run "mkdir -p $2"
	fi
	run "ln -srf $1/$3 $2/$3"
}

confirm(){
	while printf "%s? [Y/n] " "$indent$1"; do
		read -r ans
		if echo "$ans" | grep -iq '^\(n\|no\)$'; then
			break
		elif echo "$ans" | grep -iq '^\(y\|yes\)$'; then
			break
		else
			printf "\nCouldn't parse %s.\n" "$ans"
		fi
	done
}

recurse "$PWD/home" "$HOME"
USE_SUDO=1
recurse "$PWD/root" ""

if [ -d "$GPGHOME" ]; then
	sudo chown "$(whoami)" "$GPGHOME"
	find "$GPGHOME" -type f -exec chmod 600 {} \;
	find "$GPGHOME" -type d -exec chmod 700 {} \;
fi
