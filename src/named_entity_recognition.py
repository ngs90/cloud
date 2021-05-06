import spacy 
from spacy import displacy

#nlp_small = spacy.load('en_core_web_sm')
#nlp_medium = spacy.load('en_core_web_md')
#nlp_trf = spacy.load('en_core_web_trf')

def entities(text, nlp_model='en_core_web_sm'):
    nlp = spacy.load(name=nlp_model)
    doc = nlp(text)
    ent = displacy.render(doc, style='ent')
    #dep = displacy.render(doc, style='dep')
    return ent # , dep