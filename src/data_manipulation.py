# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:26:35 2026

@author: sabin

"""

from datasets import load_dataset

data = load_dataset("google-research-datasets/go_emotions", "simplified")

names = data["train"].features["labels"].feature.names

target=['anger','disgust','fear','joy','sadness','surprise']
ekman_emotions=set()

for e in target:
    for i, j in enumerate(names):
        if j == e:
            ekman_emotions.add(i)

print(ekman_emotions)