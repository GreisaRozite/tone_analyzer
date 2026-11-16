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
