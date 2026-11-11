# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:26:35 2026

@author: sabin
"""

from datasets import load_dataset
import random

data = load_dataset("google-research-datasets/go_emotions", "simplified")

names = data["train"].features["labels"].feature.names

n=random.randrange(43409)

obj=data["train"][n]
  
print(f"\nthe sentence: \n{obj["text"]}\n\nthe emotion:")
           
l=obj['labels']

for i in range (len(l)):
    emotion = l[i]
    print(names[emotion])
    
    
