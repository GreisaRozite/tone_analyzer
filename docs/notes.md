# Project notes

## Dataset selection

- `GoEmotions` (Google): 27 emotions +neutral, (multi-label), however, the full 28 class version is too complex - there are fewer examples per class, results harder to read and errors harder to analyze
- `dair-ai/emotion`: 6 emotions, automatically labeled tweets based on hashtags. Good sample and label size for this project. However, after reading some, the labels seemed very inaccurate
- `TweetEval`: 4 emotions, human labeled, but not enough breadth, heavy slang usage

**Decision**: I chose `GoEmotions`, but filtered it to the six basic Ekman emotions (anger, disgust, fear, joy, sadness, surprise). Therefore making it less complex (manageable number of classes), while retaining label quality, as text is human-labeled and realistic

*also chose to include 'neutral', however, it was downsized to keep classes balanced and avoid majority-class bias ('neutral' makes up more than a third of training data sentences)*

## Data distribution

- `train` {'anger': 1025, 'neutral': 1000, 'joy': 853, 'sadness': 817, 'surprise': 720, 'disgust': 498, 'fear': 430}
- `validation` {'anger': 109, 'joy': 106, 'neutral': 100, 'surprise': 95, 'sadness': 84, 'disgust': 61, 'fear': 58}
- `test` {'anger': 131, 'sadness': 102, 'neutral': 100, 'joy': 93, 'surprise': 87, 'disgust': 76, 'fear': 65}

**Analysis**: The biggest class (anger) is only approx. 2.38 times the smallest (fear) for training. 
A classifier learns from what it sees most often, so should aim for roughly equal classes.
The more lopsided the data, the more the model will lean towards the big class. In my reduced training data (emotions7), the imbalance is mild (2.38x), 
so initially i started without class weights and will test `class_weight = 'balanced'` to check

## The pipeline

- `TfidfVectorizer`: sentence -> list of numbers based on the words it contains. Common words ('the', 'and') count for less, distinctive words for more. *TF-IDF stands for Term Frequency (how often each word appears in this sentence), Inverse Document Frequency (how rare the word is across all sentences)
- `LogisticRegression` is the learning part. Looks at the vectorized numbers and correct answers
- `make_pipeline` chains them together. vectorizer output -> classifier

## First run on the validation set
*the output of classification_report in train.py:

               precision    recall  f1-score   support

       anger       0.66      0.71      0.68       109
     disgust       0.72      0.48      0.57        61
        fear       0.91      0.69      0.78        58
         joy       0.82      0.76      0.79       106
     neutral       0.40      0.62      0.49       100
     sadness       0.79      0.79      0.79        84
    surprise       0.76      0.61      0.68        95

    accuracy                           0.67       613
   macro avg       0.72      0.66      0.68       613
weighted avg       0.71      0.67      0.68       613

- `support`: number of sentences with this emotion in validation set that the model was graded against
- `precision`: true positives / (true positives + false positives), that is, correct predictions of a class / all predictions of that class. Low precision means the model over-predicts that class (happening here with neutral 0.40)
- `recall`: of the real sentences of this class, how many the model found. Low recall means the model misses that class (like with disgust here at 0.48 - the model only found about 29 sentences from 61 provided) 
*precision and recall are a tradeoff. a 1.0 score on either is unrealistic and most likely indicates a problem.
- `f1-score`: 2 x (precision x recall) / (precision + recall). Called the *harmonic mean*, it summarizes precision and recall together taking both as equally important

**Analysis** The *chance level* here is 14% (since there are 7 emotions), that is, the score it would get if randomly guessing. 
Of all 613 validation sentences, the model got 67%, that is, about 411 correct (based on accuracy score), which is much higher than 14% and quite good for the initial run. 
The weak spots appear to be 'neutral' and 'disgust'

## What next

check class weights, 
attempt collapse instead? for more training data