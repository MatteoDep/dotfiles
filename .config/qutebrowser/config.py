"""qutebrowser configs.

NOTE: config.py is intended for advanced users who are comfortable
with manually migrating the config file on qutebrowser upgrades. If
you prefer, you can also configure qutebrowser using the
:set/:bind/:config-* commands without having to write a config.py
file.

Documentation:
  qute://help/configuring.html
  qute://help/settings.html
"""

import os

# get environment variables
TERMINAL = os.environ['TERMINAL']
EDITOR = os.environ['EDITOR']

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(True)

# PRIVACY
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

# BINDINGS
config.bind('tt', 'config-cycle -t -p content.proxy socks://localhost:9050/ system none ;; reload')
config.bind(',c', 'config-edit')
config.bind(',s', 'config-source')
config.bind('ci', 'config-cycle -p colors.webpage.darkmode.enabled false true ;; restart')
stylesheets=" ".join(os.listdir(os.path.expanduser('~/.config/qutebrowser/css')))
config.bind('cs', 'config-cycle -p content.user_stylesheets ' + stylesheets + ' \'\' ;; reload')
config.bind(';v', 'hint links spawn mpv {hint-url}')
config.bind('ym', 'yank inline [{title}]({url:pretty})')
config.bind('gT', 'set-cmd-text :tab-take ')
config.bind('I', 'mode-enter passthrough')
config.bind('<Ctrl-v>', 'mode-enter insert ;; insert-text -- {clipboard} ')
c.content.blocking.enabled = True
c.content.blocking.method = 'both'
c.content.geolocation = False
searchengines = {
    'bs': 'https://search.brave.com/search?q={}',
    'ddg': 'https://duckduckgo.com/?q={}',
    'ddgt': 'https://3g2upl4pq6kufc4m.onion/?q={}',
    'aw': 'https://wiki.archlinux.org/?search={}',
    'wp': 'https://en.wikipedia.org/w/index.php?search={}',
    'wb': 'https://en.wikibooks.org/w/index.php?search={}',
    'gh': 'https://github.com/search?q={}',
    'wr': 'https://www.wordreference.com/definition/{}',
    'gt': 'https://translate.google.com/?text={}',
    'gs': 'https://scholar.google.com/scholar?q={}',
    'hl': 'https://hoogle.haskell.org/?hoogle={}',
    'aur': 'https://aur.archlinux.org/packages/?O=0&K={}'
}
searchengines['DEFAULT'] = searchengines['bs']
c.url.searchengines = searchengines
config.bind('<Ctrl-o>', 'set-cmd-text :open -t  {primary} ;; rl-beginning-of-line ;; rl-forward-word ;; rl-forward-word ;; rl-forward-char ;; rl-forward-char')
c.url.default_page = "https://search.brave.com"
c.url.start_pages = [c.url.default_page]
c.editor.command = [TERMINAL, '--class', 'floatterm', '-e', EDITOR, '{file}']
c.downloads.location.directory = '~/downloads'
c.downloads.location.prompt = False
c.downloads.remove_finished = 3000
c.colors.webpage.preferred_color_scheme = "dark"

#########
# THEME #
#########

# Start flavours
# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova and Daniel Mulford
# Harmonic16 Dark scheme by Jannik Siebert (https://github.com/janniks)

base00 = "#0b1c2c"
base01 = "#223b54"
base02 = "#405c79"
base03 = "#627e99"
base04 = "#aabcce"
base05 = "#cbd6e2"
base06 = "#e5ebf1"
base07 = "#f7f9fb"
base08 = "#bf8b56"
base09 = "#bfbf56"
base0A = "#8bbf56"
base0B = "#56bf8b"
base0C = "#568bbf"
base0D = "#8b56bf"
base0E = "#bf568b"
base0F = "#bf5656"

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base00

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0D

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base05

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base02

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = base02

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base02

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base05

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base09

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = base01

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = base04

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = base00

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  base05

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = base02

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = base05

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base02

# Foreground color for the selected item in filename prompts.
c.colors.prompts.selected.fg = base05

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base05

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base0C

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base00

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base0A

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base00

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base0E

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base00

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base05

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base01

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base0E

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base01

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base0D

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base00

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base0D

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base00

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base09

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0B

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base00

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base00

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0B

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base00

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base00

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base02

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base05

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base02

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base05

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base05

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base02

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base05

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base02

# Background color for webpages if unset (or empty to use the theme's
# color).
# c.colors.webpage.bg = base00
# End flavours
