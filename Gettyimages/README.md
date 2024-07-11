# Gettyimages part

We provide both the human-annotated and model-generated annotations for the images from the [Gettyimages website](https://www.gettyimages.com/).

## The directory structure of Flickr should be this:
├──Shutterstock
   ├── human-annotated 
       ├── [gettyimages_images.zip]() 
       └── [gettyimages_jsons.zip]()
   ├── model-generated
       ├── [gettyimages.json](https://www.dropbox.com/scl/fi/v4ffjl0x7wg14rgswr4qi/gettyimages.json?rlkey=sxscctvhw44cx2uf1kgp2kbq7&st=nfksm6s6&dl=0)
       └── [Coming soon]()

## Human-annotated	
You should download the images and jsons for the `human-annotated` part based on the provided Dropbox link. All the mask annotations are included in `gettyimages_jsons.zip`. We do not have the copyright of these images. If the images violated the copyright issue, we would remove the images immediately.

## Model-generated
For the `model-generated` part, we provide the `gettyimages.json`, which contains the image url links and corresponding Alt-text captions. You can download all the images based on the provided urls. The model-generated mask annotations for this part is huge. We are now organizing the JSON files and will release these annotations very soon!

## Citation

If you find the data are useful in your research, please consider citing:

```bibtex
@misc{gettyimages,
  title={Getty Images},
  howpublished={\url{https://www.gettyimages.com/}}
}
@article{ziqiang2024marineinst,
  title={MarineInst: A Foundation Model for Marine Image Analysis with Instance Visual Description},
  author={Ziqiang Zheng, Yiwe Chen, Huimin Zeng, Tuan-Anh Vu, Binh-Son Hua, Sai-Kit Yeung},
  journal={European Conference on Computer Vision (ECCV)},
  year={2024},
  publisher={Springer}
}
```
