It is very tricky to provide the image annotations for the images from FathomNet. The official FathomNet did not provide Archive or link for their collected images. Instead, they only provide the API for accessing their images and the BBOX annotations. We provide the corresponding codes to download the images and save the annotations in the JSON format.

Please run the following code to download the images from the FathomNet:

```python download_images.py```

You can find more information from the official website of [FathomNet](https://fathomnet.org/fathomnet/#/).

For generating the mask annotations from the BBOX annotations, please run the following code to perform the conversion:

```python scripts/conversion_based_bbox.py --model_type vit_h --checkpoint_path sam_vit_h_4b8939.pth --test_img_path <scraped_image_path> --label_path <above_generated_json_path> --output_dir ./json_converted```

Please download the official checkpoint: the ViT-H version of SAM and find more information about the installation of SAM at [SAM](https://github.com/facebookresearch/segment-anything). 
