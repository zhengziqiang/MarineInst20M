import os
import glob
from PIL import Image
img_dir= "/your/image/data/path"

for files in glob.glob(os.path.join(img_dir,"*.*")):
    img=Image.open(files).convert("RGB").resize((1024,1024))
    target=Image.new("RGB",(1044,1044),(255,255,255))
    target.paste(img,(10,10,1034,1034))
    target.save(files)
