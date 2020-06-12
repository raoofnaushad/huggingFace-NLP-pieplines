from transformers import pipeline

translator = pipeline("translation_en_to_de")
print(translator("Medium blogs are so cool. Easy to read and easy to write", max_length=40)