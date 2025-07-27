---
title: "#474 – DHH: Future of Programming, AI, Ruby on Rails, Productivity &amp; Parenting"
date: 2025-07-26
slug: "474-dhh-future-of-programming-ai-ruby-on-rails-productivity-parenting"
tags:
  - quote
ref: https://share.snipd.com/episode/c977e2a3-7bd7-4268-81d2-9a3463425cfe
---

Quoting [Lex Fridman Podcast](https://share.snipd.com/episode/c977e2a3-7bd7-4268-81d2-9a3463425cfe):

> **Early Programming Struggles**

- David Heinemeier Hansson struggled learning programming as a child and youth despite early exposure to Commodore and Amiga computers.
- He finally found success learning PHP as a teenager, which led to his programming career.

Transcript:
Lex Fridman
For someone who became a legendary programmer, you officially got into programming late in life. And I guess that&#39;s because you tried to learn how to program a few times and you failed. So can you tell me the full story, the saga of your failures to learn programming? Was Commodore 64 involved?

David Heinemeier Hansson
Commodore 64 was the inspiration. I really wanted a Commodore 64. That was the first computer I ever sat down in front. And the way I sat down in front of it was I was five years old and there was this one kid on my street who had a Commodore 64. No one else had a computer. So we were all the kids just getting over there and we were all playing Yer Kung Fu. I don&#39;t know if you&#39;ve ever seen that game. It was one of the original fighting games. It&#39;s really a great game. And I was playing that for the first time at five years old. And we were like seven kids sitting up in this one kid&#39;s bedroom, all taking our turn to play the game. And I just found that unbelievably interesting. And I begged and I begged and I begged my dad, could I get a computer? And he finally comes home. He&#39;s like, I got your computer. I was like, yes, my own Commodore 64. And he pulls out this black, green, and blue keyboard. That&#39;s an Armstrong 464. I was like, dad, what&#39;s this? The disappointment. This is not a Commodore 64. But it was a computer. So I got my first computer at essentially six years old, that Armstrad 464. And of course, the first thing I wanted to do, I wanted to play video games. And I think the computer, which he, by the way, had traded for a TV and a stereo recorder or something like that, came with like two games. One was this frogger game where you had to escape from underground. It was actually kind of dark, like this frog, you&#39;re trying to get it out from underground. I was just, I was pretty bad at it. And I only had those two games and then I wanted more games. And one way to get more games when you&#39;re a kid who don&#39;t have a lot of money, I can&#39;t just buy a bunch of games is to type them in yourself. Back in 84, 85, magazines would literally print source code at the back of their magazines, and you could just sit and type it in. So I tried to do that, and it would take like two hours to print this game into the Amistad. And of course, I&#39;d make some spelling mistake along the way, and something wouldn&#39;t work, and the whole thing, I wasn&#39;t that good of English. I was born in Denmark. So I was really trying to get into it because I wanted all these games. I didn&#39;t have the money to buy them. And I tried quite hard for quite a while to get into it, but it just never clicked. And then I discovered the magic of piracy. And after that, I basically just took some time off from learning the program because, well, now suddenly I had access to all sorts of games. So that was the first attempt, like around six, seven years old. And what&#39;s funny is I remember these fragments. I remember not understanding the purpose of a variable. If there&#39;s a thing and you assign something, why would you assign another thing to it? So for some reason, I understand constants. Constants made sense to me, but variables didn&#39;t. Then maybe I&#39;m 11 to 12. I&#39;ve gotten into the Amiga at this point. The Amiga, by the way, still perhaps my favorite computer of all time. I mean, this is one of those things where you&#39;re like, people get older and they&#39;re like, the music from the 80s was amazing. To me, even as someone who loves computers or loved new computers, the Amiga was this magical machine that was made by the same company that produced the Commodore 64. And I got the Amiga 500, I think in 87.

Lex Fridman
Look at this sexy thing. That is a sexy machine right there.

David Heinemeier Hansson
This is from an age, by the way, where computing wasn&#39;t global in the same sense. The different territories had different computers that were popular. The Amiga was really popular in Europe, but it wasn&#39;t very popular at all in the US as far as I understand it. It wasn&#39;t popular in Japan. There were just different machines. The Apple II was a big thing in the US. I&#39;d never even heard of Apple in the 80s in Copenhagen. But the Amiga 500 was the machine that brought me to want to try it again. And you know what&#39;s funny? The reason I wanted to try it again was I remembered the first time to learn. And then there was this programming language that was literally called Easy Amos, like the easy version of Amos. I&#39;m like, if it&#39;s Easy Amos, how hard can it be? I got to be able to figure this out. And this time I tried harder. I got into conditionals. I got into loops. I got into all these things. And I still, I couldn&#39;t do it. And on the second attempt, I really got to the point of like, maybe I&#39;m not smart enough. Maybe programming is just not maybe it&#39;s too much math. Like, I like math in this sort of superficial way. I don&#39;t like it in the deep way that some of my perhaps slightly nerdier friends did, who I had tremendous respect for. I&#39;m like, I&#39;m not that person. I&#39;m not the math geek who&#39;s going to figure it all out. So after that attempt with Easy Amos and failing to even get, I don&#39;t even think I completed one even very basic game. I thought the program is just not for me. I&#39;m going to have to do something else. I still love computers. I still love video games. I actually at that time had already begun making friends with people who knew how to program, who weren&#39;t even programming Easy Amos. They were programming freaking Assembler.

> **Simplicity of Early Web Development**

- DHH chases the simplicity of late 90s PHP web development where deploying a dynamic webpage was incredibly easy.
- Modern web development has become overcomplicated, obscuring the underlying CRUD operations.

Transcript:
David Heinemeier Hansson
And it was essentially the easiest way to get a dynamic web page up and going. And this is one of the things I&#39;ve been chasing that high for basically the rest of my career, that it was so easy to make things for the internet in the mid to late 90s. How did we lose the sensibilities that allowed us to not just work this way, but get new people into the industry to give them their success experiences that I had, adding a freaking blink Tag to an HTML page, FTPing a PHP page to an Apache web server without knowing really anything about anything, without knowing anything about frameworks, without knowing anything About setup. All of that stuff have really taken us to a place where it sometimes feels like we&#39;re barely better off. Like webpages aren&#39;t that different from what they were in the late 90s, early 2000s. They&#39;re still just forms. They still just write to databases. A lot of people, I think, are very uncomfortable with the fact that they are essentially crud monkeys. They just make systems that create, read, update, or delete rows in a database. And they have to compensate for that existential dread by overcomplicating things. Now, that&#39;s a bit of a character. There&#39;s more to it. And there&#39;s things you can learn for more sophisticated ways of thinking about this. But there&#39;s still an ideal here, which is why I was so happy you had

> **Developer Ergonomics of 90s PHP**

- Late 1990s PHP was the pinnacle of developer ergonomics, offering instant deployment and simplicity.
- Modern frameworks should return to that ease without sacrificing progress.

Transcript:
David Heinemeier Hansson
And all that stuff started to make sense enough to me that I thought I can do this.

Lex Fridman
So would it be fair to say that we wouldn&#39;t have DHH without PHP and therefore you owe all your success to PHP?

David Heinemeier Hansson
A hundred percent, that&#39;s true. And it&#39;s even better than that because PHP to me didn&#39;t just give me a start in terms of making my own web applications. It actually gave me a bar. In many ways, I think the pinnacle of web developer ergonomics is late 90s PHP. You write this script. You FTP it to a server, and instantly it&#39;s deployed. Instantly it&#39;s available. You change anything in that file and you reload. Boom, it&#39;s right there. There&#39;s no web servers. There&#39;s no setup. There&#39;s just an Apache that runs mod.php. And it was essentially the easiest way to get a dynamic web page up and going. And this is one of the things I&#39;ve been chasing that high for basically the rest of my career, that it was so easy to make things for the internet in the mid to late 90s. How did we lose the sensibilities that allowed us to not just work this way, but get new people into the industry to give them their success experiences that I had, adding a freaking blink Tag to an HTML page, FTPing a PHP page to an Apache web server without knowing really anything about anything, without knowing anything about frameworks, without knowing anything About setup. All of that stuff have really taken us to a place where it sometimes feels like we&#39;re barely better off. Like webpages aren&#39;t that different from what they were in the late 90s, early 2000s. They&#39;re still just forms. They still just write to databases. A lot of people, I think, are very uncomfortable with the fact that they are essentially crud monkeys. They just make systems that create, read, update, or delete rows in a database. And they have to compensate for that existential dread by overcomplicating things. Now, that&#39;s a bit of a character. There&#39;s more to it. And there&#39;s things you can learn for more sophisticated ways of thinking about this. But there&#39;s still an ideal here, which is why I was so happy you had Peter Levels on. Because he still basically works like this. And I look at that and go, man, that&#39;s amazing.

Lex Fridman
Yeah, you&#39;re chasing that high. He&#39;s been high all along. Yes.

David Heinemeier Hansson
Using PHP, jQuery, and SQLite. I think it&#39;s amazing, because he&#39;s proving that this isn&#39;t just a nostalgic dream. He&#39;s actually doing it. He&#39;s running all these businesses. Now, some of that is, as he would admit up first, up front, is that he&#39;s just one guy and you can do different things when you&#39;re just one guy when you&#39;re working in a team when i started working On the team when i started working with jason freed on base camp we at first didn&#39;t use version control together i used version control for myself. And then I thought, you know what? Designers, they&#39;re probably not smart enough to figure out CBS. And therefore I just like, no, no, no, you just FTP it up. You just FTP it. I knew they knew how to do FTP. And then after the third time

> **FTP Instead of Version Control**

- David Heinemeier Hansson initially had designers FTP changes instead of using CVS version control. He eventually taught Jason Fried CVS after overwriting their changes multiple times.

Transcript:
David Heinemeier Hansson
And then I thought, you know what? Designers, they&#39;re probably not smart enough to figure out CBS. And therefore I just like, no, no, no, you just FTP it up. You just FTP it. I knew they knew how to do FTP. And then after the third time I had overridden their changes, I was like, God damn it. I guess I got to teach Jason CBS to not do that again. But I think there&#39;s still way more truth to the fact that we can work the way we did in the 90s, work the way Peter works today, even in the team context. And then we&#39;ve been far too willing to hand over far too much of our developer ergonomics to the merchants of complexity.

Lex Fridman
And you&#39;ve been chasing that with Rails 8. So how do you bring
