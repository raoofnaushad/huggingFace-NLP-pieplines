from transformers import pipeline

nlp = pipeline("sentiment-analysis")

print(nlp("You are bad"))
print(nlp("I like you"))