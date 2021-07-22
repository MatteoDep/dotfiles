# _________  _   _ ____   ____
# |__  / ___|| | | |  _ \ / ___|
#   / /\___ \| |_| | |_) | |
#  / /_ ___) |  _  |  _ <| |___
# /____|____/|_| |_|_| \_\\____|

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# Lines configured by zsh-newuser-install
HISTFILE=~/.cache/zsh/histfile
HISTSIZE=100000
SAVEHIST=100000
setopt extendedglob
setopt nomatch
setopt notify
unsetopt beep   # no annoying sounds

# Enable vim key bindings
source /usr/share/zsh/plugins/zsh-vi-mode/zsh-vi-mode.plugin.zsh

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

# enable sintax highlighting
source ${ZDOTDIR}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null

# ls colors nord theme
[ -r "$XDG_CONFIG_HOME/dir_colors" ] && eval $(dircolors "$XDG_CONFIG_HOME/dir_colors")

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
    PS1="%(?..%F{#ff0000}!%? )%F{blue}%1~%f%b \$vcs_info_msg_0_ %F{red}%(!.#.>)%f "
} || {
    zstyle ':vcs_info:git:*' formats ' %F{white} %b%f'
    PS1="%(?..%F{#ff0000}%? )%F{blue}%1~%f%b\$vcs_info_msg_0_ %F{red}%(!.#.)%f "
}

###########
# aliases #
###########

alias cp='cp -r'
alias v='nvim'
alias vi='nvim'
alias vim='nvim'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ls='lsd --group-dirs first'
alias ll='lsd -alF --group-dirs first'
alias la='lsd -A --group-dirs first'
alias p='sudo pacman'
alias cat='bat'
alias vifm='vifmrun'
alias d='devour'

#############
# functions #
#############

# cd recursively, press Esc when you are done
fzf-cd(){
    while choice=$({echo '..'; fd -HI -t d -d=1} | fzf --preview "previewer {}"); do
        cd "$choice"
    done
}

# cd recursively, press Esc when you are done
fzf-goto(){
    choice=$(locate / | fzf --preview "previewer {}")
    cd "$([ -d "$choice" ] && echo "$choice" || echo "${choice%/*}")"
}

# select multiple files to edit
fzf-open(){
    choices=$(fd -HL -t f | fzf -m --prompt "choose files: " --preview "previewer {}") &&
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
bindkey -s '^[e' 'vifm\n'
bindkey '^[i' fzf-locate-widget
bindkey -s '^[d' 'fzf-cd\n'
bindkey -s '^[f' 'fzf-open\n'
bindkey -s '^[g' 'fzf-goto\n'
bindkey '^[h' fzf-history-widget
bindkey -s '^[o' 'ipython --pylab --debug\n'
