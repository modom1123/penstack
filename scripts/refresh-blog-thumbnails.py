from PIL import Image
import numpy as np
from pathlib import Path

names = [
  "final-product-taxonomy-before-catalog-becomes-a-mess.webp",
  "final-agencies-onboard-new-ecommerce-client-penstack.webp",
  "final-audit-inherited-shopify-catalog.webp",
  "final-product-listing-qa-standard-team.webp",
  "final-one-account-multiple-brands-separate-stores.webp",
]
for name in names:
  path = Path(name)
  image = Image.open(path).convert("RGB")
  arr = np.asarray(image)
  lo, hi = arr.min(axis=2), arr.max(axis=2)
  ys, xs = np.where((lo < 125) & ((hi - lo) > 15))
  x0, x1 = np.percentile(xs, [0.2, 99.8])
  y0, y1 = np.percentile(ys, [0.2, 99.8])
  crop = image.crop((max(0,int(x0-45)), max(0,int(y0-50)), min(image.width,int(x1+45)), min(image.height,int(y1+50))))
  scale = min(1500/crop.width,805/crop.height)
  crop = crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
  output = Image.new("RGB",(1648,928),(251,249,244))
  output.paste(crop,((1648-crop.width)//2,(928-crop.height)//2))
  output.save(path,format="WEBP",quality=91,method=6)
  print(f"Updated {path} ({crop.size})")
