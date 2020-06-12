from transformers import pipeline

nlp = pipeline("fill-mask")
print(nlp(f"HuggingFace is creating a {nlp.tokenizer.mask_token} that the community uses to solve NLP tasks."))