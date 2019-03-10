import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.linear_model import ElasticNet
from imblearn.under_sampling import (EditedNearestNeighbours)
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import ADASYN
from imblearn.combine import SMOTEENN
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import average_precision_score
from sklearn.metrics import cohen_kappa_score


## resampling methods
# SMOTE
sm = SMOTE(ratio='auto', kind='regular', random_state=7)
trainstome_x, trainstome_y = sm.fit_sample(train_x, train_y)

# random oversampling
ros = RandomOverSampler(random_state=7)
over_x, over_y = ros.fit_sample(train_x, train_y)

# ADASYN
ada = ADASYN()
ada_x, ada_y = ada.fit_sample(train_x, train_y)

# random undersampling
rus = RandomUnderSampler(return_indices=True, random_state=7)
under_x, under_y, idx_resampled = rus.fit_sample(train_x, train_y)

# ENN
enn = EditedNearestNeighbours(return_indices=True)
enn_x, enn_y, idx_resampled = enn.fit_sample(train_x, train_y)

# SMOTE + ENN
sme = SMOTEENN(random_state=7)
stenntrain_x, stenntrain_y = sme.fit_sample(train_x, train_y)
