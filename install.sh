#!/bin/sh

recurse() {
    for f in $(ls -a "$1"); do
        [ "$3" -eq 0 ] &&
            case "$f" in
                "LICENSE") continue;;
                "README.md") continue;;
                "install.sh") continue;;
            esac
        [ "$f" != "." ] && [ "$f" != ".." ] && [ "$f" != ".git" ] && {
            n=0
            while [ "$n" -lt "$3" ]; do
                printf "  "
                n="$(( $n + 1 ))"
            done
            if [ -d "$1/$f" ]; then
                echo "making $2/$f"
                mkdir -p "$2/$f"
                recurse "$1/$f" "$2/$f" "$(( $3 + 1 ))"
            else
                echo "linking $2/$f"
                ln -sf "$1/$f" "$2/$f"
            fi
        }
    done
}

recurse "$PWD" "$HOME" 0
