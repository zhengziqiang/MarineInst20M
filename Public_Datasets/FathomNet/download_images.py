from fathomnet.api import boundingboxes
import os
import glob
import json
concepts=boundingboxes.find_concepts()
from fathomnet.api import images

img_dir="/your/root/data/path"

for tmp in concepts:
    if tmp=="":
        continue
    else:
        try:
            img_list=images.find_by_concept(tmp)
        except:
            continue
        for img_item in img_list:
            url=img_item.url
            attr=url.split("/")
            img_name=attr[-1]
            path_name=attr[-2]
            if not os.path.exists(os.path.join(img_dir,path_name)):
                os.mkdir(os.path.join(img_dir,path_name))

            target_path=os.path.join(img_dir,path_name)
            targe_file=os.path.join(target_path,img_name)
            if os.path.exists(targe_file):
                continue
            download_cmd="wget -P "+target_path +" "+url
            try:
                os.system(download_cmd)
            except:
                continue
            bboxes=img_item.boundingBoxes
            output_json={}
            output_json['img_name']=os.path.join(path_name,img_name)
            output_json['height']=img_item.height
            output_json['width'] = img_item.width
            extracted_bboxes=[]
            for tmp_bbox in bboxes:
                item_bbox={}
                object_concept=tmp_bbox.concept
                object_bbox=[tmp_bbox.x,tmp_bbox.y,tmp_bbox.width,tmp_bbox.height]
                item_bbox['concept']=object_concept
                item_bbox['bbox']=object_bbox
                extracted_bboxes.append(item_bbox)
            output_json['bboxes']=extracted_bboxes
            with open(targe_file[:-4]+".json", "w") as fp_merged:
                json.dump(output_json, fp_merged)
