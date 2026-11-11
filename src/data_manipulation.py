# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:26:35 2026

@author: sabin
"""

from datasets import load_dataset

data = load_dataset("google-research-datasets/go_emotions", "simplified")
print(data)