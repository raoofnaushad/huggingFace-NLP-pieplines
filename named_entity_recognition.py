from transformers import pipeline

ner = pipeline('ner')
sequence = "This story is written by Raoof Naushad from India working at Accubits Technologies."
print(ner(sequence))