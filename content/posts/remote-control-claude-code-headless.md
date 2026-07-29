---
title: "My mobile claude code setup"
date: 2025-07-26
slug: "mobile-claude-code"
tags:
  - dev
  - ai
  - claude
  - macos
  - tailscale
---

I previously wrote about [using Claude Code from my phone](/p/remote-control-claude-code/).  
Since then, I've ported that to a headless Mac Mini. This is the updated setup.

## Why

One of the [key principles of working with agents](/p/tai-talk) is to steer early and often. You can only do that if you keep an eye on them. This setup enables me to connect to a Claude Code session running on my Mac Mini at home from my phone and macbook, so I can seamless switch between them. This allows me to start work on my laptop, leave it running, and keep an eye on it while I'm away.

## Prerequisites

- An always-online Mac you can use as a server (doesn't have to be a Mac Mini)
- Another computer for initial setup
- [Tailscale](https://tailscale.com) account
- A phone with a terminal app
- Basic terminal knowledge

## Initial Setup

This is the only step where you need physical access to the Mac Mini.

Tip: If you have another Mac, you can use that Mac's mouse/keyboard to control the Mac Mini if you login to your iCloud account.

1. Setup the Mac Mini with a user account and connect to your WiFi
1. System Preferences → Sharing → Remote Login
1. Note the local IP address (e.g. `192.168.1.100`)
3. SSH in from your other laptop: `ssh username@192.168.1.100`

## Continue over SSH

Now let's install the basics:

```bash
# Install [Homebrew](https://brew.sh)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv)"

# Install dependencies
brew install go tmux reattach-to-user-namespace

# Optional: Install mosh for reliable mobile connections
# if your mobile shell app supports it
brew install mosh
```

## tailscaled

According to [Tailscale's macOS comparison table](https://tailscale.com/kb/1065/macos-variants), there are three ways to run Tailscale on macOS. 
The trade-offs include:
- No GUI
- Incomplete Taildrop support
- Partial exit node support
- Manual DNS configuration required
- No automatic updates
- Requires command-line management

In my original post, I tried then dropped tailscaled because of these tradeoffs.  
However, for headless servers, it's the only option that works because:

- Runs as a system daemon before user login
- Survives restarts without physical access
- Enables SSH access immediately after boot

### Install

Build and install tailscaled from source:

```bash
# Build tailscaled from source
export PATH=$PATH:$(go env GOPATH)/bin
go install tailscale.com/cmd/tailscale{,d}@main

# Install as system daemon
sudo $(which tailscaled) install-system-daemon

# Connect to your tailnet
sudo tailscale up
```

The daemon will now start automatically on boot, before any user logs in.

## tmux Configuration

Create `~/.tmux.conf`:

```bash
# macOS clipboard integration
set-option -g default-command "reattach-to-user-namespace -l $SHELL"

# Enable mouse mode for mobile
set -g mouse on

# Reasonable history limit
set -g history-limit 10000

# Start numbering at 1
set -g base-index 1
setw -g pane-base-index 1
```

## Auto-attach Configuration

For a seamless experience, you need to auto attach to the same tmux session on SSH login. 
I sync my dotfiles between machines, and I don't want this behaviour on my laptop, so I put local bits like this in `~/.local.zsh` (and source it from `~/.zshrc`).

```bash
# Auto-attach to tmux session for SSH connections (except iTerm2 -CC mode)
if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
    # Check if we're not using iTerm2's control mode and not already in tmux
    if [[ ! "$SSH_ORIGINAL_COMMAND" =~ "-CC" ]] && [ -z "$TMUX" ]; then
        # Try to attach to existing session named 'main', or create new one
        tmux attach-session -t main 2>/dev/null || tmux new-session -s main
    fi
fi
```

I use [iTerm2](https://iterm2.com) as my shell, and  `-CC` enables its [tmux integration](https://iterm2.com/documentation-tmux-integration.html), where tmux windows become native iTerm tabs.
You probably don't need it if you use another shell.

## Security Hardening

After Tailscale SSH is working, secure the system:

```bash
# Disable standard SSH (we're using Tailscale SSH now)
sudo systemsetup -setremotelogin off

# Enable firewall with stealth mode
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on

# Allow tailscaled through firewall
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add $(which tailscaled)
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --unblockapp $(which tailscaled)

# Prevent sleep (optional but recommended for servers)
sudo pmset -a sleep 0
sudo pmset -a disksleep 0
```

## Optional: Enable MagicDNS

Unlike the GUI versions, `tailscaled` doesn't configure DNS automatically. To use MagicDNS (which allows using hostnames instead of IP addresses):

```bash
# Set DNS to Tailscale's MagicDNS server
networksetup -setdnsservers Wi-Fi 100.100.100.100
# or for Ethernet:
networksetup -setdnsservers Ethernet 100.100.100.100
```

See the [Tailscaled on macOS wiki](https://github.com/tailscale/tailscale/wiki/Tailscaled-on-macOS) for more details.
This is only required if you want to use MagicDNS **from the server** e.g. to access other services on your tailnet.

## Client Setup

### Laptop

On your laptop, add to `~/.zshrc`:

```bash
alias macmini="ssh macmini -t 'tmux -CC new-session -A -s main'"
```

Again, if you aren't using iTerm2, you can probably omit the `-CC` flag.

### Phone

Download the Tailscale app and connect to your tailnet.
Download a mobile shell app.  
I use [Blink](https://blink.sh). Free alternative: [Termius](https://termius.com).

Connect to your server with `ssh` or [Mosh](https://mosh.org) for more reliable mobile connections.
```bash
mosh adi@macmini
```

Mosh provides persistent connections that survive network changes.

## Usage

If you setup things the way I did:
- Connect from laptop: `macmini` (opens native iTerm windows)
- Connect from iPhone: `mosh macmini` (persistent connection)

The first time (or when the auth expires), Tailscale will pop a login window, it's a seamless experience.

### Key commands:

- Detach from tmux: `Ctrl-B D` (not `Ctrl-D` which kills the shell)
- Resume Claude after an interrupted session: `claude -c`

If you kill or leave the the tmux session, just logout and login again. You'll automatically reconnect to the existing session if it still exists, or a new one will be created.

## Alternatives

Any kind of homelab setup needs Tailscale, but you can skip all the terminal steps if you just want a Claude Code session with **[VibeTunnel](https://vibetunnel.sh)**, a Web-based experience. It's pretty nice but I prefer the mobile UX of a terminal app so I mostly use my setup.

People are building **native mobile apps** for this, so at some point there will be a really polished experience. I'm on the waitlist for [Kisuke](https://x.com/0xKyon/status/1946660320275304827) which seems like a really polished experience.

If you don't have a server, refer to my **[original setup](/p/remote-control-claude-code/)** for running this on your laptop, so you can still leave your desk without leaving Claude.

## Summary

This setup enables truly headless operation of a Mac mini running Claude Code. The key is using `tailscaled` as a system daemon, which is the only Tailscale variant that runs before user login. Combined with tmux for session persistence and mosh for reliable mobile connections, you get a robust remote development environment that survives restarts and network changes.

Any bugs, improvements, or questions, please [email](mailto:hi@adim.in) or [DM](https://x.com/adstastic) me.
