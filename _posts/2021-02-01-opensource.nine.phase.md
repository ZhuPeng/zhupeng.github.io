---
layout: post
title: 开源项目维护的九个阶段
tags: 翻译
---

大家好。

> 本文为翻译，原文为：[https://nibblestew.blogspot.com/2020/11/the-nine-phases-of-open-source-project.html](https://nibblestew.blogspot.com/2020/11/the-nine-phases-of-open-source-project.html)

文章标题为：开源项目维护的九个阶段



There is more to running an open source project than writing code. In fact most of all work has to do with something else. This places additional requirements to project maintainers that are often not talked about. In this post we'll briefly go over nine distinct phases each with a different hat one might have to wear. These can be split into two stages based on the lifetime and popularity of the project.

# Stage One: The Project Is Mostly for Yourself

Almost all projects start either with just one person or a small team of just a few people. At the start doing things is easy. Breaking changes can be made on a whim. Programming languages and frameworks can be changed. It is even possible to pivot to something completely different without a care in the world. As there are only a few stakeholders and they typically have similar ideologies and thus it is easy to get consensus. It is even possible to ignore consensus altogether and "just do it".

## Phase One: The Inventor

Everything starts with an idea: how something could be done differently or in a more efficient way. This is the part that tends to get fetishised by journalists and even some inventors themselves. The typical narrative explains how a single genius managed to create a revolutionary new thing all on their own in a basement somewhere. The reality is not quite as glamorous, as almost all ideas are ones that many, many other people have already come up with. Some people go as far as to say that ideas are worthless, only execution matters. This is a bit extreme but nevertheless coming up with ideas is an important skill.

## Phase Two: The MVP Implementer

Once an idea is chosen, some sort of a prototype needs to be written. This is the most fun part of coding. There are vast green fields where you can do whatever, design the architecture as you want and get to solve interesting problems that form the core of the eventual proudct. This phase is the main reason why people become programmers. Getting to create something completely new is a joyful experience. Still, not everything is wine and roses, as it is important to focus enough to get the first version finished rather than going off on all sorts of tangents and eventually losing interest.

## Phase Three: The Ditch Digger

Once the first version exists and is found usable, the next step is to make it production ready. This is where the nature of project work takes a very sharp turn. Whereas the previous stage could be described as fun, this phase is tedious. It consists of making the end product reliable and smooth in the face of real world input and usage. This typically exposes bugs and design flaws in the original implementation that need to be fixed or rewritten. It is easy to get discouraged in this phase because the outcome of days of coding might be "the same as before, but also handles this one rare corner case".

The work profile is similar to digging a ditch with a shovel. It's dirty, heavy and taxing work and there are not that many rewards to be had. After all, a half dug ditch is about as useless as a completely undigged ditch. It's only when you reach the end and water starts flowing that you get any benefits. The difference between physical ditches and sotware is that there is no reliable way of estimating how much more you still have to dig. This is a very risky phase of any project as it carries the potential for burnout.

## Phase Four: The Documentation Writer

Every new project needs documentation, but some projects need it more than others. Programmers are typically not very eager to write documentation or to keep it up to date. Telling users to "read the source" to find out how to do things is not enough, because people don't want to have to learn about implementation details of your project, they just want to use it. Sometimes it is possible to get other people to write documentation, but usually that only happens after the project has "made it big".

One way of looking at documentation is that it is a competitive advantage. If there are multiple competing projects for the same thing and one of them has better documentation, it has a higher chance of winning (all other things being equal). Writing end user documentation requires a completely different approach and skill set than writing code. This is especially true for things like tutorials as opposed to reference documentation.

## Phase Five: The Marketer

Build a better mousetrap and the world will ignore you, tell you that their mouse trap situation is perfectly fine thankyouverymuch and why don't you get a real job rather than wasting your time on this whateveritis, as it will never work. If you want to make them change their mind, you need marketing. Lots of it.

There are many different ways of making your project more known: writing blog posts, presenting at conferences, general online advocacy and so on. This requires, again, a new set of skills, such as talking to a large group of people in public. This is especially true for programmers who are mostly introverted, but sadly the meek don't inherit the earth. It tends to go to those who can make the most noise about their solution.

# Stage Two: The Project Is Mostly for Other People

As the project becomes bigger and more used, eventually another tipping point is reached. Here the program is no longer catering to the needs of the original creator but to the community at large. The rate of change reduces dramatically. Breaking changes can no longer be made at a quick pace or possibly at all. It is also possible that the landscape has changed and the project is now being used in a different way or for different ends than was originally planned. All of this means that the project runner needs to spend more and more time solving issues that does not directly benefit themselves. This may cause friction if, for example, the project leader works for a company that has other priorities and does not want the person to spend time on things that don't benefit them directly.

## Phase Six: The Recruiter

A project that does not keep refreshing and growing its developer base is a dead one. Typically a project needs to have a sizable chunk of users before other people start contributing to it in a major way. Sometimes people become involved voluntarily, but it's even better if you can somehow actively encourage them to contribute. That is only part of the story, though, since they need to be trained and taught the processes and so on. Paradoxically getting new contributors slows down development at first, but eventually makes things faster as the workload can be split among multiple people.

## Phase Seven: The Culture Cultivator

Every project has its own set of unspoken guidelines. These get established quite early on and include things like requiring tests for every new feature, not using coding patterns X, Y or Z but use H, J and K instead and so on. People are generally quite good at detecting these and doing the same thing as everyone else. As the pool of contributors grows, this becomes less and less common. Contributions tend to become more lax. This is not due to malice, but simply because people are not aware of the requirements.

It is very easy to slip on these requirements little by little. It is the job of the project leader to make sure this does not happen. This requires both leading by example and also by noting out these issues in code review and other discussions. 

## Phase Eight: The Overseer

This phase begins when the project maintainer realizes that they are no longer the person who knows most about the code base. Other people have done most of the coding work for so long that they are the actual experts on it. This causes yet another change in the type of work one needs to do. Up until now the work has been about solving problems and making decisions on things you are intimately familiar with. As an overseer you need to make decisions on things you don't really know about. Earlier decisions were based on code and implementation details, but now decisions are based mostly on what other people say in their merge requests and design discussions.

This is something nobody really prepares you for. Making big decisions based on imperfect information can be really difficult for someone who has gotten used to going through every detail. Once a project gets over a certain size this is just not possible as the human brain is incapable of holding that many details in active memory at the same time. Even if it could, having a single person review everything would be a huge bottleneck. It is (more than) a full time job, and getting someone to pay for a full time maintainer review job is very rare.

Finally, even if this were possible, reviewing is a very tiring job that very few people can keep on doing as their only task for very long. Eventually the mind will start screaming for something else, even for a while. Finally even if someone could do that, contributors would eventually get very annoyed by getting micromanaged to death and just leave.

## Phase Nine: The Emeritus

All good things eventually come to an end and so will open source project maintainership. Eventually the project will either become irrelevant or the torch will be passed to someone else. This is, in a way, the greatest thing a project maintainer could hope for: being able to create a new entity that will keep on being used even after you have stopped working on it.

Open source maintainership is a relatively young field and most projects at the end of their life cycle either become unmaintained zombies or get replaced by a new project written from scratch. Ee don't have that much experience on what emerituses do. Based on other fields these may range from "nothing" to doing conference talks, advising current maintainers on thorny issues.

原文链接：[https://nibblestew.blogspot.com/2020/11/the-nine-phases-of-open-source-project.html](https://nibblestew.blogspot.com/2020/11/the-nine-phases-of-open-source-project.html)
