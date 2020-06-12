from transformers import pipeline

nlp = pipeline("sentiment-analysis")

print(nlp("I hate you"))
print(nlp("I love you"))