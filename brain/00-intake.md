# 00-INTAKE.md · Smart Start

Status: DRAFT (submitted for the Captain's review). Rebuilt 2026-09-27 from research on what proven intakes ask (StoryBrand, Hormozi, Priestley, Schwartz, Halbert, agency voice questionnaires) and how long people will answer (SurveyMonkey, Survicate, ScoreApp). Full report: `v1-EpicOS-SmartStartResearch-2026-09-27.md`.

The Smart Start is how a Brain gets turned on. Ten questions. About five minutes if your AI drafts first, ten to fifteen if you talk it. The output is the ten numbered files in this folder.

## Why ten
Every proven framework is under 30 items; the tightest are 4 to 7. Drop-off climbs fastest with each added question up to 15 and completion falls past 7 or 8 minutes. Ten is the bottom of the proven range, and each of the ten Brain files gets one real answer instead of a guess. [VERIFIED: SurveyMonkey and Survicate studies in the research report]

## Four ways to answer (lead with the first)
1. **Ask your AI.** Paste the prompt below into the AI that already knows you (ChatGPT, Claude, whatever you use). It drafts. You correct. Fastest.
2. **Talk it.** An AI interviews you one question at a time. Best voice capture. Slowest.
3. **Write it.** One screen per question. Skip anything. Short answers are fine.
4. **Feed it.** Upload what you already have (bio, site, posts, a book). Always on. Never the only door; it is the on-ramp to Pro.

## The Smart 10
| # | Question | Feeds |
|---|---|---|
| 1 | Who are you and what do you do? Name, business, website, and the one-line story of how you got here. | 01-identity |
| 2 | Who is your best customer, and what do they want most? Describe one real person if you can. | 04-audience |
| 3 | What problem keeps them stuck, in their own words? What have they already tried? | 03-messaging, 04-audience |
| 4 | What do you sell, what does it cost, and what do they get? Your main offer and the result it promises. | 05-offers |
| 5 | Why you? What is different about how you do it? Your method, your story, or the thing clients love. | 03-messaging, 01-identity |
| 6 | What results can you prove? Numbers, stories, testimonials, links. "Just starting" is a fine answer. | 10-proof |
| 7 | What do you want in the next 90 days, and what do you want off your plate? | 06-goals |
| 8 | How do you sound? Paste one thing you wrote or link one video, then give 3 words you are and 3 words you are not. | 02-voice |
| 9 | What should AI never do or say for you? Values, hard lines, things that would embarrass you. | 07-rules |
| 10 | Show me your taste. Your colors or logo if you have them, plus 2 or 3 people or brands you admire and why. | 08-design, 09-mentors |

Rules for every question: one screen, skipping allowed, short answers accepted, a best guess is fine. Anything thin becomes a Gap line in the file, not a second follow-up.

## Mode 1: the "Ask your AI" prompt (paste this)
```
You know me from our past chats and files. Draft answers to these 10 questions from what you know. Do not interview me. I will fix the draft.

Rules:
- One short paragraph each. Plain words. My voice, not corporate.
- Start any guessed sentence with [GUESS].
- If you know nothing, write "Not known."
- Never invent prices, results, testimonials, names or credentials.

1. Who am I and what do I do? Name, business, website, one-line story.
2. Who is my best customer and what do they want most?
3. What problem keeps them stuck, in their words? What have they tried?
4. What do I sell, what does it cost, what do they get?
5. Why me? What is different about how I do it?
6. What results can I prove?
7. What do I want in the next 90 days, and off my plate?
8. How do I sound? 3 words I am, 3 words I am not.
9. What should AI never do or say for me?
10. My taste: colors, style, 2 or 3 people or brands I admire and why.

End with a list of every [GUESS] so I can fix them fast.
```
Fix the guesses. Then hand the corrected answers to mode 2 or 3, or straight to the file builder below.

## Mode 2: the "Talk it" prompt (paste this into any AI)
```
Interview me one question at a time using the Smart 10 from Epic OS brain/00-INTAKE.md. Start with question 1 and wait. Friendly, simple language. Accept short or messy answers. Let me skip anything. One brief follow-up only when an essential detail is unclear, then move on. Never invent facts, prices, results, testimonials, credentials, or preferences. Mark unknown information "Not provided." Separate goals from results.

Before finishing, show me a concise draft of all ten answers and ask what I want to correct. After I approve, write ten Markdown files named 01-identity.md, 02-voice.md, 03-messaging.md, 04-audience.md, 05-offers.md, 06-goals.md, 07-rules.md, 08-design.md, 09-mentors.md, 10-proof.md. Each starts with "Status: DRAFT" and ends with a "Gaps" section. No word cap; detail beats a summary. This is intake material, not a finished Brain. Do not send anything automatically.
```

## After the files land
The AI gives you ten blocks of text. Save each as its own file in this `brain/` folder, named exactly as listed. Read them. Correct, do not edit: fix what is wrong, leave the rest. Change `Status: DRAFT` to `Status: APPROVED` on each file you have read. The Brain is usable at DRAFT. It is trusted at APPROVED.

## Make it Pro (data, not questions)
Hand over real artifacts; the AI rebuilds the ten files from them with the Smart answers as the skeleton.
| Ask | Amount | Rebuilds |
|---|---|---|
| Writing you wrote yourself | 10 pieces, 600 to 1,500 words, long and short, 2 or 3 topics, last 12 months | 02-voice |
| Talk transcripts | 3: one sales call, one interview or podcast, one teaching moment | 02-voice, 03-messaging, 05-offers |
| Books or long-form | every book, manuscript, course outline | 01-identity, 03-messaging, 09-mentors |
| Best-performing content | top 10 posts or emails by response, plus 3 that flopped | 02-voice, 03-messaging |
| Customer voice | 10 customer emails, testimonials, or DMs in their words | 04-audience, 10-proof |
| Offer pages | every live offer page, price sheet, guarantee | 05-offers |
| Design assets | logo, colors, fonts, 3 designs you love and 3 you hate | 08-design |
| Taste list | 5 creators you copy, 5 you never would, one line why | 09-mentors, 07-rules |
| Proof file | every number, screenshot, case study, press mention, with a link | 10-proof |
Sample counts are vendor guidance, not science: 5 to 10 self-written pieces, 50 to 100 examples before a model reliably has your pattern, and most clone data is audio or video. [BELIEVED 75%: The Stacc, Like One, OpenAI fine-tuning docs, Delphi]
Test that Pro landed: fresh output scores 85 or better on a 10-point voice card.

## Make it Epic (100 real inputs)
One input = one real artifact or one real correction that touched a Brain file, with a date, a source, the file, and the change. A question answer is not an input. A guess is not an input.
Targets: 30 calls · 30 pieces of content with results · 20 corrections · 10 customer words · 10 decisions.
Logged one line each in `memory/INPUTS.md`: `2026-09-27 | call | Fathom link | 05-offers | added the 3-step plan Trevor uses on sales calls`. The Scorekeeper counts the lines; the count is the Epic number.
Every input does one of three things to a file: confirm, correct (old line goes to CORRECTIONS), or add. Each Brain file carries "Backed by N inputs" and a ladder: DRAFT (Smart) > APPROVED (the Captain read it) > PROVEN (20+ inputs, zero corrections in 30 days). Epic is all ten files PROVEN.
