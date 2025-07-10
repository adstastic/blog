---
title: "TIL: Chromium & Webkit treat markdown videos differently"
date: 2025-07-10T16:26:07+09:00
draft: false
tags: []
---

I just published [a post with gifs and videos](/p/claude-code-setup) and was pretty happy with how it was looking.
A few minutes later, a friend messaged me:
![whatsapp screenshot of friend telling me videos are broken](/assets/videos-broken-whatsapp-screenshot.png)

I use [Orion](https://kagi.com/orion/), which is a Webkit-based browser (like Safari). I know my friend uses Brave, a Chromium-based browser.
Why were these videos rendering fine in Webkit and not Chromium?

This blog is powered by [Hugo](https://gohugo.io/), and the posts written as Markdown. In that blog post, I had attached the videos using the markdown image syntax
```
![alt text](video.mp4)
```
which rendered to HTML as an `<img>` tag. This broke in Chromium because it strictly requires `<video>` tags for video content.

So how did it work in Webkit?

Turns out [Webkit supports displaying videos in `img` tags since 2018](https://webkit.org/blog/8216/new-webkit-features-in-safari-11-1/):
> Animated image formats are very popular, but they easily become large, bandwidth intensive file sizes. To address the performance impact, WebKit in Safari now supports loading H.264 encoded MP4 video with an HTML  tag. This allows content authors to replace animated GIF files that are much larger than H.264 video files and require more processing power to display. Beyond the performance gains, this change also allows web content authors to use videos as a CSS background-image.

I recommend reading the [deep dive on this](https://calendar.perfplanet.com/2017/animated-gif-without-the-gif/) for some interesting facts about browser performance and image formats.

## The fix

This was fixed by adding a [custom shortcode](https://gohugo.io/content-management/shortcodes/) that expanded to a `<video>` tag. Now, the following markdown:
```
{{</* video src="video.mp4" */>}}
```
renders to the following HTML:
```
<video controls width="100%">
  <source src="{{ .Get "src" }}" type="video/mp4">
  Your browser does not support the video tag.
</video>
```
with a nice little debug message if it doesn't work.

## The process

1. I summarise the issue in Claude Code, instructing it to verify using [Playwright](https://github.com/microsoft/playwright-mcp), fix, commit the fix to a new branch, and create a PR when finished
1. Claude verifies the issue, assumes (correctly) the problem is the markdown img tags, and decides to implement a custom shortcode
1. Claude messes up the shortcode syntax and the site doesn't build
1. I prompt Claude to use [Ref](https://ref.tools/) to find the docs for Hugo shortcodes
1. Claude finds the correct docs and implements a working video shortcode
1. Claude tries to verify the fix using Playwright
1. Claude hallucinates/misunderstands the videos are still not working
1. I can see that the issue is fixed, so I tell Claude
1. Claude checks out a new branch, commits & pushes the code, and creates a PR
1. I review the PR and merge

Steer count: 2
