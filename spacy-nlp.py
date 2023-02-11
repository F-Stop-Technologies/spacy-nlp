import spacy

# Load the large English NLP model
nlp = spacy.load("en_core_websm")

# The text to be processed
text = input("NLP: ")

# Process the text using the NLP model
doc = nlp(text)

# Iterate over the named entities and print their label and text
for ent in doc.ents:
    print(ent.label, ent.text)
