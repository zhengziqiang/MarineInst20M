# Flickr part

We provide both the human-annotated and model-generated annotations for the images from the [Flickr website](https://www.flickr.com/).

## The directory structure of Flickr should be this:
```
├──Flickr
   ├── human-annotated 
       ├── images.zip
       └── jsons.zip
   ├── model-generated
       ├── flickr.json
       └── Coming soon
```

* [images.zip](https://www.dropbox.com/scl/fi/bn12v8xyg1uaug2nhmt2z/images.zip?rlkey=7v3tny2lu2v1sjhs3dco0cq2i&st=j7u2g6d7&dl=0) 
* [jsons.zip](https://www.dropbox.com/scl/fi/9usht3zyqbtjx0p18dkst/jsons.zip?rlkey=rc6il72ihuoon4hqy4gdlzkth&st=2vzc470a&dl=0)
* [flickr.json](https://www.dropbox.com/scl/fi/l852y1clw2o5afgg1cd6z/flickr.json?rlkey=3ajhqysvkj4cvvqon9z94aqne&st=a41ds2m8&dl=0)

## Human-annotated	
You should download the images and jsons for the `human-annotated` part based on the provided Dropbox link. All the mask annotations are included in `jsons.zip`. We do not have the copyright of these images. If the images violated the copyright issue, we would remove the images immediately.

## Model-generated
For the `model-generated` part, we provide the `flickr.json`, which contains the image url links and corresponding Alt-text captions. You can download all the images based on the provided urls. The model-generated mask annotations for this part is huge. We are now organizing the JSON files and will release these annotations very soon!

## Citation

If you find the data are useful in your research, please consider citing:

```bibtex
@misc{flickr,
  title={Flickr},
  howpublished={\url{https://www.flickr.com/}}
}
@article{ziqiang2024marineinst,
  title={MarineInst: A Foundation Model for Marine Image Analysis with Instance Visual Description},
  author={Ziqiang Zheng, Yiwe Chen, Huimin Zeng, Tuan-Anh Vu, Binh-Son Hua, Sai-Kit Yeung},
  journal={European Conference on Computer Vision (ECCV)},
  year={2024},
  publisher={Springer}
}
```
