from transformers import pipeline

nlp = pipeline("question-answering")

context = r"""
Barack Hussein Obama II is an American politician and attorney who served as the 44th president of the
 United States from 2009 to 2017. A member of the Democratic Party, Barack Obama was the first African-American 
 president of the United States.
"""

print(nlp(question="Who is Obama?", context=context))
print(nlp(question="Who is the president of United States?", context=context))


