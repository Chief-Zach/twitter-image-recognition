# Twitter Profile Picture Analyzer

### Instillation
```
git clone https://github.com/Chief-Zach/twitter-image-recognition 
```

This is recommended because changes were made to some libraries in order to improve performance with the program.
This will install the VENV to your system allowing for the use of 

### Useable Metrics 
- [Root mean square error (RMSE)](https://en.wikipedia.org/wiki/Root-mean-square_deviation)
- [Peak signal-to-noise ratio (PSNR)](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)
- [Structural Similarity Index (SSIM)](https://en.wikipedia.org/wiki/Structural_similarity)
- [Feature-based similarity index (FSIM)](https://www4.comp.polyu.edu.hk/~cslzhang/IQA/TIP_IQA_FSIM.pdf)
- ~~[Information theoretic-based Statistic Similarity Measure (ISSM)](https://www.tandfonline.com/doi/full/10.1080/22797254.2019.1628617)~~*
- [Signal to reconstruction error ratio (SRE)](https://www.sciencedirect.com/science/article/abs/pii/S0924271618302636)
- [Spectral angle mapper (SAM)](https://ntrs.nasa.gov/citations/19940012238)
- [Universal image quality index (UIQ)](https://ece.uwaterloo.ca/~z70wang/publications/quality_2c.pdf)

*I have found that ISSM tends to produce booleans far off the other metrics and have opted to remove it from the useable
metrics*