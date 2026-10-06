# How a job moves

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: repo/team/LOOP.md, rules/CURSOR-BOB-DISPATCH.md

Captain asks > First Mate makes the Tango task > Lead staffs it > Researcher (if the current state is unknown) > Builder > Reviewer (if it ships) > Scorekeeper > First Mate reports in the thread the ask came from.

## The loop (every job, one pass or standing)
Five words, modeled on Eric Siu's loop: TARGET > OBSERVE > GAP > ACT AND TRACE > LEARN, STOP, OR ESCALATE. The steps below are those five words with names. Then back to OBSERVE until the target holds or the Captain says stop.
"@Captain" below means the handle on the Captain card in `team/02-people/01-captain.md`.

## 1. Ask
In Slack or in chat. Messy is fine. Voice-to-text is fine. The First Mate interprets charitably and never makes the Captain repeat himself.

## 2. Task, the TARGET
The First Mate makes it in Tango; the Captain never does. Fields: `team/05-handoffs/02-task-template.md`.

## 3. Observe, then build (OBSERVE, GAP, ACT AND TRACE)
Researcher if the current state is unknown. Write the gap in one line on the task. No gap? Complete the task and say so; that is a finished job too. Then `team/04-seats/04-builder.md`: the smallest change that closes the gap, exact command, exact output, on a branch, as a pull request (code in a GitHub repo: Bob opens it and never merges). Over 60 minutes of work gets a five-line plan on the task first (goal, approach, steps, risks, done looks like); the Reviewer replies PLAN OK or PLAN FAIL before building.

## 4. Review
`team/04-seats/05-reviewer.md`. PASS, FAIL, or BLOCKED. FAIL: fix only what failed, back to step 3. Two FAILs, then the third verdict is BLOCKED with a 1-3-1 (LAWS 7). A red act stops here and escalates (LAWS 8).

## 5. Scorekeeper row
One row in the Scorecard format, one source, after PASS only. The Scorecard file is not in the repo yet.

## 6. Report
If a correction or a decision landed, write the memory line first (`AGENTS.md`, Memory). Then report in the format in `team/04-seats/01-first-mate.md`, in the thread the ask came from.
Green: the Lead calls complete_task with the receipt (summary, evidence artifacts, open questions). Tango parks it in review. That is green done; nobody taps anything. Len sweeps review once a week and accepts in a batch.
Yellow and red: end with "Reply done or say what's off." On "done": a human merges the pull request if it is code (Bob never merges; `rules/CURSOR-BOB-DISPATCH.md`), accept the task, archive.

## Words for state
- A task's state is whatever Tango shows. Its end states are done, review, blocked, cancelled. Do not invent columns.
- A review verdict is PASS, FAIL, or BLOCKED.
- An agent's strongest claim is PASSED REVIEW. The human says done (green: LAWS 5).
- The state of a thing (a fix, a site, an automation) is one of four words only: PERMANENT · IN PROGRESS · WORKS NOW NOT PERMANENT · BLOCKED.
- A draft is not a send. A build is not a launch. A report is not money moved. Every report says which one happened.

## Irreversible acts need a PASS
Send, publish, charge, delete, DM a human outside the team: only on a task whose review is PASS and whose Authority flag is on. Otherwise draft it and request review.

## Stop button
The Captain says "stop" in Slack or on the task. Every running task blocks with reason "STOP: Captain". Nothing resumes until the Captain says go.
