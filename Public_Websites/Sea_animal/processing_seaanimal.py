import os
import glob
from PIL import Image
img_dir= "/your/image/data/path"

for files in glob.glob(os.path.join(img_dir,"*.*")):
    img=Image.open(files).convert("RGB").resize((512,512))
    target=Image.new("RGB",(522,522),(255,255,255))
    target.paste(img,(5,5,517,517))
    target.save(files)
