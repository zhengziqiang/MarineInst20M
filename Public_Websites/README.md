# Public Websites

We only provide the instance mask annotations of the existing public websites. We do **not** provide the original images from these public websites. You must download these original images based on the provided `urls.txt/urls.zip` file. We keep the same name of the original image file. For example, the name our annotation file for image `47195_fhVNyPvbSh.jpg` is `47195_fhVNyPvbSh.json` (one-to-one correspondence). Please note that we do **not** provide the mask annotations for all the images. Some images are ignored due to some reasons.

## The directory structure of Public Websites is:
```
├──Public_Websites
   ├── EOL
       ├── README.md # provide further information
       ├── jsons.zip # the json zip for the instance mask annotations
       ├── processing_xxx.py # perform further post-processings to obtain the same images as the annotation files
       └── eol_urls.txt # url file for downloading the images 
   ├── ...
```

We provide corresponding `README.md` file under each folder to provide more information.
