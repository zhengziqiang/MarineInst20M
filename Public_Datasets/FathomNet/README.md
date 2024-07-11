# FathomNet dataset

It is very tricky to provide the image annotations for the images from FathomNet. The official FathomNet did not provide Archive or link for their collected images. Instead, they only provide the API for accessing their images and the BBOX annotations. We provide the corresponding codes to download the images and save the annotations in the JSON format.

Please run the following code to download the images from the FathomNet:

```
python download_images.py
```

You can find more information from the official website of [FathomNet](https://fathomnet.org/fathomnet/#/).

For generating the mask annotations from the BBOX annotations, please run the following code to perform the conversion:

```
python scripts/conversion_based_bbox.py --model_type vit_h --checkpoint_path sam_vit_h_4b8939.pth --test_img_path <scraped_image_path> --label_path <above_generated_json_path> --output_dir ./json_converted
```

Please download the official checkpoint: the ViT-H version of SAM and find more information about the installation of SAM at [SAM](https://github.com/facebookresearch/segment-anything). 

## Citation

If you find the data are useful in your research, please consider citing:

```bibtex
@article{katija2022fathomnet,
  title={FathomNet: A global image database for enabling artificial intelligence in the ocean},
  author={Katija, Kakani and Orenstein, Eric and Schlining, Brian and Lundsten, Lonny and Barnard, Kevin and Sainz, Giovanna and Boulais, Oceane and Cromwell, Megan and Butler, Erin and Woodward, Benjamin and others},
  journal={Scientific reports},
  volume={12},
  number={1},
  pages={15914},
  year={2022},
  publisher={Nature Publishing Group UK London}
}
@article{ziqiang2024marineinst,
  title={MarineInst: A Foundation Model for Marine Image Analysis with Instance Visual Description},
  author={Ziqiang Zheng, Yiwe Chen, Huimin Zeng, Tuan-Anh Vu, Binh-Son Hua, Sai-Kit Yeung},
  journal={European Conference on Computer Vision (ECCV)},
  year={2024},
  publisher={Springer}
}
@article{kirillov2023segment,
  title={Segment anything},
  author={Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C and Lo, Wan-Yen and others},
  journal={IEEE/CVF International Conference on Computer Vision (ICCV)},
  year={2023}
}
```
