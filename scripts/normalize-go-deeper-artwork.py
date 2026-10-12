from PIL import Image
from scipy.ndimage import binary_fill_holes, binary_dilation, binary_closing, label, gaussian_filter
import numpy as np
from pathlib import Path

files = [
  "ai-seo-how-ai-changes-search.webp",
  "image-accessibility-qa-standard.webp",
  "One-variable product page test-6.webp",
]
for name in files:
    p=Path(name)
    img=Image.open(p).convert("RGB").resize((1648,928),Image.Resampling.LANCZOS)
    a=np.asarray(img).astype(np.float32)
    lo=a.min(axis=2); hi=a.max(axis=2)
    ink=(lo<145)|((hi-lo>65)&(lo<205))
    dil=binary_dilation(ink,iterations=2)
    filled=binary_fill_holes(binary_closing(dil,iterations=3))
    labs,_=label(filled)
    sizes=np.bincount(labs.ravel())
    keep=np.flatnonzero(sizes>=100)
    keep=keep[keep>0]
    mask=binary_dilation(np.isin(labs,keep),iterations=3)
    alpha=np.uint8(np.clip(gaussian_filter(mask.astype(float),1),0,1)*255)
    out=Image.fromarray(np.dstack((np.asarray(img),alpha)),"RGBA")
    out.save(p,format="WEBP",quality=94,method=6)
    print(f"Processed {name}: {out.size}, {out.mode}, transparent pixels={int((alpha==0).sum())}")
