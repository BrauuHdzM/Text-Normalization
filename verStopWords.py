import spacy

##stop words de spacy en español
nlp = spacy.load("es_core_news_sm")
stop_words = nlp.Defaults.stop_words

print(stop_words)


