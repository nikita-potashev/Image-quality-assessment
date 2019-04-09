# Image quality assessment

## How to 
### Prep data
```shell
python3 utils/unzip.py --src=datasets/blur/* --dst=datasets/blur/train/
```
```shell
python3 utils/unzip.py --src=datasets/noise/* --dst=datasets/noise/train/
```
### Train by config
```shell
python3 main.py -c configs/blur_model.json
```

Thx to [Keras Template](https://github.com/Ahmkel/Keras-Project-Template)

```shell
tensorboard --logd=experiments/noise_model/summary
```
## Sharpness 
* TOTAL: 8432, %100
* CLEAR: 3606, %42.76565464895636
* DIGIT BLUR: 3606, %42.76565464895636
* NAT BLUR: 1220, %14.468690702087287
* Accuracy : ~95%.

1. https://riemenschneider.hayko.at/vision/dataset/task.php?did=382 
2. http://www.cse.cuhk.edu.hk/leojia/projects/dblurdetect/dataset.html 
3. https://mklab.iti.gr/results/certh-image-blur-dataset/ 


## Noise
* Accuracy : ~96%.

1. http://www.fit.vutbr.cz/~vasicek/imagedb/?lev=30&knd=corrupted
2. https://www.eecs.yorku.ca/~kamel/sidd/dataset.php
3. http://www.cs.utoronto.ca/~strider/Denoise/Benchmark/

## Brightness

1. http://www.aiportal.ru/articles/other/evaluation-of-image-quality.html


## Source

### Datasets

* http://homepages.inf.ed.ac.uk/rbf/CVonline/Imagedbase.htm
* http://live.ece.utexas.edu/research/Quality/index.htm

### NN

* Image qality Assessment Guided Deep Neural Networks Training
1. https://arxiv.org/pdf/1708.03880.pdf 
* Image quality assessment NN
2. https://github.com/idealo/image-quality-assessment

### Other
* Blur Detection for Digital Images Using Wavelet Transform
1. https://www.researchgate.net/publication/4124581_Blur_detection_for_digital_images_using_wavelet_transform
* Blur detection with opencv
2. https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/
* Wavelet ru
3. http://www.lib.tpu.ru/fulltext/v/Bulletin_TPU/2011/v318/i5/15.pdf

### Main things
* Метод оценки четкости фотореалистичных изображений без использования эталона
1. http://old.tusur.ru/filearchive/reports-magazine/2012-26-1/078.pdf
* Оценки качества для анализа цифровых изображений
2. https://www.researchgate.net/publication/236593352_Ocenki_kacestva_dla_analiza_cifrovyh_izobrazenij
* Сравнительный анализ  безэалонных мер оценки качества цифровых изображений
3.  https://cyberleninka.ru/article/v/sravnitelnyy-analiz-bezetalonnyh-mer-otsenki-kachestva-tsifrovyh-izobrazheniy
* Ядро
3. https://www.intuit.ru/studies/professional_skill_improvements/11289/courses/1105/lecture/17989?page=7
4. http://optica.csic.es/papers/icpr2k.pdf

