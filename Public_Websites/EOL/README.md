# EOL

Please download the original images from the official [EOL](https://www.eol.org/) based on the provided `eol_urls.txt` file.

After downloading images, please run the following codes to do some post-processing to get the same images as our training images.

```
python processing_eol.py
```

We do not have the copyright of these images. We only provide the image URL for you to download the images on your own.

The annotations of the images are included in the `jsons.zip`. Please note that we do not provide the mask annotations for all the images. We only select 22,789 images (after removing some duplicated images) for performing the mask annotation.

## Citation

If you find the data are useful in your research, please consider citing:

```bibtex
@misc{eol,
  title={Encyclopedia of Life},
  howpublished={\url{http://eol.org}},
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
