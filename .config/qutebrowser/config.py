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

import subprocess

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
# config.bind('ci', 'set colors.webpage.darkmode.enabled false true ;; restart')
config.bind('i', 'hint inputs')

# SETTINGS
c.url.searchengines = {
    'DEFAULT': 'http://duckduckgo.com/?q={}',
    'ddgt': 'https://3g2upl4pq6kufc4m.onion/?q={}',
    'aw': 'https://wiki.archlinux.org/?search={}',
    'wp': 'https://en.wikipedia.org/w/index.php?search={}',
    'gh': 'github https://github.com/search?q={}'
}
c.editor.command = ['st', '-e', 'nvim', '{file}']
c.downloads.location.directory = '~/downloads'
c.downloads.location.prompt = False
c.downloads.remove_finished = 3000

#########
# THEME #
#########

# c.colors.webpage.darkmode.enabled = True


def read_xresources(prefix):
    """Read colors from Xresources."""
    props = {}
    x = subprocess.run(['xrdb', '-query'], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split('\n')
    for line in filter(lambda l: l.startswith(prefix), lines):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props


xresources = read_xresources('*')
print(xresources)
c.colors.completion.category.bg = xresources['*.background']
c.colors.completion.category.border.bottom = xresources['*.background']
c.colors.completion.category.border.top = xresources['*.background']
c.colors.completion.category.fg = xresources['*.color7']
c.colors.completion.even.bg = xresources['*.color0']
c.colors.completion.odd.bg = xresources['*.color0']
c.colors.completion.fg = xresources['*.foreground']
c.colors.completion.item.selected.bg = xresources['*fadeColor']
c.colors.completion.item.selected.border.bottom = xresources['*fadeColor']
c.colors.completion.item.selected.border.top = xresources['*fadeColor']
c.colors.completion.item.selected.fg = xresources['*.color15']
c.colors.completion.match.fg = xresources['*.color11']
c.colors.completion.scrollbar.bg = xresources['*.color0']
c.colors.completion.scrollbar.fg = xresources['*.color7']
c.colors.downloads.bar.bg = xresources['*.background']
c.colors.downloads.error.bg = xresources['*.color9']
c.colors.downloads.error.fg = xresources['*.color7']
c.colors.downloads.stop.bg = xresources['*.color13']
c.colors.downloads.system.bg = 'none'
c.colors.hints.bg = xresources['*.color11']
c.colors.hints.fg = xresources['*.background']
c.colors.hints.match.fg = xresources['*.color4']
c.colors.keyhint.bg = xresources['*.color0']
c.colors.keyhint.fg = xresources['*.color7']
c.colors.keyhint.suffix.fg = xresources['*.color11']
c.colors.messages.error.bg = xresources['*.color9']
c.colors.messages.error.border = xresources['*.color9']
c.colors.messages.error.fg = xresources['*.color7']
c.colors.messages.info.bg = xresources['*.color6']
c.colors.messages.info.border = xresources['*.color6']
c.colors.messages.info.fg = xresources['*.color7']
c.colors.messages.warning.bg = xresources['*.color11']
c.colors.messages.warning.border = xresources['*.color11']
c.colors.messages.warning.fg = xresources['*.color7']
c.colors.prompts.bg = xresources['*.color0']
c.colors.prompts.border = '1px solid ' + xresources['*.background']
c.colors.prompts.fg = xresources['*.color7']
c.colors.prompts.selected.bg = xresources['*fadeColor']
c.colors.statusbar.caret.bg = xresources['*.color13']
c.colors.statusbar.caret.fg = xresources['*.color7']
c.colors.statusbar.caret.selection.bg = xresources['*.color13']
c.colors.statusbar.caret.selection.fg = xresources['*.color7']
c.colors.statusbar.command.bg = xresources['*.color0']
c.colors.statusbar.command.fg = xresources['*.color7']
c.colors.statusbar.command.private.bg = xresources['*.color0']
c.colors.statusbar.command.private.fg = xresources['*.color7']
c.colors.statusbar.insert.bg = xresources['*.color2']
c.colors.statusbar.insert.fg = xresources['*.color0']
c.colors.statusbar.normal.bg = xresources['*.background']
c.colors.statusbar.normal.fg = xresources['*.color7']
c.colors.statusbar.passthrough.bg = xresources['*.color4']
c.colors.statusbar.passthrough.fg = xresources['*.color7']
c.colors.statusbar.private.bg = xresources['*fadeColor']
c.colors.statusbar.private.fg = xresources['*.color7']
c.colors.statusbar.progress.bg = xresources['*.color7']
c.colors.statusbar.url.error.fg = xresources['*.color9']
c.colors.statusbar.url.fg = xresources['*.color7']
c.colors.statusbar.url.hover.fg = xresources['*.color6']
c.colors.statusbar.url.success.http.fg = xresources['*.color7']
c.colors.statusbar.url.success.https.fg = xresources['*.color2']
c.colors.statusbar.url.warn.fg = xresources['*.color11']
c.colors.tabs.bar.bg = xresources['*fadeColor']
c.colors.tabs.even.bg = xresources['*fadeColor']
c.colors.tabs.even.fg = xresources['*.color7']
c.colors.tabs.indicator.error = xresources['*.color9']
c.colors.tabs.indicator.start = xresources['*.color13']
c.colors.tabs.indicator.stop = xresources['*.color11']
c.colors.tabs.indicator.system = 'none'
c.colors.tabs.odd.bg = xresources['*fadeColor']
c.colors.tabs.odd.fg = xresources['*.color7']
c.colors.tabs.selected.even.bg = xresources['*.background']
c.colors.tabs.selected.even.fg = xresources['*.color7']
c.colors.tabs.selected.odd.bg = xresources['*.background']
c.colors.tabs.selected.odd.fg = xresources['*.color7']
c.colors.webpage.bg = xresources['*.background']
