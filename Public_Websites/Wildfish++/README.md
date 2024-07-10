The images are from [Wildfish](https://github.com/PeiqinZhuang/WildFish) and [Wildfish++](https://github.com/PeiqinZhuang/WildFish++). We only select the partial marine images for performing the annotation. In total, we have provided annotations (17,075 instance masks) for 9,367 images.

After downloading the images, please run the following codes to do some post-processing to get the same images as our training images.

```python processing_wildfish.py```

The annotations of the images are included in the jsons.zip.

Our naming is "<image_folder>_<image_name>.json", for example, "Abalistes_stellaris_00004.json".

Please download the images based on the provided json files.
