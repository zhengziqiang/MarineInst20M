The images are from [Wildfish](https://github.com/PeiqinZhuang/WildFish) and [Wildfish++](https://github.com/PeiqinZhuang/WildFish++). We only select the partial marine images for performing the annotation. In total, we have provided annotations (17,075 instance masks) for 9,367 images.

After downloading the images, please run the following codes to do some post-processing to get the same images as our training images.

```
python processing_wildfish.py
```

The annotations of the images are included in the jsons.zip.

Our naming is `<image_folder>_<image_name>.json`, for example, `Abalistes_stellaris_00004.json`.

Please download the images based on the provided json files in `jsons.zip`.

## Citation

If you find the data are useful in your research, please consider citing:

```bibtex
@article{zhuang2020wildfish++,
  title={Wildfish++: A comprehensive fish benchmark for multimedia research},
  author={Zhuang, Peiqin and Wang, Yali and Qiao, Yu},
  journal={IEEE Transactions on Multimedia (TMM)},
  volume={23},
  pages={3603--3617},
  year={2020},
  publisher={IEEE}
}
@article{ziqiang2024marineinst,
  title={MarineInst: A Foundation Model for Marine Image Analysis with Instance Visual Description},
  author={Ziqiang Zheng, Yiwe Chen, Huimin Zeng, Tuan-Anh Vu, Binh-Son Hua, Sai-Kit Yeung},
  journal={European Conference on Computer Vision (ECCV)},
  year={2024},
  publisher={Springer}
}
```
