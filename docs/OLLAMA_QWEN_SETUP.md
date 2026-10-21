# Local Qwen (Ollama) Setup — Install, Chat, and Use with BugHunter

A complete, copy-pasteable guide to running BugHunter's AI brain **fully
offline and free**, using abliterated (uncensored) Qwen/DeepSeek models
through [Ollama](https://ollama.com). Covers installing Ollama, pulling the
models, chatting with them directly, using them inside BugHunter, and the
natural-language hunt launcher + live steering added on top of `agent.py`.

Tested on: Kali Linux (rolling), CPU-only (no discrete GPU), 15 GB RAM,
~100 GB free disk. Works the same on any Debian/Ubuntu-based Linux box —
adjust model sizes to your RAM if it's smaller.

---

## 1. Hardware reality check

Ollama needs roughly **RAM ≈ model's disk size** to run it without swapping
(a bit less thanks to mmap, but don't push it). Pick models that fit your
free RAM, not your total RAM — leave headroom for the OS and everything
else you have open.

| Your free RAM | Safe model size |
|---|---|
| ~4 GB | 3B–7B (Q4/Q5) |
| ~8 GB | 7B–8B |
| ~12 GB+ | 14B |
| 24 GB+ | 32B |

Check what you've actually got free before pulling anything:

```bash
free -h
```

---

## 2. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh -o /tmp/ollama_install.sh
sh /tmp/ollama_install.sh
```

This needs `sudo` and **must be run from a real interactive terminal** (not
piped through another tool) because it prompts for your password. It will:

- Download the `ollama` binary to `/usr/local/bin`
- Create a dedicated `ollama` system user and add you to the `ollama` group
- Install and enable `ollama.service` (systemd) — so it starts on boot and
  survives logout
- Print a warning if no GPU is detected (CPU-only mode — slower, still works)

Verify it's alive:

```bash
systemctl is-active ollama     # → active
ollama --version
curl -s http://localhost:11434 # → "Ollama is running"
```

If you just got added to the `ollama` group, open a **new terminal tab**
(or run `newgrp ollama`) before continuing — group membership doesn't
apply retroactively to an already-open shell.

---

## 3. Pull the abliterated models

"Abliterated" = refusal behavior surgically removed from the model weights.
These models will attempt whatever you ask, including offensive-security
tasks a stock-aligned model would refuse. **That responsibility is yours —
use them only within your engagement's authorization/scope.**

```bash
# General reasoning / strategist — 9.0 GB
ollama pull huihui_ai/qwen2.5-abliterate:14b

# Coder — payload/exploit scripts, JSON tool-calling — 4.7 GB
ollama pull huihui_ai/qwen2.5-coder-abliterate:7b

# Chain-of-thought reasoner — attack-tree / kill-chain planning — 5.0 GB
ollama pull huihui_ai/deepseek-r1-abliterated:8b
```

~19 GB total. Ollama loads one model into RAM at a time (and unloads it
after a few idle minutes), so pulling all three is fine even on a
15 GB-RAM box — it's only *running two at once* that would be tight.

Confirm they're installed:

```bash
ollama list
```

```
NAME                                     ID              SIZE      MODIFIED
huihui_ai/deepseek-r1-abliterated:8b     5ae823b61e22    5.0 GB    ...
huihui_ai/qwen2.5-coder-abliterate:7b    e30ab496af8a    4.7 GB    ...
huihui_ai/qwen2.5-abliterate:14b         a865def0555e    9.0 GB    ...
```

### Picking other sizes/models

Browse what exists for a family before pulling:

```bash
# in a browser: https://ollama.com/huihui_ai      (abliterated models)
# or:           https://ollama.com/search?q=qwen2.5
```

Smaller/bigger tags of the same models used above (swap `:14b` / `:7b` for
whichever fits your RAM): `huihui_ai/qwen2.5-abliterate:7b`, `:32b`,
`huihui_ai/qwen2.5-coder-abliterate:3b`, `:14b`, `:32b`,
`huihui_ai/deepseek-r1-abliterated:14b`, `:32b`.

---

## 4. Chat with a model directly (no BugHunter needed)

```bash
ollama run huihui_ai/qwen2.5-abliterate:14b
```

Drops you into an interactive prompt:

```
>>> hello
```

Type a message, press Enter, it replies. Useful in-chat commands:

| Command | Does |
|---|---|
| `/bye` or Ctrl+D | Quit |
| `/show info` | Model details |
| `/set system <text>` | Change the system prompt for this session |
| `/clear` | Wipe conversation history, keep the session open |

One-shot (no interactive session, good for scripting):

```bash
ollama run huihui_ai/qwen2.5-coder-abliterate:7b "write a Python port scanner"
```

Via the raw local API (for scripting against it from anything, any language):

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "huihui_ai/qwen2.5-abliterate:14b",
  "messages": [{"role": "user", "content": "hello"}],
  "stream": false
}'
```

CPU-only machines take a moment to produce the *first* token — once it
starts streaming, it's fine.

---

## 5. Using these models with BugHunter

**Nothing to configure.** `brain.py` (BugHunter's multi-provider LLM layer)
auto-detects Ollama and auto-picks a model: it checks a priority list of
known-good model names first, and if none of those are installed, it falls
back to "whatever's installed" — which, on a fresh machine with only the
three models above pulled, means it just works.

```bash
cd ~/claude-bug-bounty
./engine.py providers     # confirms Ollama is detected
./engine.py models        # lists what it sees + which one it'll use
./engine.py chat          # plain Q&A shell using whichever model it picked
```

To force a specific one instead of auto-pick:

```bash
BRAIN_PROVIDER=ollama python3 engine.py chat
```

(`brain.py` doesn't expose a `BRAIN_MODEL` override — model choice is
always auto-picked from what's installed. Keep only the model you want it
to use installed if you need to pin a specific one.)

---

## 6. The autonomous hunt agent (`agent.py`)

This is BugHunter's self-driving ReAct loop: give it a target, it decides
what to do next itself (recon → scan → analyze → repeat), using Ollama's
native tool-calling.

### 6a. Classic way — flags

```bash
cd ~/claude-bug-bounty
python3 agent.py --target example.com -d example.com -d '*.example.com' \
  --time 4 --max-steps 30
```

- `-d` / `--domain` — **required** to actually send traffic; without it,
  every tool call is blocked (fail-closed scope gate).
- `--cookie "JSESSIONID=..."` — authenticated session for logged-in testing
- `--scope-lock` — stick to the exact target only, no subdomain pivoting
- `--time` — hours budget (default 2)
- `--model` — override which Ollama model it uses

### 6b. New — just describe it in plain English

```bash
python3 agent.py --chat
```

It prompts you to type freely, multi-line, finishing with a blank line:

```
Describe the hunt — target, scope, test accounts, what to focus on.
End with a blank line (or Ctrl+D):

Hunt myco.io
Check grounds.myco.io, here are test accounts, check privilege escalation issues

```

It sends that to the local model once to extract target/scope/cookie/notes,
shows you what it understood, then starts the hunt immediately with those
notes already loaded into the agent's working memory — no extra flags, no
need to repeat "focus on privilege escalation" later:

```
[Chat] Understood:
  Target:  grounds.myco.io
  Scope:   grounds.myco.io
  Notes:   Hunt myco.io / Check grounds.myco.io / check privilege escalation issues
```

If it misreads your target, Ctrl+C immediately — nothing has run yet at
that point.

### 6c. Steer it while it's running (like Claude Code)

While a hunt from either 6a or 6b is running, just **type into the same
terminal and press Enter** at any time:

```
check the /api/v2/users endpoint for IDOR instead
```

It's picked up and folded into the agent's notes before its next decision —
you don't need a second terminal or to know any session ID. To stop the
hunt early:

```
/quit
```

(also accepts `/stop`, `exit`, `quit`)

This only activates when stdin is a real interactive terminal — running
`agent.py` from a script/cron/CI is unaffected and behaves exactly as
before.

### 6d. Cross-terminal guidance (the old way, still works)

If you'd rather fire-and-forget a note from a monitoring script instead of
keeping a terminal attached to the hunt:

```bash
# the running hunt prints this path at startup:
#   [Agent] Bump:  echo 'guidance here' > recon/<domain>/sessions/<id>/agent_bump.txt
python3 agent.py --bump recon/<domain>/sessions/<id> "focus on that login form"
```

---

## 7. Troubleshooting

| Symptom | Fix |
|---|---|
| `sudo: a terminal is required` during install | Run the install script yourself in an interactive shell, not through a wrapper/automation tool |
| `ollama run` says connection refused | `systemctl status ollama` — if not active, `sudo systemctl start ollama` |
| "No models found in Ollama" from `brain.py`/`agent.py` | `ollama list` — if empty, pull one of the models in §3 |
| Everything feels slow | Expected on CPU-only — no discrete GPU means no acceleration; smaller model = faster |
| `agent.py` tool-calling error / model ignores tools | Not every model supports native tool calling well; stick to the Qwen/DeepSeek families above, which do |
| RAM pressure / swapping heavily | You're running a model bigger than your free RAM — pull a smaller tag (see §1 table) |

---

## 8. Reproducing this exact setup on another PC

```bash
# 1. Clone BugHunter
git clone https://github.com/Awarexone/Agentic-Bug-Hunter.git claude-bug-bounty
cd claude-bug-bounty
chmod +x install.sh && ./install.sh

# 2. Install Ollama (run yourself — needs an interactive sudo prompt)
curl -fsSL https://ollama.com/install.sh -o /tmp/ollama_install.sh
sh /tmp/ollama_install.sh

# 3. Pull the models (~19 GB, adjust sizes to your free RAM per §1)
ollama pull huihui_ai/qwen2.5-abliterate:14b
ollama pull huihui_ai/qwen2.5-coder-abliterate:7b
ollama pull huihui_ai/deepseek-r1-abliterated:8b

# 4. Verify
ollama list
./engine.py providers

# 5. Go
python3 agent.py --chat
```

That's the whole setup — no config files to edit, no API keys, no account
to sign up for.

---

## Reminder

Abliterated models have no refusal training — they'll help with anything,
not just in-scope, authorized work. The authorization boundary lives with
you and your engagement's scope, not with the model.
