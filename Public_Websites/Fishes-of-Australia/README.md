Please download the original images from the official [Fishes-of-Australia](https://fishesofaustralia.net.au/) based on the provided `urls.zip` file.

After downloading images, please run the following codes to do some post-processing to get the same images as our training images.

```
python processing_australia.py
```

We do not have the copyright of these images. We only provide the image URL for you to download the images on your own.

The annotations of the images are included in the `fishes-of-australia.zip`. Please note that we do not provide the mask annotations for all the images.

## Citation

If you find the data are useful in your research, please consider citing:

```bibtex
@misc{australia,
  title={Fishes of Australia},
  author={Bray, D.J. \& Gomon, M.F. (eds)},
  howpublished={\url{http://fishesofaustralia.net.au/}},
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
