from pathlib import Path
from collections import Counter
import json, re, subprocess, urllib.parse

root=Path('.')
tracked=subprocess.check_output(['git','ls-files','-z']).decode().split('\0')
tracked=[p for p in tracked if p and Path(p).is_file()]
exts={'.png','.jpg','.jpeg','.webp','.svg','.gif','.avif','.ico'}
images=[p for p in tracked if Path(p).suffix.lower() in exts]
code_exts={'.html','.htm','.css','.js','.jsx','.ts','.tsx','.json','.md','.xml','.yml','.yaml','.txt','.webmanifest','.php'}
text={}
for p in tracked:
 if Path(p).suffix.lower() in code_exts:
  try:text[p]=Path(p).read_text(encoding='utf-8')
  except (UnicodeError,OSError):pass

used=[]
maybe=[]
unused=[]
for p in images:
 base=Path(p).name
 # Full path and basename references cover absolute, relative, encoded, CSS url, JSON etc
 aliases={p,base,urllib.parse.quote(base),urllib.parse.quote(p),base.replace(' ','%20')}
 hits=sorted([name for name,src in text.items() if name!=p and any(a in src for a in aliases)])
 if hits:used.append({'path':p,'refs':hits})
 elif re.search(r'(logo|favicon|icon|og-|social|apple-touch|share|preview|source|original|sprite|manifest)',base,re.I):
  maybe.append({'path':p,'reason':'Unreferenced but potentially implicit/reserved site image'})
 else:unused.append(p)

report={'tracked_images':len(images),'referenced':len(used),'needs_manual_review':len(maybe),'unreferenced_candidates':len(unused),'used':used,'manual_review':maybe,'candidates':unused}
Path('image-asset-audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['tracked_images','referenced','needs_manual_review','unreferenced_candidates']},indent=2))
