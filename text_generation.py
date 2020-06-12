from transformers import pipeline

text_generator = pipeline("text-generation")
print(text_generator("Whatever happens I want to fly", max_length=50))