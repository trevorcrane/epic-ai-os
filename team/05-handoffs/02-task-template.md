# Task template (the TARGET)

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: repo/team/LOOP.md step 2

Tango's own fields where they exist. Authority, Evidence required, and Staffing go in Tango's `constraints` field as three labeled lines. [BELIEVED 80%: check create_task before relying on a flag.]
```
Client: <the Brain this is for>          Project: <an open project; list_projects first. Start with one. Split at ten tasks.>
Title: the result, not the activity ("12 follow-up drafts ready for Dana", not "follow-up outreach")
Goal: one sentence
Definition of done: 3 to 5 checks, each "do X, see Y", each tagged TERMINAL (Builder / Reviewer run it), BROWSER (Reviewer on the live thing), or HUMAN (the Captain's 2-minute check). Anything a person outside the team will see has at least one BROWSER or HUMAN check.
Assignee: @<the Lead's handle>
Estimate: minutes. Over 240 means it is two tasks.      Deadline: date and hour
Authority (in constraints): the flags send, publish, merge, deploy, spend with a cap, contact_client. Green: none on. Yellow: the one flag the approver said yes to, with the link to that yes in the note. Red: none on, approver set.
Sources: links to read first
Evidence required: URL | file | screenshot | record ID | test contact. Deliverable files named v1-What-It-Is-2026-09-25.ext (version first, date last, never final).
Staffing: which seats, and why (a green one-liner is Lead plus Builder; anything that ships gets a Reviewer)
```
Missing a field? Fill it from what you know, note the assumption in one line, go. A task is never something the Captain fills in.
