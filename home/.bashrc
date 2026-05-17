# variables
export RIPGREP_CONFIG_PATH=~/.config/ripgreprc
export EDITOR=nvim
export BROWSER=wslview
export WH=/mnt/c/Users/MatteoDePellegrin
export WS="${WH}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
export FZF_DEFAULT_COMMAND='fd -HL'
export FZF_DEFAULT_OPTS='--color=16,border:-1 --layout=reverse --cycle --border'

# path
echo "$PATH" | grep -qv 'go/bin' && PATH="$(go env GOPATH)/bin:${PATH}"
PATH="/home/linuxbrew/.linuxbrew/opt/postgresql@16/bin:$PATH"
export PATH
export DOTNET_ROOT="/home/linuxbrew/.linuxbrew/opt/dotnet/libexec"

# fix shell escaping env var on autocomplete
shopt -s direxpand

# history
HISTSIZE=5000
HISTFILESIZE=10000
shopt -s histappend

# vi mode
set -o vi

# prompt
export PROMPT_COMMAND=__prompt_command

__parse_git_dirty(){
    [ "$(git status --porcelain 2> /dev/null)" ] && echo "*"
}
__parse_git_branch(){
    git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e "s/* \(.*\)/ (\1$(__parse_git_dirty))/"
}
__parse_python_venv(){
    local venv
    if [ ${VIRTUAL_ENV} ]; then
        venv="($(basename "${VIRTUAL_ENV}")) "
    fi
    if [ ${VIRTUAL_ENV_PROMPT} ]; then
        venv="(${VIRTUAL_ENV_PROMPT}) "
    fi
    if [ ${CONDA_PROMPT_MODIFIER} ]; then
        venv="${CONDA_PROMPT_MODIFIER}"
    fi
    echo "$venv"
}

__prompt_command(){
    local EXIT="$?"  # This needs to be first
    PS1=""
    history -a; history -c; history -r;

    local reset_col='\[\e[0m\]'
    local red='\[\e[0;31m\]'
    local blu='\[\e[0;34m\]'

    if [ $EXIT != 0 ]; then
        PS1+="${red}!${EXIT} ${reset_col}"
    fi

    PS1+="$(__parse_python_venv)${blu}\w${reset_col}$(__parse_git_branch) ${red}\$${reset_col} "
}

# bindings
bind -x '"\C-l": clear'
bind '"\eg":"lazygit\n"'

# aliases
alias grep='grep --color=auto'
alias ls='exa --group-directories-first --icons'
alias la='exa -a --group-directories-first --icons'
alias ll='exa -alhg --group-directories-first --icons'
alias lt='exa -alhg --tree --level=3 --group-directories-first --icons'
alias cat='bat'
alias t='tmux-start'
alias v='nvim-start'
alias pydbg='python -m debugpy --listen localhost:5678 --wait-for-client'

export NVM_DIR="$HOME/.nvm"
[ -s "/home/linuxbrew/.linuxbrew/opt/nvm/nvm.sh" ] && \. "/home/linuxbrew/.linuxbrew/opt/nvm/nvm.sh"  # This loads nvm
[ -s "/home/linuxbrew/.linuxbrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/home/linuxbrew/.linuxbrew/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion

# pnpm
export PNPM_HOME="/home/matteo/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

export PATH=/home/matteo/.oracle/bin:$PATH

eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

if [ -e "/home/matteo/.oracle/lib/lib/python3.10/site-packages/oci_cli/bin/oci_autocomplete.sh" ]; then source "/home/matteo/.oracle/lib/lib/python3.10/site-packages/oci_cli/bin/oci_autocomplete.sh"; fi
if [ -e "$HOME/.cargo/env" ]; then source "$HOME/.cargo/env"; fi
