# Sea Animal Dataset

The images are from [Kaggle Sea Animal Dataset](https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste/data). We only select the partial marine images for performing the annotation. In total, we have provided annotations (7,448 instance masks) for 3,080 images.

After downloading the images, please run the following codes to do some post-processing to get the same images as our training images.

```
python processing_seaanimal.py
```

The annotations of the images are included in the `jsons.zip`.

## Citation

If you find the data are useful in your research, please consider citing:

```bibtex
@misc{animal,
  title={Sea Animal Image Dataset},
  howpublished={\url{https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste}},
  year={2018}
}
@article{ziqiang2024marineinst,
  title={MarineInst: A Foundation Model for Marine Image Analysis with Instance Visual Description},
  author={Ziqiang Zheng, Yiwe Chen, Huimin Zeng, Tuan-Anh Vu, Binh-Son Hua, Sai-Kit Yeung},
  journal={European Conference on Computer Vision (ECCV)},
  year={2024},
  publisher={Springer}
}
```
