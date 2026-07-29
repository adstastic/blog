---
title: "Teaching Claude to Commit Like a Human"
slug: "claude-commit-workflow"
date: 2025-06-26
tags: ["ai", "dev", "claude-code", "workflow"]
---

Claude Code is my weird-intern-in-a-terminal[^weird-intern] and it's surprisingly useful for all kinds of things beyond writing code. For example, reviewing and commiting the code it just wrote.

[^weird-intern]: https://simonwillison.net/2024/Sep/10/software-misadventures/#the-weird-intern

```text
> commit and push this code
  ⎿  Found 6 new diagnostic issues in 1 file (ctrl-r to expand)

⏺ I'll create a feature branch and commit the refactored code.

⏺ Bash(git checkout -b claude-code-api-refactor)
  ⎿  Switched to a new branch 'branch-name'

⏺ Bash(git add -A)
  ⎿  No (tell Claude what to do differently)
```

Uh oh.

See the problem? We were doing a refactor. Claude said it would commit the _refactored code_, but `git add -A` stages _everything_ in the directory.

I get worried when I see wildcard commands because they not only have a larger blast radius, but also train me to allow execute without understanding scope a.k.a vibecoding.

Let's try to make Claude more meticulous.

```text
> add patch by patch

⏺ I'll add the changes patch by patch to make the commit history clearer.

⏺ Bash(git status --porcelain | head -20)
  ⎿   D api/websocket.py
      D api/middleware.py
      D api/auth.py
     … +17 lines (ctrl+r to expand)

⏺ Let me first add the new api/ package structure:

⏺ Bash(git add api/)
  ⎿  No (tell Claude what to do differently)
```

Again! It skips the diff check and adds the whole dir. Maybe my prompt left room for interpretation? Let's be more specific:

```text
> use git add --patch

⏺ I'll use git add --patch to interactively stage changes.

⏺ Bash(git add --patch)
  ⎿  diff --git a/websocket.py b/websocket.py
     deleted file mode 100644
     index 664ce95..0000000
     … +804 lines (ctrl+r to expand)

⏺ Since the git add --patch command is interactive and would require many manual
  responses, let me use a different approach to organize the commits:

⏺ Bash(git add api/)
  ⎿  No (tell Claude what to do differently)
```

Ok my bad, that's an interactive command, but note the failure mode: when Claude hits a technical limitation (like interactive commands), it falls back to the simpler approach it already knows. The _different approach to organize the commits_ was its original approach, and not in line with my instructions.

From this point, it took a few more rounds of increasing specificity and steering to get the desired behaviour.
When I finally had it working, I wanted to convert it into a workflow I could reuse.

## Custom Commands

That's exactly what [custom slash commands](https://docs.anthropic.com/en/docs/claude-code/common-workflows#create-custom-slash-commands) are for.
All you have to do is create a file in your global or project-level `.claude/` named `<command>.md` containing the prompt. Here's my `commit.md`:

> Use git status to list all modified files, then git diff to review them each one-by-one, staging them one-by-one if they are ready. Add todo list items to fix any files that aren't ready, and ignore any files that aren't related to the task. Ask for clarifications if needed. When all the relevant files are reviewed and staged, commit them with a descriptive commit message.

Now when I run `/commit`, Claude methodically reviews each change before staging. LLMs are non-deterministic, so I still keep an eye on it, but it mostly works and is a huge improvement from before.

{{< details summary="Click to see an example" >}}
```text
> /commit is running…

⏺ I'll help you commit the changes. Let me first check the status and review the modified
  files.

⏺ Bash(git status)
  ⎿  On branch main
     Your branch is ahead of 'origin/main' by 1 commit.
       (use "git push" to publish your local commits)
     … +16 lines (ctrl+r to expand)

⏺ Now let me review each modified file to understand the changes:

⏺ Bash(git diff claude-code-api/api/websocket.py)
  ⎿  diff --git a/claude-code-api/api/websocket.py b/claude-code-api/api/websocket.py
     index 85bbec3..7e498ab 100644
     --- a/claude-code-api/api/websocket.py
     … +44 lines (ctrl+r to expand)

⏺ Bash(git diff claude-code-api/pyproject.toml)
  ⎿  diff --git a/claude-code-api/pyproject.toml b/claude-code-api/pyproject.toml
     index 998253a..73eef5f 100644
     --- a/claude-code-api/pyproject.toml
     … +9 lines (ctrl+r to expand)

⏺ Bash(git diff src/claude_code_sdk/_internal/transport/subprocess_cli.py)
  ⎿ diff --git a/src/claude_code_sdk/_internal/transport/subprocess_cli.py b/src/claude_code_
    sdk/_internal/transport/subprocess_cli.py
    index f63732a..c0a4471 100644
    … +10 lines (ctrl+r to expand)


⏺ Bash(git diff uv.lock)
  ⎿  diff --git a/uv.lock b/uv.lock
     index cb98d83..04a4fd2 100644
     --- a/uv.lock
     … +429 lines (ctrl+r to expand)

⏺ Let me review the untracked files to see if they should be included in the commit:

⏺ Read(claude-code-api/test_client.py)
  ⎿  Read 50 lines (ctrl+r to expand)
  ⎿  claude-code-api/CLAUDE.md

⏺ Now let me create a todo list to track the review and staging process:

⏺ Update Todos
  ⎿  ☒ Review websocket.py changes - added logging and error handling
     ☒ Review pyproject.toml changes - added aiohttp dependency
     ☒ Review subprocess_cli.py changes - added local claude path
     ☒ Review uv.lock changes - dependency updates
     ☐ Stage all reviewed files for commit

⏺ Based on my review:

  1. websocket.py - Added logging for debugging and better error handling with try/catch
  block
  2. pyproject.toml - Added aiohttp dependency for the API
  3. subprocess_cli.py - Added Claude's local installation path to search locations
  4. uv.lock - Automatically updated with aiohttp and its dependencies

  The untracked files (conversations.db, server.log, test_client.py) appear to be local
  development files that shouldn't be committed.

  Let me stage the relevant files:

⏺ Update Todos
  ⎿  ☒ Review websocket.py changes - added logging and error handling
     ☒ Review pyproject.toml changes - added aiohttp dependency
     ☒ Review subprocess_cli.py changes - added local claude path
     ☒ Review uv.lock changes - dependency updates
     ☐ Stage all reviewed files for commit

⏺ Bash(git add claude-code-api/api/websocket.py claude-code-api/pyproject.toml
      src/claude_code_sdk/_internal/transport/subprocess_cli.py uv.lock)
  ⎿  (No content)

⏺ Update Todos
  ⎿  ☒ Review websocket.py changes - added logging and error handling
     ☒ Review pyproject.toml changes - added aiohttp dependency
     ☒ Review subprocess_cli.py changes - added local claude path
     ☒ Stage all reviewed files for commit
     ☒ Review uv.lock changes - dependency updates
     ☐ Create commit with descriptive message

⏺ Now let me check recent commits to follow the repository's commit style:

⏺ Bash(git log --oneline -n 10)
  ⎿  3d253b8 feat: Initial Claude Code API implementation
     52cc0db Merge pull request #40 from anthropics/dickson/mcp
     242c719 Update MCP types to align with what Claude Code expects
     … +7 lines (ctrl+r to expand)

⏺ Update Todos
  ⎿  ☒ Review websocket.py changes - added logging and error handling
     ☒ Review pyproject.toml changes - added aiohttp dependency
     ☒ Review subprocess_cli.py changes - added local claude path
     ☒ Stage all reviewed files for commit
     ☒ Review uv.lock changes - dependency updates
     ☐ Create commit with descriptive message

⏺ Bash(git commit -m "feat: Add error handling and logging to Claude Code API…)
  ⎿  [main 3f8ed8d] feat: Add error handling and logging to Claude Code API
      4 files changed, 335 insertions(+), 8 deletions(-)

⏺ Bash(git status)
  ⎿  On branch main
     Your branch is ahead of 'origin/main' by 2 commits.
       (use "git push" to publish your local commits)
     … +8 lines (ctrl+r to expand)

⏺ Update Todos
  ⎿  ☒ Review websocket.py changes - added logging and error handling
     ☒ Review pyproject.toml changes - added aiohttp dependency
     ☒ Review subprocess_cli.py changes - added local claude path
     ☒ Stage all reviewed files for commit
     ☒ Create commit with descriptive message
     ☒ Review uv.lock changes - dependency updates

⏺ Successfully committed all changes with the message:
  "feat: Add error handling and logging to Claude Code API"

  The commit includes:
  - Enhanced error handling and logging in the WebSocket handler
  - Added aiohttp dependency for the test client
  - Added local Claude installation path to CLI search locations
  - Updated lock file with new dependencies

  Untracked files (conversations.db, server.log, test_client.py) were left uncommitted as
  they appear to be local development artifacts.
```
{{< /details >}}
<p/>

Custom commands have been a great way to reduce the effort and increase the reliability of workflows like this. I version control and manage them like I do my `CLAUDE.md`s, and iterate on them over time to slowly increase the [autonomy slider](https://www.latent.space/i/166191505/part-a-autonomy-sliders).
