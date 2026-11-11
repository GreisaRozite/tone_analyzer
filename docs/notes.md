# Project notes

## Dataset selection

- `GoEmotions` (Google): 27 emotions +neutral, multi-label), too complex. There are fewer examples per class, results harder to read and errors harder to analyze
- `dair-ai/emotion`: 6 emotions, automatically labeled tweets based on hashtags. Good sample and label size for this project, however after reading a few deemed very innacurate
- `TweetEval`:4 emotions, human labeled, but not enough breadth, heavy slang usage

*Decision*
I chose `GoEmotions`, but collapsed it to the six basic Ekman emotions (anger, disgust, fear, joy, sadness, surprise). Therefore making it less complex (manageable number of classes), while retaining accuracy, as text is human-labeled and realistic


