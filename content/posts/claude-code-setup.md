---
title: "My Claude Code setup"
date: 2025-07-10T11:27:04+09:00
draft: false
tags: [claude-code, devtools, list, living-document]
---
This is a list of the various things I've done to my claude code setup. A lot of it is not well documented, so I'm pulling it together as a master list here.

## Plan mode

Always hit shift-tab twice when starting a new session to have Claude plan first, then execute. Do the same when steering significantly, or starting a new task.
![switching to plan mode when starting claude code](/assets/plan-mode.gif)

## Background tasks

Add `export ENABLE_BACKGROUND_TASKS=1` in your shell profile to allow claude to run long-running tasks in the background.
![screenshot of the claude code background tasks terminal UI](/assets/claude-code-background-tasks.png)

## MCP servers

MCP servers can be local or remote. Installing them to claude code is either done by adding a block like:
```
"mcpServers": {
  "puppeteer": {
    "type": "stdio",
    "command": "npx",
    "args": [
      "-y",
      "u/modelcontextprotocol/server-puppeteer"
    ],
    "env": {}
  }
}
```
to Claude Desktop config and running `claude mcp add-from-claude-desktop`, or running a command like `claude mcp add --transport http Ref https://api.ref.tools/mcp?apiKey=YOUR_API_KEY`.

Skip the Claude Desktop step (unless you _also_ want Claude Desktop to have those MCPs) and add the code block directly to `~/.claude.json`.
When installing via the CLI, add `-s user` to populate the same part of the config file and use those MCPs from anywhere.

## Documentation

There are a lot of recommendations for the context7 MCP server, but I find [Ref](https://ref.tools/) faster, more reliable, and token-efficient. There's a generous free tier[^generous], so it's worth a try. Here's a side-by-side comparison on finding docs for Apple's Foundation Models framework:

{{< video src="/assets/ref-vs-context7-web-h264.mp4" >}}

[^generous]: Ref claims the 200 free tier credits last 10 weeks of typical usage.

## Teleoperation

I still use my [custom mobile dev setup](/p/remote-control-claude-code/), but [VibeTunnel](https://vibetunnel.sh) is far easier to set up, and has a bunch of nice UX improvements like mouse mode and session management. A setup like this let's me easily switch from my laptop to my phone, and continue working on stuff AFK. Having a server helps, but you can run it off a laptop too[^backpack]

[^backpack]: Just not when it's in clamshell mode in your backpack.

{{< video src="/assets/vibe-tunnel.mp4" >}}

## Optimisation

There's a lot of buzz about frameworks like [SuperClaude](https://github.com/NomenAK/SuperClaude) but [I'm pretty sure it doesn't work](https://github.com/NomenAK/SuperClaude/issues/83), and significantly pollutes the context window.
Rather than installing and learning a framework like this, I prefer to:
- optimise my global and project-level `CLAUDE.md`
- add custom commands for things I do often
- add MCPs sparingly

Configuring and optimising these tools is still very vibe-based, so it's surprisingly easy to fool yourself into thinking something works and adding layers of complexity you don't understand and don't need. [Keep it simple, stupid!](https://en.wikipedia.org/wiki/KISS_principle)
