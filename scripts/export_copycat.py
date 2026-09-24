#!/usr/bin/env python3
"""Create a generic, client-safe Copycat skill package from an explicit allowlist."""
from pathlib import Path
import zipfile, hashlib, json, argparse
root=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
paths=['operating-system/CAT_COPYWRITING_AGENT_BRIEF.md','operating-system/TEAM-ROSTER.md','operating-system/MEMORY-SYNC.md','operating-system/tools/OJOY.md','operating-system/adapters/CROSS-PLATFORM.md','operating-system/agents/cat/MEMORY.md','operating-system/agents/cat/LOAD.md']
paths += [str(p.relative_to(root)) for p in (root/'operating-system/skills/copycat').rglob('*') if p.is_file()]
# Generic exports keep the functional framework but remove private repo references,
# deployment rows, named staff/clients and campaign-specific references.
files={}
for path in paths:
 text=(root/path).read_text()
 if path.endswith('agents/cat/MEMORY.md'):
  text='# Cat / Copycat memory\n\nCat and Copycat are the same copywriting agent. Your coordinator is a separate role. Add only this owner’s sourced preferences, corrections and measured results. Keep client facts scoped. Load the role brief, copycat skill, communication standard and assigned brand profile at startup. Record version and actual worker ID.\n'
 elif path.endswith('agents/cat/LOAD.md'):
  text='# Load Cat\n\nRead operating-system/CAT_COPYWRITING_AGENT_BRIEF.md, agents/cat/MEMORY.md (under operating-system), EPIC_AI_COMMUNICATION_STANDARD.md (under operating-system), operating-system/skills/copycat/SKILL.md and its references. Add your own brand profile. Record exact package version, loaded paths, worker ID and available tools. A separate reviewer validates substantial work; disclose when unavailable. A repository link is not proof of loading. Test identity separation, four Cs, primary CTA, optional Ojoy and memory update rules.\n'
 elif path.endswith('TEAM-ROSTER.md'):
  text='# Team roles\n\nOwner sets intent. PM coordinates. Cat/Copycat owns copy. Researcher supplies evidence. Builder implements. Independent reviewer validates. Scorekeeper records measured outcomes. Ojoy is optional and access must be verified.\n'
 elif path.endswith('CROSS-PLATFORM.md'):
  text='# Install portable Copycat\n\nLoad operating-system/CAT_COPYWRITING_AGENT_BRIEF.md and operating-system/skills/copycat/SKILL.md into your host’s supported agent instructions or project knowledge. Add only your own approved brand profile. Register the skill when supported. Confirm loaded version and tools. No account credentials are included.\n'
 else:
  text=text.replace('https://github.com/trevorcrane/epic-ai-os','[your private canonical repository]')
  text='\n'.join(line for line in text.splitlines() if not any(term in line for term in ['Alfred is Trevor','Historical Robyn campaign context:','Claude','adapters/ADOPTION.md','Alfred / Al / First Mate / Number One','brand/trevor/VOICE.md']))+'\n'
 text=text.replace('Trevor’s','the owner’s').replace('Trevor', 'the owner').replace('Robyn, Leigh and each client’s', 'each client’s').replace('Robyn’s', 'another client’s').replace('Leigh’s', 'another client’s').replace('Leigh example', 'book-waitlist example')
 files[path]=text
files['operating-system/EPIC_AI_COMMUNICATION_STANDARD.md']="# Four C communication standard\n\nSanitized adaptation of the owner-supplied v5 framework. It preserves the core distinction between the four practices and their intended outcomes.\n\nConnect: address the person appropriately and refer to specific true context. Intended outcome: seen.\nCare: acknowledge expressed emotion or intent without invented feelings or canned empathy. Intended outcome: heard.\nClarity: state purpose plainly and ask a concise question to confirm an uncertain interpretation. Intended outcome: understood.\nCall to Action: one clear next step, verified resource or owned follow-through. Intended outcome: confident.\n\nUse natural language, not four labeled paragraphs. One primary action can have repeated links. Avoid corporate filler, em dashes, false certainty, fake familiarity, shaming and invented deadlines. Check times/timezones. Keep brand voice, facts and permissions separate. Close the loop in the originating conversation.\n\nApplication note: verified logistics and automated confirmations need clear facts, not invented uncertainty or an unnecessary reply. This is an adaptation, not a redefinition of the source's question-based Clarity rule. A response-time target is not a promise of monitoring when offline. Two to five writing rounds are calibration guidance, not a reason for empty revisions. Owner approval and publishing authority remain separate from editorial scores. No unresolved placeholders in send-ready copy.\n"
files['START-HERE.md']='# Copycat portable kit\n\nRead operating-system/adapters/CROSS-PLATFORM.md. This contains generic instructions, not client facts or credentials. Add your own brand profile.\n'
manifest={p:hashlib.sha256(t.encode()).hexdigest() for p,t in sorted(files.items())}
files['manifest.json']=json.dumps({'version':'1.1.0','sha256':manifest},indent=2)+'\n'
out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p,t in sorted(files.items()):z.writestr(p,t)
print(out)
