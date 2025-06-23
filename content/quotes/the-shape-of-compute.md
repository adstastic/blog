---
title: "The Shape of Compute"
date: 2025-06-22
slug: "the-shape-of-compute"
tags:
  - quote
ref: https://share.snipd.com/episode/be60abdd-983f-4a34-9f4f-6834b293ddbb
---

Quoting [Latent Space: The AI Engineer Podcast](https://share.snipd.com/episode/be60abdd-983f-4a34-9f4f-6834b293ddbb):

> **Max Framework &amp; Modular Design**

- Modular&#39;s AI inference framework, Max, tightly integrates with Mojo and focuses on performance and control.
- It enables custom kernel fusion and reduces complexity, allowing easy modification of common models and clustering at scale.

Transcript:
Chris Lattner
So the inner circle is the programming language, right? And so it&#39;s a good way to make stuff go fast. The next level out is you say, okay, well, you know what&#39;s cool, AI. Have I convinced you? And so if you get into the world of AI, you start thinking about models. And beyond models, now we have Gen AI. And so you have things like pipelines, right? And the entire pipeline where you have KVCache orchestration and you have stateful batching. And I mean, you guys are the experts, agentic everything and all this kind of stuff. And so next level out is a very simple Gen AI inference focused framework we call Max. And so Max has a serving component. Is it Max Engine? Yeah, okay. We just call it Max. We got too complicated with sub-brands. This is also part of our R&amp;D on branding is that...

Speaker 2
HBO has the same problem.

Chris Lattner
Yeah, exactly. Like, who named LLVM? I mean, what the heck is that? Honestly, it&#39;s short.

Speaker 2
It&#39;s Googleable. Not the worst.

Chris Lattner
Yeah, and VLLM came and decided to mess with it. So Max, the way to think about it is it&#39;s not a PyTorch. That&#39;s not what it wants to be, but it&#39;s really focused on inference. It&#39;s really focused on performance and control and latency. And if you want to be able to write something that then gets Python out of the loop of the model logic, it&#39;s really good for control. And so it dovetails and is designed to work directly with Mojo. And so within a lot of LLM applications, as you all know, there&#39;s a lot of very customized GPU kernels. And so you have a lot of crazy forms of attention, like the DeepSeek things that just came out. And all this stuff is always changing. And so a lot of those are custom kernels. But then you have a graph level that&#39;s outside of it. And the way that has always worked is you have, for example, CUDA or things like TritonLang or things like this on the inside. And then you have Python on the outside. We&#39;ve embraced that model, like don&#39;t fix what ain&#39;t broken. So we use straight Python for the model level. And so we have an API. It&#39;s very simple. It&#39;s not designed to be fancy, but it feels kind of like a very simple PyTorch. And you can say, give me an attention block, give me these things, configure out these ops, but it directly integrates with Mojo. And so now you get full integration in a way that you can&#39;t get because none of the other frameworks and things like this can see into the code that you&#39;re running. And so this means that you get things like automatic kernel fusion. What&#39;s that? Well, that&#39;s a very fancy compiler technology that allows you to say, okay, you will write one version of flash attention, and then, cool, we can autofuse in Sulu and the other activation Functions that you might want to use, and you don&#39;t have to write all the permutations of these kernels. That just means you&#39;re more productive. That means you get better performance. It just drives down complexity in the system, and so you shouldn&#39;t have to know there&#39;s a fancy compiler. Everybody should hate compilers. The only reason people should know about compilers is if they&#39;re breaking, right? And so it just feels like a very nice, very ergonomic and efficient way to build custom models and customize existing models and things like this. And so with Max, we have five, 600, very common model families implemented in that. You can see builds.modular We have a whole bunch of models and you can scroll through them and you can get the source code and play with them and do that. That actually really great for people that care about serving and research and all this kind of stuff. Next layer out is you say, okay, well, you have a very fancy way to do serving on a single node. That&#39;s pretty useful and pretty important, but you know, it&#39;s actually cool. Large scale deployment. And so we have a next level out cluster level. And so that&#39;s the okay, cool. I have a Kubernetes cluster. I&#39;ve got a platform team. They&#39;ve got a three-year commit on 300 GPUs. And now I have product teams. I want to throw workloads against this shared pool of compute. And the folks carrying the pagers want the product teams to behave and so they want to keep track of what&#39;s actually happening. And so that&#39;s the cluster level that goes out and each of the and so very fancy prefix caching on a perno basis and then you have intelligent routing and there&#39;s a whole bunch of disaggregated Pre-fill and like a whole bunch of cool technologies at each of these layers but the the cool thing about it is that they&#39;re all co-designed and because the inside is heterogeneous you Can say, hey, I have some in AMD, I have some in Vida. Hey, I throw a model on there, run around the best architecture. Well, this actually simplifies a lot of the management problems. And so a lot of the complexity that we&#39;ve all internalized as being inherent to AI is actually really a consequence of these systems that are being designed together. And so to me, my number one goal right now is to drive out complexity, both of our stack, because we do have some tech debt that we&#39;re still fixing, but of AI in general.
