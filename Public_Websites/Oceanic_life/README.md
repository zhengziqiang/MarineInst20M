# Oceanic Life Dataset

The images are from [Kaggle Oceanic Life Dataset](https://www.kaggle.com/datasets/cyanex1702/oceanic-life-dataset). We only select the partial marine images for performing the annotation. In total, we have provided annotations (20,811 instance masks) for 5,029 images.

After downloading the images, please run the following codes to do some post-processing to get the same images as our training images.

```
python processing_oceanic_life.py
```

The annotations of the images are included in the `jsons.zip`.

## Citation

If you find the data are useful in your research, please consider citing:

```bibtex
@misc{oceanic,
  title={Oceanic Life Dataset},
  howpublished={\url{https://www.kaggle.com/datasets/cyanex1702/oceanic-life-dataset}},
  year={2023}
}
@article{ziqiang2024marineinst,
  title={MarineInst: A Foundation Model for Marine Image Analysis with Instance Visual Description},
  author={Ziqiang Zheng, Yiwe Chen, Huimin Zeng, Tuan-Anh Vu, Binh-Son Hua, Sai-Kit Yeung},
  journal={European Conference on Computer Vision (ECCV)},
  year={2024},
  publisher={Springer}
}
```
