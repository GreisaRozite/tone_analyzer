# Project notes

## Dataset selection

- `GoEmotions` (Google): 27 emotions +neutral, multi-label), too complex. There are fewer examples per class, results harder to read and errors harder to analyze
- `dair-ai/emotion`: 6 emotions, automatically labeled tweets based on hashtags. Good sample and label size for this project. However, after reading some, the labels seemed very innacurate
- `TweetEval`: 4 emotions, human labeled, but not enough breadth, heavy slang usage

**Decision**: I chose `GoEmotions`, but collapsed it to the six basic Ekman emotions (anger, disgust, fear, joy, sadness, surprise). Therefore making it less complex (manageable number of classes), while retaining accuracy, as text is human-labeled and realistic

*also chose to include 'neutral', however, it was downsized to keep classes balanced and avoid majority-class bias ('neutral' makes up more than a third of training data sentences)*

## Data distribution

- `train` {'anger': 1025, 'neutral': 1000, 'joy': 853, 'sadness': 817, 'surprise': 720, 'disgust': 498, 'fear': 430}
- `validation` {'anger': 109, 'joy': 106, 'neutral': 100, 'surprise': 95, 'sadness': 84, 'disgust': 61, 'fear': 58}
- `test` {'anger': 131, 'sadness': 102, 'neutral': 100, 'joy': 93, 'surprise': 87, 'disgust': 76, 'fear': 65}

**Analysis**: The biggest class (anger) is only approx. 2.38 times the smallest (fear) for training. 
A classifier learns from what it sees most often, so should aim for proportional classes.
The more lopsided the data, the more the model will lean towards the big class. In my reducted training data (emotions7), the imbalance is mild (2.38x), 
so there is no need to balance it with additional tools