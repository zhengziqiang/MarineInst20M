# Shutterstock part

We provide both the human-annotated and model-generated annotations for the images from the [Shutterstock website](https://www.shutterstock.com/).

## The directory structure of Flickr should be this:
```
├──Shutterstock
   ├── human-annotated 
       ├── [shutterstock_images.zip](https://www.dropbox.com/scl/fi/8mw783exbk4hgjixbbz4r/shutterstock_images.zip?rlkey=05wp43xqys6h278akvrhpyv99&st=vo7whdgt&dl=0) 
       └── [shutterstock_jsons.zip](https://www.dropbox.com/scl/fi/2yxpp0zaha1ndynnze98a/shutterstock_jsons.zip?rlkey=8jpl4rd2ejh67nhdxv4kfcsav&st=mskhln9p&dl=0)
   ├── model-generated
       ├── [shutterstock.json](https://www.dropbox.com/scl/fi/nq5phvemaufzvvz0mq8kx/shutterstock.json?rlkey=8ba0p10u4a214cdwb4bx01ymn&st=c2eh2vus&dl=0)
       └── [Coming soon]()
```

## Human-annotated	
You should download the images and jsons for the `human-annotated` part based on the provided Dropbox link. All the mask annotations are included in `shutterstock_jsons.zip`. We do not have the copyright of these images. If the images violated the copyright issue, we would remove the images immediately.

## Model-generated
For the `model-generated` part, we provide the `shutterstock.json`, which contains the image url links and corresponding Alt-text captions. You can download all the images based on the provided urls. The model-generated mask annotations for this part is huge. We are now organizing the JSON files and will release these annotations very soon!

## Citation

If you find the data are useful in your research, please consider citing:

```bibtex
@misc{shutterstock,
  title={ShutterStock},
  howpublished={\url{https://www.shutterstock.com/}}
}
@article{ziqiang2024marineinst,
  title={MarineInst: A Foundation Model for Marine Image Analysis with Instance Visual Description},
  author={Ziqiang Zheng, Yiwe Chen, Huimin Zeng, Tuan-Anh Vu, Binh-Son Hua, Sai-Kit Yeung},
  journal={European Conference on Computer Vision (ECCV)},
  year={2024},
  publisher={Springer}
}
```
