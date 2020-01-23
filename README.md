# Analyzing-online-prices-by-using-machine-learning-techniques-ML
In my thesis, I tried to build a model that predicts whether the prices of items will be adjusted today.

[Analyzing Online Prices by Using Machine Learning Techniques](https://www.researchgate.net/publication/324749650_Analyzing_online_price_by_using_machine_learning_techniques?_sg=3UdZEoizQYN68GgK46_HMGToTjE9PHEaxeP5qUlSGBwud7scncmPiAud836hrR_waHbiEWnVNc2MWi-kAhViKDekejAW9Hpqhqg3PDtw.60jGQ3FndrHiF_rLxx7OBxeiX1dU9rbvuV0) 
(2018) (master thesis) - ML part source code.
Also documented in my [medium blog post](https://medium.com/analytics-vidhya/can-we-predict-a-price-adjustment-in-an-online-supermarket-by-using-machine-learning-and-7bf3e8fff81a).

## Table of contents
* [Requirements](#requirements)
* [Imbalanced Data](#Imbalanced-data)


## Requirements
```
Python 3.6.5
imbalanced_learn == 0.5.0
matplotlib == 3.1.2
numpy == 1.15.4
pandas == 0.23.4
scikit_learn == 0.21.3
seaborn == 0.9.0
```

## Imbalanced Data
As we have known by intuition, the prices in the online supermarket are not often be adjusted. 
Prices were adjusted only around 2% of the time.

To deal with this imbalanced data, I applied following methods;
1. Use a tree-based algorithm
2. Resampling
3. Use appropriate metrics

