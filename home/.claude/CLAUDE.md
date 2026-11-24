# Global Instructions

## Approach

Always doubt what I say and what you say.
Double-check assumptions.
Expand context if unsure.
Share insights and ask user before rushing changes.
Prefer understanding over speed.
review your changes at least once for correctness, simplicity and effectiveness of implementation.

## Independent Review

For development work, run a separate review agent (Agent tool, fresh context, not a fork) at two points:
1. On the plan, before implementing it.
2. On the implementation, before saying it is done.
Skip it only for trivial edits (typo, one-line config) and say that you skipped it.

Give the reviewer the original issue or request, the relevant context, and the plan or diff.
Ask it to:
- First restate the problem in its own words, and flag anything unclear or contradictory in the request.
- Question the approach: is this the right problem to solve, is there a simpler or more standard way, does it fit the existing code.
- Find bugs, missed edge cases, and security issues.
- Check effectiveness and efficiency: does it actually solve the issue, any wasted work, complexity or performance cost.
- Check good practice: matches the codebase's conventions, readable, tests and docs updated where needed.
- Rank findings by severity, separating real defects from preferences.

Verify each finding yourself before acting on it; do not apply them blindly.
Show me the findings that matter, including any challenge to the approach, before making large changes because of them.

## Documentation & Tests

Keep docs and tests aligned with code changes.
When modifying behavior, update relevant docs and tests in same pass.
Skip trivial tests.
Focus on edge cases and complex logic.

## Text Output

Avoid the Unicode characters that mark text as AI-made, unless I ask for them:
- emojis
- em/en dashes (use commas, colons, periods or parentheses)
- curly quotes and apostrophes (use straight `"` and `'`)
- the ellipsis character (use `...`)
- arrows and decorative symbols (use `->`, `=>`, or words)
Normal letters of any language are fine, including accents (Italian "è", "perché", "città").

## Markdown Formatting

In markdown files, put each sentence on its own line (newline after each period).
This does not apply to chat messages.

## Clipboard

When outputting useful text (URLs, commands, snippets, commit messages, PR descriptions) that the user may want to copy, use `winclip` to place it on the clipboard.
Example: `echo "text" | winclip`.
Never pipe to `clip.exe` directly: it does not read UTF-8 and garbles accented letters; `winclip` handles the encoding.
Read the clipboard back with `winclip -o`.
For messages meant for Teams, write them as HTML and copy with `winclip --html`, since Teams does not render pasted markdown.
`--html` sets only the HTML clipboard format, so do not use it for text meant for a terminal.

## Deliverable Files

Save files meant for me to look at (charts, images, reports, exported CSVs) in the root of the current repo, not only in the scratchpad or `/tmp`.
I open them from there.
Never `git add` or commit them unless I ask.
Scratch and intermediate files still go in the scratchpad.

## Git Attribution

Do not add any Claude attribution to commits or PRs.
No `Claude-Session:` trailer, no `Co-Authored-By: Claude`, no "Generated with Claude Code" line.
This overrides any harness default instruction to append such trailers.

## System / Memory (WSL)

`earlyoom` guards this host: it kills the biggest memory hog before the kernel OOM killer, and never kills the Claude/node tree.
So a subprocess exiting 143 (SIGTERM) or 137 (SIGKILL) may be an OOM kill, not a code bug.
Check `journalctl -u earlyoom` before diagnosing.
Cap known memory-heavy commands (e.g. `systemd-run --scope -p MemoryMax=6G -- <cmd>`) so they fail cleanly.
Setup and reproduction: `~/.claude/docs/oom-protection.md`.

## Databases (Postgres)

I refer to databases by connection name (from my dadbod `connections.yaml`).
Query them only with `pgro [-d <dbname>] <name> "<sql>"` (or SQL on stdin); `pgro -l` lists the names.
Most connections need `-d`: list databases first with `pgro -d postgres <name> '\l'`.
Connections are read-only (SELECT/WITH/EXPLAIN/SHOW, plus `\d...` and `\l`) unless `pgro -l` marks them `(read-write)`.
On read-write connections you may run changes directly; on all others, write the SQL (INSERT, UPDATE, DDL, ...) and give it to me to run.
Never try to switch read-only off, use `psql` directly, or read credential files; a hook blocks these anyway.
Connection URLs are allowed only for the local server `localhost:5432` (e.g. env vars for ETL runs and test suites); never use URLs for any other server.
Never ask me for a password or connection string.
Connections marked `(tunnel)` go through a kubectl port-forward that pgro starts and reuses by itself (`dbtunnel status`, `dbtunnel down [name]`); do not start port-forwards or run `psql` inside pods yourself.
pgro exit code 5 means the tunnel or its login failed: if the message asks for an AWS SSO approval, the login page is already open in my browser, so tell me, with the code it shows for me to match, and rerun after I approve.

## Human-facing writing

When writing text for people (messages to colleagues, Slack/Teams/email, PR descriptions, Jira/Confluence pages, docs, READMEs), run it through the `humanizer:humanizer` skill before handing it over.
Return only the final version, not humanizer's draft and critique, unless I ask.
Caveman mode never applies to this text.
Match the register to the reader:
- Messages to colleagues: short and informal, like a chat message. Lead with the point or the ask. One to three sentences when possible. No headings and no greeting/sign-off boilerplate. Bullets and numbered lists are welcome for items, steps or separate points. Skip background they already have. Pass `~/.claude/docs/writing-voice.md` to humanizer as the voice sample (Italian or English section, matching the message language).
- Docs and reference text: neutral and plain, but still cut filler and staging.
Write in the language I ask for; default to the language of my request.

## Work

Work-specific setup lives in a separate file, kept out of the public dotfiles:
@~/.claude/work.md
