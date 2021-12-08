#!/bin/zsh

# Default programs:
export MONITOR=":0"
export EDITOR="nvim"
export TERMINAL="alacritty"
export BROWSER="qutebrowser"
export EXPLORER="vifmrun"
export READER="zathura"
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
export STATUSBAR="statusblocks"

# Adds `~/.local/bin` to $PATH
export PATH="$HOME/.local/bin:$PATH"

# xdg specifications
export XDG_CONFIG_HOME="$HOME"/.config
export XDG_DATA_HOME="$HOME"/.local/share
export XDG_CACHE_HOME="$HOME"/.cache
export ZDOTDIR="$XDG_CONFIG_HOME"/zsh
export IPYTHONDIR="$XDG_CONFIG_HOME"/ipython
export JUPITER_CONFIG_DIR="$XDG_CONFIG_HOME"/jupyter
export PYTHONSTARTUP="$XDG_CONFIG_HOME"/python/python_startup.py
export LESSHISTFILE=-
export NPM_CONFIG_USERCONFIG="$XDG_CONFIG_HOME"/npm/npmrc
export GNUPGHOME="$XDG_CONFIG_HOME"/gnupg
export PASSWORD_STORE_DIR="$XDG_DATA_HOME"/password-store
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
export GTK_RC_FILES="$XDG_CONFIG_HOME"/gtk-1.0/gtkrc
export WGETRC="$XDG_CONFIG_HOME"/wgetrc
export _JAVA_OPTIONS=-Djava.util.prefs.userRoot="$XDG_CONFIG_HOME"/java
export CARGO_HOME="$XDG_DATA_HOME"/cargo
export TERMINFO="$XDG_DATA_HOME"/terminfo
export TERMINFO_DIRS="$XDG_DATA_HOME"/terminfo:/usr/share/terminfo
export SSB_HOME="$XDG_DATA_HOME"/zoom

# personal paths
export MYVIMRC="$XDG_CONFIG_HOME/nvim/init.vim"
export MYVIFMMRC="$XDG_CONFIG_HOME/vifm/vifmrc"
export DOTFILES_DIR="$HOME/.dotfiles"

# askpass program
export SSH_ASKPASS="/usr/bin/xaskpass"
export SUDO_ASKPASS="/usr/bin/xaskpass"

# clipmenu
export CM_SELECTIONS="clipboard"
export CM_MAX_CLIPS=10

# fzf configs
export FZF_DEFAULT_COMMAND="fd -HL"
export FZF_DEFAULT_OPTS="--color=16"

# dictd
export D_XTERM_CLASS="st256-color"
export D_XTERM_PROG="st -e"

# bat
export BAT_THEME="ansi"

# qt theme
export QT_QPA_PLATFORMTHEME="gtk2"
