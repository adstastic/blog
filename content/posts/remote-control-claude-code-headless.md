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

This post covers setting up a headless Mac mini for remote Claude Code access that survives system restarts. My [original remote control setup](/p/remote-control-claude-code/) works well for laptops but requires manual intervention after a Mac mini restart.

## Why tailscaled

According to [Tailscale's macOS comparison table](https://tailscale.com/kb/1065/macos-variants), there are three ways to run Tailscale on macOS. For headless servers, `tailscaled` is the only option that:

- Runs as a system daemon before user login
- Survives restarts without physical access
- Enables SSH access immediately after boot

The trade-offs include:
- No GUI
- Incomplete Taildrop support
- Partial exit node support
- Manual DNS configuration required
- No automatic updates
- Requires command-line management

## Prerequisites

- Mac mini for headless operation
- Another Mac for initial setup
- Tailscale account
- For mobile access: iPhone with [Blink Shell](https://blink.sh/) or similar
- Basic terminal knowledge

## Initial Setup (one-time physical access)

First, enable Remote Login on the Mac mini:
1. System Preferences → Sharing → Remote Login
2. Note the local IP address (like `192.168.1.100`)
3. SSH in from your other Mac: `ssh username@192.168.1.100`

Now let's install the basics:

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv)"

# Install dependencies
brew install go tmux mosh reattach-to-user-namespace
```

## Building tailscaled

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

Add to `~/.local.zsh` (and source it from `~/.zshrc`):

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

This automatically attaches SSH sessions to tmux while preserving iTerm2 integration mode.

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

## Client Setup

On your main Mac, add to `~/.zshrc`:

```bash
alias iron="ssh iron -t 'tmux -CC new-session -A -s main'"
```

This uses iTerm2's integration mode where tmux windows become native iTerm tabs.

On your iPhone with Blink:
1. Add your Tailscale host
2. Connect with: `mosh iron`

Mosh provides persistent connections that survive network changes.

## Usage

Start Claude Code in your tmux session:
```bash
claude
```

Key commands:
- Detach from tmux: `Ctrl-B D` (not `Ctrl-D` which kills the shell)
- From Mac: `iron` (opens native iTerm windows)
- From iPhone: `mosh iron` (persistent connection)
- Resume Claude after crash: `claude -c`

## Alternatives

For different use cases:

- **[VibeTunnel](https://vibetunnel.sh)**: Web-based terminal that still requires Tailscale but no tmux configuration
- **[Original setup](/p/remote-control-claude-code/)**: Better suited for laptops and non-headless machines
- **Native mobile apps**: Currently in development (e.g., https://x.com/0xKyon/status/1946660320275304827)

## Summary

This setup enables truly headless operation of a Mac mini running Claude Code. The key is using `tailscaled` as a system daemon, which is the only Tailscale variant that runs before user login. Combined with tmux for session persistence and mosh for reliable mobile connections, you get a robust remote development environment that survives restarts and network changes.
