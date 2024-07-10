import os
import glob
from PIL import Image
img_dir= "/your/image/data/path"

for files in glob.glob(os.path.join(img_dir,"*.*")):
    img=Image.open(files).convert("RGB").resize((1280,720))
    target=Image.new("RGB",(1290,730),(255,255,255))
    target.paste(img,(5,5,1285,725))
    target.save(files)
