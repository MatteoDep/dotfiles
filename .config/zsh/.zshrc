# _________  _   _ ____   ____
# |__  / ___|| | | |  _ \ / ___|
#   / /\___ \| |_| | |_) | |
#  / /_ ___) |  _  |  _ <| |___
# /____|____/|_| |_|_| \_\\____|

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# Lines configured by zsh-newuser-install
mkdir -p ~/.cache/zsh
HISTFILE=~/.cache/zsh/histfile
HISTSIZE=100000
SAVEHIST=100000
setopt extendedglob
setopt nomatch
setopt notify
unsetopt beep   # no annoying sounds

# Enable vim key bindings
source /usr/share/zsh/plugins/zsh-vi-mode/zsh-vi-mode.plugin.zsh

# enable sintax highlighting
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# enable autosuggestions
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# ls colors
[ -r "$XDG_CONFIG_HOME/zsh/dir_colors" ] && eval $(dircolors "$XDG_CONFIG_HOME/zsh/dir_colors")

# Autocompletion
autoload -Uz compinit
zstyle ':completion:*' menu select  # enable menu selction
zstyle ':completion:*' rehash true  # automatically update for new executables in $PATH
zmodload zsh/complist
compinit
_comp_options+=(globdots)		# Include hidden files.

# history search matching what you have already written
autoload -U history-search-end
zle -N history-beginning-search-backward-end history-search-end
zle -N history-beginning-search-forward-end history-search-end
bindkey "^[[A" history-beginning-search-backward-end
bindkey "^[[B" history-beginning-search-forward-end

########################
# Prompt customization #
########################

# use variables in prompt
setopt prompt_subst
autoload -Uz vcs_info
precmd() { vcs_info }

read pcomm < /proc/$PPID/comm
[ "$pcomm" = "login" ]  && {
    zstyle ':vcs_info:git:*' formats '%F{white}(%b)%f'
    PS1="%(?..%F{#ff0000}!%? )%F{cyan}%1~%f%b \$vcs_info_msg_0_ %F{red}%(!.#.>)%f "
} || {
    zstyle ':vcs_info:git:*' formats ' %F{white} %b%f'
    PS1="%(?..%F{#ff0000}%? )%F{cyan}%1~%f%b\$vcs_info_msg_0_ %F{red}%(!.#.)%f "
}

###########
# aliases #
###########

alias cp='cp -r'
alias t='trash-put'
alias v='nvim'
alias vi='nvim'
alias vim='nvim'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ls='exa --group-directories-first --icons'
alias la='exa -a --group-directories-first --icons'
alias ll='exa -alhg --git --group-directories-first --icons'
alias lt='exa -alhg --tree --level=3 --git --group-directories-first --icons'
alias p='sudo pacman'
alias cat='bat'
alias d='devour'
alias monerod='monerod --data-dir "$XDG_DATA_HOME"/bitmonero'
alias monero-cli='monero-wallet-cli --wallet-file "$XDG_DATA_HOME"/bitmonero/wallet0 --log-file "$XDG_DATA_HOME"/bitmonero/monero-wallet-cli.log'
alias yt='ytfzf -tfl'
alias ytm='ytfzf -tml'

#############
# functions #
#############

# cd recursively, press Esc when you are done
fzf-cd(){
    while choice=$({echo '..'; fd -HI -t d -d=1} | fzf --preview "preview {}"); do
        cd "$choice"
    done
}

# cd recursively, press Esc when you are done
fzf-goto(){
    choice=$(locate / | fzf --preview "preview {}")
    cd "$([ -d "$choice" ] && echo "$choice" || echo "${choice%/*}")"
}

# select multiple files to edit
fzf-open(){
    choices=$(fd -HL -t f | fzf -m --prompt "choose files: " --preview "preview {}") &&
        echo $choices | xargs ${EDITOR:-vim}
}

# Paste the selected entry from history output into the command line
fzf-history-widget() {
  local choice
  choice=$(history count "$HISTSIZE" | sed -r 's/^.*  (.*)/\1/' | awk '!a[$0]++' | fzf --tac --prompt "choose command: ") &&
    LBUFFER="$LBUFFER$choice"
  zle redisplay
}
zle -N fzf-history-widget

# Paste the selected entry from locate output into the command line
fzf-locate-widget() {
  local choice
  if choice=$(locate / | fzf --prompt "choose path: "); then
    LBUFFER="$LBUFFER$choice"
  fi
  zle redisplay
}
zle -N fzf-locate-widget

# proxy on/off
proxy_on(){
    source "$ZDOTDIR/proxy_conf.zsh"
}
proxy_off(){
    for var in $(env | grep -i 'proxy' | cut -d '=' -f 1); do
        unset $var
    done
}


# KEY BINDINGS
bindkey -s '^[e' 'ranger\n'
bindkey '^[i' fzf-locate-widget
bindkey -s '^[d' 'fzf-cd\n'
bindkey -s '^[f' 'fzf-open\n'
bindkey -s '^[g' 'fzf-goto\n'
bindkey -s '^[p' 'ipython\n'
bindkey '^[h' fzf-history-widget
