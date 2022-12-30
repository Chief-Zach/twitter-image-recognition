# Twitter Profile Picture Analyzer
[![wakatime](https://wakatime.com/badge/user/671d32e4-888d-43d9-8178-5f26d6a7202d.svg)](https://wakatime.com/@671d32e4-888d-43d9-8178-5f26d6a7202d)
![twitter](https://img.shields.io/twitter/follow/chiefz_sol?style=social)

This tool leverages the power of OpenCV and other image processing libraries to compare the profile pictures of 
Twitter users to pictures of the users choosing. This can be useful for 
### Instillation
#### Download the repository
```
git clone https://github.com/Chief-Zach/twitter-image-recognition 
```

#### Install packages:
```
pip3 -m install -r requirements.txt
```

#### Create .env
Fill in each of the variables with no spaces in between the "=" and first character of keys from your [Twitter Developer
account](https://developer.twitter.com/en)

_consumer_key=_
_consumer_secret=_
_access_token=_
_access_token_secret=_

```
sudo vim .env
```

### Useable Metrics 
- [Root mean square error (RMSE)](https://en.wikipedia.org/wiki/Root-mean-square_deviation)
- [Peak signal-to-noise ratio (PSNR)](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)
- ~~[Structural Similarity Index (SSIM)](https://en.wikipedia.org/wiki/Structural_similarity)~~ *
- [Feature-based similarity index (FSIM)](https://www4.comp.polyu.edu.hk/~cslzhang/IQA/TIP_IQA_FSIM.pdf)
- ~~[Information theoretic-based Statistic Similarity Measure (ISSM)](https://www.tandfonline.com/doi/full/10.1080/22797254.2019.1628617)~~**
- [Signal to reconstruction error ratio (SRE)](https://www.sciencedirect.com/science/article/abs/pii/S0924271618302636)
- ~~[Universal image quality index (UIQ)](https://ece.uwaterloo.ca/~z70wang/publications/quality_2c.pdf)~~***

**SSIM is an algorithm that shows the degradation of an image during compression or by losses in transmission(1). 
Therefore, due to the compression and transfer loss of the Twitter image, this method will skew our results. This is 
also an outdated version of FSIM which works much better for detecting shapes vs quality* 

***ISSM tends to produce booleans far off the other metrics and have opted to remove it from the usable
metrics*

****Takes FOREVER. Not sustainable for running large amounts of iterations*

## Citations
(1) [SSIM: Structural Similarity Index | Imatest](https://www.imatest.com/docs/ssim/)

(2) [Creators of the Original Image Similarity Measures](https://pypi.org/project/image-similarity-measures/)