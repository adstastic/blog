---
title: "Running a local coding agent with LM Studio and OpenCode"
date: 2025-08-07T11:39:09+09:00
slug: local-coding-agent
draft: false
tags: ["local ai", "coding", "claude code", "terminal agent", "opencode", "lm studio"]
---

I've been a huge fan of Claude Code since it launched. Over the past few months, I've been using it extensively across all kinds of projects. Claude Code is still the best tool out there, though others (Gemini CLI) are catching up. I recently discovered OpenCode, an open-source model agnostic framework that supports local models, and used it to test `gpt-oss-20b`, `qwen3-coder-30b` — currently the best open source coding models with tool calling.

This tutorial covers setting up OpenCode with LM Studio for local inference on a single machine.

# Setup

## LMStudio

[Ollama](https://ollama.com) is very popular, but I use [LM Studio](https://lmstudio.ai) because it has a nice UI and an [MLX](https://github.com/ml-explore/mlx) runtime which is very efficient for inference on Apple Silicon.

- Download [LM Studio](https://lmstudio.ai)
- Switch to Developer mode at the bottom left
![Developer mode](/assets/lms-developer.png)
- If you're on Apple Silcon, ensure you have the MLX backend installed
![Runtimes](/assets/lms-runtime.png)
- Download the right version of the model for your hardware
![gpt-oss-20b variants](/assets/gpt-oss-20b-variants.png)
- Go for the highest memory footprint you can fit on your hardware for best capabilities, the lowest for fastest inference
![qwen3-coder-30b variants](/assets/qwen3-coder-30b-variants.png)
- Run the LM Studio server
{{< video src="/assets/lms-start-server.mp4" alt="Running LM Studio server" >}}
- Load the model. Set the context window to at least 16k, otherwise there isn't enough context for OpenCode's prompts. Save these params for future.
{{< video src="/assets/lms-loading-qwen3-coder-30b.mp4" alt="Loading qwen3-coder-30b" >}}
- Test it works - copy the URL shown in `Reachable at` and curl `/v1/models`
{{< video src="/assets/lms-list-models.mp4" alt="curl API to list models" >}}

#### Fix qwen3-coder tool calling format

`qwen3-coder` with LMStudio's default system prompt template outputs tool calls as XML while OpenCode expects JSON. 
This isn't an issue with `gpt-oss` as it uses the new JSON-based [Harmony](https://github.com/openai/harmony) format.

![qwen3-coder-30b malformed tool call](/assets/qwen3-coder-30b-bad-tool-call.png)

Fix it by replacing the default template with one like [this](https://gist.github.com/adstastic/71632f39f4ea8d7facc2eddf0e46b3fd) and reloading the model.
{{< video src="/assets/lms-qwen3-sysprompt-template.mp4" alt="Updating a model's system prompt template" >}}


## OpenCode

- Install [OpenCode](https://opencode.ai)
- Create a config file at `~/.config/opencode/opencode.json` with the following, replacing `$BASE_URL` with the "Reachable At" URL from LM Studio:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "$BASE_URL/v1"
      },
      "models": {
        "openai/gpt-oss-20b": {
          "name": "gpt-oss-20b"
        },
        "qwen/qwen3-coder-30b": {
          "name": "qwen3-coder-30b"
        }
      }
    }
  }
}
```
- Run `opencode` and `/model` to select the model. It'll be listed under `LM Studio (local)`
{{< video src="/assets/opencode-models.mp4" alt="Selecting the model in OpenCode" >}}
- Keen an eye on the LM Studio server logs for any errors
- Enjoy!

### Hosting the model on another machine

I use an M4 Pro Mac Mini as a home server, on which I host many services. The LM Studio server is the latest one, which I use to drive OpenCode, [Open Webui](https://openwebui.com), [llm](https://github.com/simonw/llm), and call from other codebases. All my devices are connected via Tailscale, so the only change to these instructions is to set `baseURL` in the OpenCode config to the `tailscale serve` URL instead of the one from LM Studio.

# Review

## Capabilities

I've tested both `qwen3-coder-30b` and `gpt-oss-20b` on menial tasks I normally use Claude Code for:
- vibe coding a simple idea as a demo
- compressing GIFs to a certain size
- explaining what's going on a repo/directory

These workflows expose the gap between Claude Code and local models: while `qwen3-coder` and `gpt-oss` can make tool calls, they lack Claude's intelligent tool selection and the framework's reliability. 
I also tested these workflows with `gpt-oss-120b` hosted on [Cerebras](https://www.cerebras.ai), which is supposed to match `o4-mini`. It did well at coding and explaining, but couldn't complete the GIF compression task.

I highly recommend trying a [Cerebras](https://www.cerebras.ai) backend, with OpenCode, [Cline](https://inference-docs.cerebras.ai/integrations/cline), or their playground - the speed is incredible and it's got a free tier. Claude Code with such performance would be magical, no more waiting for responses.

{{< video src="/assets/gpt-oss-120b-cerebras-speed.mp4" alt="ultra fast inference with gpt-oss-120b on Cerebras" >}}

## Performance

Apple Silicon is very different from Nvidia hardware. With any local model, especially with a long context window, prefill is slow — often tens of seconds as context grows. But decoding is surprisingly fast. Simple Q&A prompts can actually run faster than Claude—without tool use or complex reasoning, you're eliminating network latency while running a smaller, faster model than 4.1 Opus.

Here's an example of the memory usage on my Mac Mini with loading and chatting with `gpt-oss-20b`, with [llm](https://github.com/simonw/llm) to make requests and [asitop](https://github.com/tlkh/asitop) to profile.

{{< video src="/assets/gpt-oss-20b-inference.mp4" alt="gpt-oss-20b inference" >}} 

#### `llm`

[llm](https://github.com/simonw/llm) is a fantastic tool with a rich plugin ecosystem that makes running simple prompts like this effortless. Here's a quick guide to setting it up with LM Studio:

- install `llm`
- go to `dirname "$(llm logs path)"`
- create `extra-openai-models.yaml` with contents:
```yaml
- model_id: gpt-20b
  model_name: openai/gpt-oss-20b
  api_base: "https://<api_url>/v1"
```
- run it with `llm -m gpt-20b '<your prompt here>'`

# Looking Forward

`qwen3-coder-30b` and `gpt-oss-20b` are the best open-source coding models I've tested at their parameter ranges. While this setup isn't ready to replace Claude Code for daily work, it's surprisingly capable for specific workflows. The real value is in rapid experimentation — when a new model drops, I can test it within minutes using familiar tools.

Next, I want to design a set of evals - not rigorous performance benchmarks, but small, self-contained, real world tasks like the above or Simon Willison's [SVG of a pelican on a bicycle](https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/) or [space invaders game](https://simonwillison.net/2025/Jul/29/space-invaders/), as a measure of how ready these models & frameworks are to migrate workflows off the cloud.

If there are any bugs in this tutorial, or if you have anything to add, please [email](mailto:hi@adim.in) or [DM](https://x.com/adstastic) me.
