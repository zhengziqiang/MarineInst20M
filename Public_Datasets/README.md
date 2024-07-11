# Public datasets

We only provide the instance mask annotations of the existing public datasets after our conversion based on their provided annotations (for example, point and bounding box). We do **not** provide the original images from these public datasets. You must download these original images on your own. We keep the same name of the original image file. For example, the name our annotation file for image `7117_Caranx_sexfasciatus_juvenile_f000001.jpg` is `7117_Caranx_sexfasciatus_juvenile_f000001.json` (one-to-one correspondence). 

## The directory structure of Public dataset is:
```
├──Public_Datasets
   ├── Aquarium
       ├── README.md # provide further information
       └── xxxx.zip # the json zip for the instance mask annotations
   ├── DeepFish
       ├── README.md
       └── xxxx.zip
   ├── ...
```

We provide corresponding `README.md` file under each folder to provide more information.

## visualization
  
<p align="center">
    <img src="figs/conversion.jpg" width="100%"></a> <br>
    Visualization of provide mask annotations for various public marine datasets.
</p>
