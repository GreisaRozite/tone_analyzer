# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:26:35 2026

@author: sabin

"""

from datasets import load_dataset, concatenate_datasets

raw_data = load_dataset('google-research-datasets/go_emotions', 'simplified')

names = raw_data['train'].features['labels'].feature.names

target=['anger','disgust','fear','joy','sadness','surprise']

ekman_emotions=set()

for e in target:
    for i, j in enumerate(names):
        if j == e:
            ekman_emotions.add(i)

def filter_by_target(x):
    return all(label in ekman_emotions for label in x['labels'])
    
target_data = raw_data.filter(filter_by_target)

def one_label_only(x):
    return len(x['labels'])==1

emotion_data=target_data.filter(one_label_only)

neutral_id=27

def filter_by_neutral_only(x):
    return all(label == neutral_id for label in x['labels'])
  
neutral_data = raw_data.filter(filter_by_neutral_only)

neutral_sizes = {'train':1000, 'validation':100, 'test':100}
#split chosen proportional to emotion_data amount of examples per emotion label

for section, size in neutral_sizes.items():
    neutral_data[section] = neutral_data[section].shuffle(seed=42).select(range(size))

train = concatenate_datasets ([emotion_data['train'], neutral_data['train']]).shuffle(seed=42)

validation = concatenate_datasets ([emotion_data['validation'], neutral_data['validation']]).shuffle(seed=42)

test = concatenate_datasets ([emotion_data['test'], neutral_data['test']]).shuffle(seed=42)
