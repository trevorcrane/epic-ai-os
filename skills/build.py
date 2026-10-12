import json, html, datetime
W="/home/box/agent-data/workflows"
T="/workspace/assets/teaching-frameworks/tom-bilyeu-ai-team-pack/handoffs"
M="/workspace/mentor-machine"
S=[]
def add(**k): S.append(k)
# ---------- Strategy & planning
add(id="master-plan",name="Master Plan",category="Strategy & planning",
 what="Turns a rough project or idea into a short, clear plan card with what done looks like, a grade, and a ship-or-improve decision.",
 bots=["Planner","Advisor","Navigator","Epic OS (First Mate)"],status="Live",share="Yes",
 path=f"{W}/master-plan/SKILL.md",trigger='Say "master plan re: ..."',notes="Our own method. Uses the Score skill for the grade.")
add(id="pressure-test-before-go",name="Pressure Test Before Go",category="Strategy & planning",
 what="Scores a big new tool, system, or workflow on 7 checks before anyone says go, and only allows a small pilot if the key scores are under 80.",
 bots=["Advisor","Navigator","Epic OS (First Mate)","Reviewer"],status="Live",share="Yes",
 path=f"{W}/pressure-test-before-go/SKILL.md",trigger="Runs automatically before any go, install, or build decision",notes="Our own method.")
add(id="demand-test-design",name="Demand Test Design",category="Strategy & planning",
 what="Picks the one smallest test (free download, booked call, or pre-sale) that proves people want an offer before it gets built, with a win number and a quit number set up front.",
 bots=["Advisor"],status="Draft",share="No",
 path=f"{T}/strategist-demand-test.md",trigger='"How do I test this?" or after Idea Validation says GO',notes="Not installed. Shaped after the Tom Bilyeu pack (personal use only), so not for clients as is.")
add(id="growth-plan",name="90-Day Growth Plan",category="Strategy & planning",
 what="Builds a 90-day plan to get a live offer in front of the right people and turn them into conversations and customers, with every task given to a named bot.",
 bots=["Campaign Ops","Content Engine","GTM Prospecting","GTM Loop Closer","Call Follow-Ups","Sales Call Coach","Scorekeeper"],status="Draft",share="No",
 path=f"{T}/marketer-campaign-ops.md",trigger='"How do I get leads?" once a page is live',notes="Not installed. Tom-derived. Campaign Ops owns it and hands pieces to the others.")
# ---------- Research
add(id="idea-validation",name="Idea Validation",category="Research",
 what="Proves or kills a business idea using real customer words and proof that people already pay for this, ending in GO, SHARPEN, or KILL.",
 bots=["Researcher"],status="Draft",share="No",
 path=f"{T}/researcher-idea-validation.md",trigger='"Is this idea any good?" or "validate this"',notes="Not installed. Tom-derived. First step of the launch chain.")
# ---------- Copy & content
add(id="launch-copy",name="Launch Copy",category="Copy & content",
 what="Writes every word a launch needs (hook, page, free download, follow-up emails, posts, DMs) in the client's own voice using only real proof.",
 bots=["Cat (Book: Dr. Leigh)","Content Engine","Writing Bot"],status="Draft",share="No",
 path=f"{T}/copywriter-cat.md",trigger="After a Demand Test is picked, or any ask for a hook, page, or emails",notes="Not installed. Tom-derived. Planned for Cat as she moves into Trevor's copywriter seat.")
add(id="landing-page-build",name="Landing Page Build",category="Copy & content",
 what="Turns approved launch copy into one live web page with one button and a working signup form, then hands a checklist to the Reviewer before it goes public.",
 bots=["Builder","Bot Studio","Reviewer"],status="Draft",share="No",
 path=f"{T}/builder-landing-page.md",trigger='"Publish a page" once copy is approved',notes="Not installed. Tom-derived. Bot Studio Builder for client builds.")
# ---------- Mentors/coaching
for sid,nm,who,pct,pack in [("hormozi-advisor","Hormozi Mentor","Alex Hormozi","50%","hormozi"),
                            ("kallaway-advisor","Kallaway Mentor","Kallaway","57%","kallaway"),
                            ("ed-lawrence-advisor","Ed Lawrence Mentor","Ed Lawrence","56%","ed-lawrence")]:
    topic={"hormozi":"offers, leads, free value, and growth","kallaway":"YouTube, short videos, packaging, bios, and calls to action","ed-lawrence":"business YouTube: simple style, intros, stories that turn viewers into buyers, and views versus sales"}[pack]
    add(id=sid,name=nm,category="Mentors/coaching",
     what=f"Coaches Trevor on {topic} in a {who}-style voice, using only saved quotes and videos, never pretending to be {who}.",
     bots=["Mentor agents","Podcast" if False else "Mentor agents"][:1]+([f"YT Mentor: Hormozi"] if pack=="hormozi" else []),
     status="Live",share="No",path=f"{W}/{sid}/SKILL.md",trigger=f'Ask for "{who}" advice',
     notes=f"Installed, but the pack scored {pct} with Reviewer, so it is held from being promoted as a finished coach. Copy also lives at {M}/skills/{sid}/SKILL.md."+(" The two copies are identical." if pack=="hormozi" else " The two copies differ slightly (need to pick one)."))
for sid,nm,who,pct in [("dan-martell-pack","Dan Martell Mentor (stub)","Dan Martell","48%"),("gary-vee-pack","Gary Vee Mentor (stub)","Gary Vee","48%"),("mrbeast-pack","MrBeast Mentor (stub)","MrBeast","42%")]:
    folder=sid.replace("-pack","")
    add(id=sid,name=nm,category="Mentors/coaching",
     what=f"Starter rules for a future {who}-style coach; the videos and quotes are gathered but it is not a working skill yet.",
     bots=["Mentor agents"],status="Parked",share="No",path=f"{M}/packs/{folder}/persona/SYSTEM.md",trigger="Not usable yet",
     notes=f"Reviewer score {pct}. No installed skill and no mentor agent assigned yet.")
add(id="mrbeast-perspective",name="MrBeast Perspective (outside download)",category="Mentors/coaching",
 what="A free skill someone else published online (written in Chinese) that role-plays MrBeast to give YouTube title, thumbnail, and hook advice.",
 bots=[],status="Parked",share="No",path=f"{M}/refs/mrbeast-github/alchaincyf-mrbeast-skill/SKILL.md",trigger="Reference only",
 notes="Third-party. Our MrBeast pack treats it as a guess to check, not a source. No owner bot.")
# ---------- Ops & quality
add(id="score",name="Score",category="Ops & quality",
 what="Grades any piece of work with a letter and a percent, names the 2 to 4 gaps, and asks whether to ship it or improve it.",
 bots=["Reviewer","Epic OS (First Mate)","Planner","All bots"],status="Live",share="Yes",
 path=f"{W}/score/SKILL.md",trigger='Say "score this" or "grade this"',notes="Our own method.")
add(id="first-mate-os",name="First Mate Operating System",category="Ops & quality",
 what="The rulebook for how First Mate takes a request, puts it on a Linear card with an owner and a checker, and only calls it done when there is proof.",
 bots=["Epic OS (First Mate)","Implementer","Builder","Reviewer"],status="Live",share="Maybe",
 path=f"{W}/first-mate-os/SKILL.md",trigger='"Get this done" to First Mate',notes="Our own method, but tied to Trevor's Linear setup and Grok Bot; would need trimming for a client.")
add(id="epic-skill-card",name="Epic Skill Card Template",category="Ops & quality",
 what="The blank pattern every new skill should follow: one job, what it needs first, hard rules, steps with checks, a self-score, and a handoff note.",
 bots=["Bot Studio","Epic Brain"],status="Draft",share="No",
 path=f"{T}/00-epic-skill-card-template.md",trigger="Used when writing a new skill",notes="Not installed. Structure inspired by the Tom pack, rewritten in our words; Maybe for clients after Tom says OK.")
add(id="tango-work-loop",name="Tango Work Loop (outside tool)",category="Ops & quality",
 what="Instructions from the Tango tool for how bots claim a task, show their work, attach proof, and hand off to the next bot or person.",
 bots=["Epic OS (First Mate)","Implementer"],status="Parked",share="Maybe",
 path="/workspace/tango-pilot/src/skill.md",trigger="Only if the Tango pilot goes ahead",
 notes="Written by Tango (a vendor), saved during a pilot. Not installed. No bot formally owns it.")
# ---------- Client-specific
add(id="dr-leigh-voice",name="Dr. Leigh Richardson Voice",category="Client-specific",
 what="Makes anything written in Dr. Leigh's name (book chapters, emails, posts, bios) sound warm, plain, and hopeful like her, with every science fact sourced.",
 bots=["Cat (Book: Dr. Leigh)","Writing Bot","Content Engine"],status="Live",share="No",
 path=f"{W}/dr-leigh-richardson-voice/SKILL.md",trigger="Any writing in Dr. Leigh's voice",
 notes="Short installed version. Full version: /workspace/leigh-book/LEIGH-VOICE-SKILL.md (Word copy in /workspace/leigh-docx/). Still partial: blogs and LinkedIn not added yet.")
add(id="depleted-brain-ghostwriting",name="Depleted Brain Ghostwriting Playbook",category="Client-specific",
 what="The playbook for drafting Dr. Leigh's book The Depleted Brain: table of contents patterns, launch deadlines, and rules against made-up facts.",
 bots=["Cat (Book: Dr. Leigh)","Writing Bot"],status="Live",share="No",
 path="/workspace/leigh-book/research/COPY-SKILLS.md",trigger="Book drafting sessions",
 notes="A reference file the Book agent reads, not an installed skill.")
for s in S:
    s["bots"]=list(dict.fromkeys(s["bots"]))
cats=["Strategy & planning","Research","Copy & content","Mentors/coaching","Ops & quality","Client-specific"]
S.sort(key=lambda s:(cats.index(s["category"]),["Live","Draft","Parked"].index(s["status"]),s["name"]))
for i,s in enumerate(S,1): s["num"]=i

planned=[("intake-brain","Fill in a new person's Brain files"),("first-job","Five questions that turn a new Brain into one finished job"),
 ("follow-up-draft","Draft follow-ups in the Brain's voice from a list of names"),("call-to-content","Turn one call recording into a post, clip list, and newsletter section"),
 ("log-job","Write the Scorekeeper row for a finished job"),("1-3-1","Turn a messy ask into a one problem, three options, one pick decision brief")]
third_party={"count_files":54,"unique":30,"locations":[f"{M}/packs/hormozi/corpus/from-github/",f"{M}/refs/hormozi-github/"],
 "note":"Free Hormozi-style skills other people published online. Saved as reference, blocked from auto-loading into answers. 24 of them exist twice (once in each folder). Status Parked, Share No, no owner bot."}
builtin="Cursor/Grok built-in skills (managed-skills, plugin-skills, plugins/compound-engineering): built-in, not ours."
counts={k:sum(1 for s in S if s["status"]==k) for k in ["Live","Draft","Parked"]}
data={"title":"Epic OS Skill Library","owner":"Trevor Crane","generated":datetime.date.today().isoformat(),
 "counts":counts,"categories":cats,"skills":S,"planned_not_written":[{"id":a,"what":b,"source":"/workspace/epic-brain/source/EPIC-OS-HANDOFF-2026-09-27/repo/team/SKILLS.md"} for a,b in planned],
 "third_party_reference":third_party,"builtin_appendix":builtin,"favorite_field":"Add \"favorite\": true to any skill to mark it for sharing later."}
for s in S: s["favorite"]=False
json.dump(data,open("/workspace/skill-library/skills.json","w"),indent=2,ensure_ascii=False)

howto=["Skim the cards below. Each one says what the skill does, which bot uses it, and whether it is ready.",
 'To hand a skill to a bot, say "give skill [name] to bot [name]" (example: "give Score to Content Engine").',
 'To approve a draft, say "install [skill name]". Drafts are written but not turned on yet.',
 'Mark favorites to share with clients later: say "favorite [skill name]" and it gets a star here and in skills.json.',
 "Share column: Yes means ours and safe to give clients, Maybe means needs trimming first, No means Tom-derived, third-party, or client-private."]
odd=["Two naming schemes for the same launch skills: the Epic OS plan (team/SKILLS.md) calls them pain-research, offer-test, launch-copy, one-page-site, gtm-plan, while the drafts are idea-validation, demand-test-design, launch-copy, landing-page-build, growth-plan. Pick one set before installing.",
 "Mentor skills live in two places (installed copy and a copy in mentor-machine/skills). Hormozi copies match; Kallaway and Ed Lawrence copies differ slightly.",
 "Dr. Leigh voice exists as a short installed skill, a long Markdown version, and a Word copy.",
 "No owner bot: MrBeast Perspective (outside download), the 30 outside Hormozi skills, and Tango Work Loop (only a pilot).",
 "Mentor skills are installed but held: none has passed Reviewer yet (scores 50% to 57%).",
 "All 5 launch drafts are Tom-derived and marked personal use only, so they are No for clients until rewritten or Tom agrees."]
# ---------- Markdown
L=[f"# Epic OS Skill Library","",f"Owner: Trevor Crane. Updated {data['generated']}. {len(S)} skills: {counts['Live']} Live, {counts['Draft']} Draft, {counts['Parked']} Parked.","","## How to use this",""]
L+= [f"{i}. {t}" for i,t in enumerate(howto,1)]+["","Status key: Live = installed and in use. Draft = written, not installed. Parked = saved for later or reference only.",""]
for c in cats:
    L+=[f"## {c}","","| # | Skill | What it does | Bot(s) | Status | Share with clients? | File |","|---|---|---|---|---|---|---|"]
    for s in [x for x in S if x["category"]==c]:
        L.append(f"| {s['num']} | **{s['name']}** | {s['what']} | {', '.join(s['bots']) or 'None yet'} | {s['status']} | {s['share']} | `{s['path']}` |")
    L.append("")
    for s in [x for x in S if x["category"]==c]:
        L.append(f"{s['num']}. {s['name']}: {s['notes']} How to start it: {s['trigger']}.")
    L.append("")
L+=["## On the list, not written yet","","From the Epic OS plan. Skills get written after a job repeats three times.",""]
L+=[f"{i}. {a}: {b}." for i,(a,b) in enumerate(planned,1)]
L+=["","## Outside reference skills (Parked)","",f"1. {third_party['count_files']} files, {third_party['unique']} unique skills. {third_party['note']}",f"2. Locations: `{third_party['locations'][0]}` and `{third_party['locations'][1]}`","",
 "## Things to know","",]+[f"{i}. {t}" for i,t in enumerate(odd,1)]+["","## Appendix","",f"1. {builtin}",
 "2. Related instruction files that are not skills (bot start-up rules, drafts): /workspace/epic-brain/source/EPIC-OS-HANDOFF-2026-09-27/repo/AGENTS.md and CLAUDE.md, /workspace/epic-brain/trevor/team/ (seat and handoff rules).",""]
md="\n".join(L)
open("/workspace/skill-library/SKILL-LIBRARY.md","w").write(md)
# ---------- HTML
e=html.escape
badge={"Live":"#1f8f4e","Draft":"#b7791f","Parked":"#6b7280"}
sh={"Yes":"#1f8f4e","Maybe":"#b7791f","No":"#b91c1c"}
H=[f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Epic OS Skill Library</title><style>
body{{font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:0;background:#f5f6f8;color:#1a1d23;line-height:1.5}}
.wrap{{max-width:1000px;margin:0 auto;padding:20px 16px 60px}}
h1{{margin:0 0 4px;font-size:1.7rem}} h2{{margin:32px 0 12px;font-size:1.25rem;border-bottom:2px solid #dde1e7;padding-bottom:6px}}
.sub{{color:#555}} .box{{background:#fff;border-radius:12px;padding:14px 18px;box-shadow:0 1px 3px rgba(0,0,0,.08)}}
.stats{{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0}} .stat{{flex:1;min-width:90px;background:#fff;border-radius:10px;padding:10px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,.08)}}
.stat b{{display:block;font-size:1.6rem}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:12px}}
.card{{background:#fff;border-radius:12px;padding:14px 16px;box-shadow:0 1px 3px rgba(0,0,0,.08);display:flex;flex-direction:column;gap:6px}}
.card h3{{margin:0;font-size:1.05rem}} .pill{{display:inline-block;color:#fff;border-radius:999px;padding:1px 10px;font-size:.78rem;font-weight:600;margin-right:4px}}
.bots{{font-size:.9rem}} .path{{font-family:ui-monospace,Menlo,monospace;font-size:.72rem;color:#666;word-break:break-all}}
.note{{font-size:.85rem;color:#444}} ol{{padding-left:22px}} li{{margin:4px 0}}
</style></head><body><div class="wrap">
<h1>Epic OS Skill Library</h1><div class="sub">Trevor Crane. Updated {data['generated']}. Every skill the bots use, in plain language.</div>
<div class="stats"><div class="stat"><b>{len(S)}</b>skills</div>"""]
for k in ["Live","Draft","Parked"]: H.append(f'<div class="stat"><b style="color:{badge[k]}">{counts[k]}</b>{k}</div>')
H.append('</div><h2>How to use this</h2><div class="box"><ol>'+"".join(f"<li>{e(t)}</li>" for t in howto)+'</ol><p class="note">Live = installed and in use. Draft = written, not installed. Parked = saved for later or reference only.</p></div>')
for c in cats:
    H.append(f"<h2>{e(c)}</h2><div class='grid'>")
    for s in [x for x in S if x["category"]==c]:
        H.append(f"""<div class="card"><h3>{s['num']}. {e(s['name'])}</h3>
<div><span class="pill" style="background:{badge[s['status']]}">{s['status']}</span><span class="pill" style="background:{sh[s['share']]}">Share: {s['share']}</span></div>
<div>{e(s['what'])}</div><div class="bots"><b>Bot(s):</b> {e(', '.join(s['bots']) or 'None yet')}</div>
<div class="note"><b>Start it:</b> {e(s['trigger'])}</div><div class="note">{e(s['notes'])}</div><div class="path">{e(s['path'])}</div></div>""")
    H.append("</div>")
H.append("<h2>On the list, not written yet</h2><div class='box'><ol>"+"".join(f"<li><b>{e(a)}</b>: {e(b)}.</li>" for a,b in planned)+"</ol></div>")
H.append(f"<h2>Outside reference skills (Parked)</h2><div class='box'><ol><li>{third_party['count_files']} files, {third_party['unique']} unique skills. {e(third_party['note'])}</li><li class='path'>{e(third_party['locations'][0])}<br>{e(third_party['locations'][1])}</li></ol></div>")
H.append("<h2>Things to know</h2><div class='box'><ol>"+"".join(f"<li>{e(t)}</li>" for t in odd)+"</ol></div>")
H.append(f"<h2>Appendix</h2><div class='box'><ol><li>{e(builtin)}</li><li>Related instruction files that are not skills: Epic OS AGENTS.md and CLAUDE.md drafts, and the seat and handoff rules in /workspace/epic-brain/trevor/team/.</li></ol></div></div></body></html>")
open("/workspace/skill-library/SKILL-LIBRARY.html","w").write("\n".join(H))
print(counts,len(S))
for s in S: print(s['num'],s['name'],'|',', '.join(s['bots']),'|',s['status'],'|',s['share'])
