#!/bin/zsh

# Default programs:
export EDITOR="nvim"
export TERMINAL="st"
export BROWSER="brave"
export EXPLORER="vifmrun"
export READER="zathura"
export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# Adds `~/.local/bin` to $PATH
export PATH="$PATH:$(du "$HOME/.local/bin/" | cut -f2 | grep -v '\.git' | paste -sd ':')"

# xdg specifications
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"
export ZDOTDIR="$XDG_CONFIG_HOME/zsh"
export IPYTHONDIR="$XDG_CONFIG_HOME/ipython"
export LESSHISTFILE=-
export NPM_CONFIG_USERCONFIG="$XDG_CONFIG_HOME/npm/npmrc"
export XAUTHORITY="$XDG_RUNTIME_DIR/Xauthority"
export GNUPGHOME="$XDG_CONFIG_HOME/gnupg"
export PASSWORD_STORE_DIR="$XDG_DATA_HOME/password-store"

# personal paths
export MYVIMRC="$XDG_CONFIG_HOME/nvim/init.vim"
export MYVIFMMRC="$XDG_CONFIG_HOME/vifm/vifmrc"
export DOTFILES_DIR="$HOME/.dotfiles"

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
export BAT_THEME="Nord"

# Start graphical server on tty1 if not already running.
[ "$(tty)" = "/dev/tty1" ] && ! pidof Xorg >/dev/null 2>&1  && exec startx -- vt1 &> /dev/null
