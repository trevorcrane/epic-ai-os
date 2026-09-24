#!/usr/bin/env python3
"""Create a generic, client-safe Copycat skill package from an explicit allowlist."""
from pathlib import Path
import zipfile, hashlib, json, argparse
root=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
paths=['operating-system/CAT_COPYWRITING_AGENT_BRIEF.md','operating-system/TEAM-ROSTER.md','operating-system/MEMORY-SYNC.md','operating-system/tools/OJOY.md','operating-system/adapters/CROSS-PLATFORM.md']
paths += [str(p.relative_to(root)) for p in (root/'operating-system/skills/copycat').rglob('*') if p.is_file()]
# Generic exports keep the functional framework but remove private repo references,
# deployment rows, named staff/clients and campaign-specific references.
files={}
for path in paths:
 text=(root/path).read_text()
 if path.endswith('TEAM-ROSTER.md'):
  text='# Team roles\n\nOwner sets intent. PM coordinates. Cat/Copycat owns copy. Researcher supplies evidence. Builder implements. Independent reviewer validates. Scorekeeper records measured outcomes. Ojoy is optional and access must be verified.\n'
 elif path.endswith('CROSS-PLATFORM.md'):
  text='# Install portable Copycat\n\nLoad operating-system/CAT_COPYWRITING_AGENT_BRIEF.md and operating-system/skills/copycat/SKILL.md into your host’s supported agent instructions or project knowledge. Add only your own approved brand profile. Register the skill when supported. Confirm loaded version and tools. No account credentials are included.\n'
 else:
  text=text.replace('https://github.com/trevorcrane/epic-ai-os','[your private canonical repository]')
  text='\n'.join(line for line in text.splitlines() if not any(term in line for term in ['Alfred is Trevor','Historical Robyn campaign context:','Claude','adapters/ADOPTION.md']))+'\n'
 text=text.replace('Trevor’s','the owner’s').replace('Trevor', 'the owner').replace('Robyn, Leigh and each client’s', 'each client’s').replace('Robyn’s', 'another client’s').replace('Leigh’s', 'another client’s').replace('Leigh example', 'book-waitlist example')
 files[path]=text
files['operating-system/EPIC_AI_COMMUNICATION_STANDARD.md']='# Communication standard\n\nConnect, Care, Clarity, Call to Action. Establish a truthful reason for contact, acknowledge real context without inventing feelings, make the message understandable, and offer one useful next step. Keep claims evidence-based and voice scoped to the assigned brand.\n'
files['START-HERE.md']='# Copycat portable kit\n\nRead operating-system/adapters/CROSS-PLATFORM.md. This contains generic instructions, not client facts or credentials. Add your own brand profile.\n'
manifest={p:hashlib.sha256(t.encode()).hexdigest() for p,t in sorted(files.items())}
files['manifest.json']=json.dumps({'version':'1.0.0','sha256':manifest},indent=2)+'\n'
out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p,t in sorted(files.items()):z.writestr(p,t)
print(out)
