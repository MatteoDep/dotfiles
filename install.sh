#!/bin/sh

sudocmd=

recurse(){
    for f in $(ls -a "$1"); do
        if [ "$f" != "." ] && [ "$f" != ".." ]; then
            n=0
            while [ "$n" -lt "$3" ]; do
                printf "  "
                n="$(( n + 1 ))"
            done
            if [ -d "$1/$f" ]; then
                confirm "mkdir -p $2/$f"
                mkdir -p "$2/$f"
                recurse "$1/$f" "$2/$f" "$(( $3 + 1 ))"
            else
                echo "linking $2/$f"
                ln -srf "$1/$f" "$2/$f"
            fi
		fi
    done
}

confirm(){
	while printf "Run %s%s? [Y/n] " "$sudocmd " "$1"; do
		read -r ans
		if echo "$ans" | grep -iq '^no\?$'; then
			exit 1
		elif echo "$ans" | grep -iq '^y\?e\?s\?$'; then
			$sudocmd sh -c "$1"
			exit 0
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
