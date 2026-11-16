# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:52:03 2026

@author: sabin
"""

from datasets import load_from_disk
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

data = load_from_disk('data/emotions7')
train = data['train']
validation = data['validation']
test = data['test']

X_train = train['text'] # inputs
Y_train = train['emotion'] # outputs

X_validation = validation['text'] # inputs
Y_validation = validation['emotion'] # outputs

X_test = test['text'] # inputs
Y_test = test['emotion'] # outputs

model = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))

model.fit (X_train, Y_train)

predictions = model.predict(X_validation)

print(classification_report(Y_validation, predictions))