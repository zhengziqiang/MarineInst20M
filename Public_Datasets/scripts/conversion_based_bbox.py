import os
import glob
import shutil
import numpy as np
import glob
import os.path
import pycocotools.mask as mask_util
import pycocotools._mask as _mask_util
import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
import json
import glob
import os
import argparse
from PIL import Image
import shutil
import pycocotools.mask as mask
from sklearn.metrics import confusion_matrix
from segment_anything import sam_model_registry, SamPredictor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_type", type=str, required=True, help="model type", choices=['vit_h', 'vit_l', 'vit_b'])
    parser.add_argument("--checkpoint_path", type=str, required=True, help="path to the checkpoint")
    parser.add_argument("--test_img_path", type=str, required=True, help="the test image path")
    parser.add_argument("--label_path", type=str, required=True, help="the test image path")
    parser.add_argument("--output_dir", type=str, required=True, help="path to save the model")
    parser.add_argument("--batch_size", type=int, default=1, help="batch size")
    parser.add_argument("--gpu", type=int, default=0, help="gpu")
    parser.add_argument("--image_size", type=int, default=1024, help="image size")
    device = "cuda"
    args = parser.parse_args()
    os.environ["CUDA_VISIBLE_DEVICES"]=str(args.gpu)
    sam_checkpoint = args.checkpoint_path
    model_type = args.model_type
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)
    predictor = SamPredictor(sam)

    for files in sorted(glob.glob(os.path.join(args.test_img_path,"*.jpg"))):
        _,name=os.path.split(files)
        if not os.path.exists(os.path.join(args.label_path,name.replace(".jpg",".json"))):
            continue
        image = cv2.imread(files,2)
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = np.uint8(image)
        except:
            continue
        print(name)
        # if os.path.exists(os.path.join(args.output_dir,name.replace(".jpg",".json"))):
        #     continue
        with open(os.path.join(args.label_path,name.replace(".jpg",".json")), "r",
                  encoding='utf-8') as f:
            aa = json.loads(f.read())
            images = aa['images']
            annotations = aa['annotations']
            height, width = images[0]['height'],images[0]['width']
            for item_anno in annotations:
                img_mask = np.zeros([height, width])
                predictor.set_image(image)
                input_box = np.array([item_anno['bbox'][0], item_anno['bbox'][1], item_anno['bbox'][0]+item_anno['bbox'][2], item_anno['bbox'][1]+item_anno['bbox'][3]])
                masks, scores, logits = predictor.predict(
                    point_coords=None,
                    point_labels=None,
                    box=input_box[None, :],
                    multimask_output=False,
                )
                img_mask[masks[0]] = 255
                area=np.sum(masks[0])
                fortran_ground_truth_binary_mask = np.asfortranarray(masks[0])
                compressed_rle = mask_util.encode(fortran_ground_truth_binary_mask)
                compressed_rle['counts'] = str(compressed_rle['counts'], encoding="utf-8")
                item_anno['segmentation'] = compressed_rle
                item_anno['area']=float(area)
                item_anno['score']=float(scores[0])
            with open(os.path.join(args.output_dir,name.replace(".jpg",".json")),"w") as fp_merged:
                json.dump(aa, fp_merged)

if __name__ == "__main__":
    main()
