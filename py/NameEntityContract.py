import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
def file_contents(file_name):
    with open(file_name) as f:
        try:
            return f.read()
        finally:
            f.close()
text = file_contents('txt/LetterofContract1.txt')
# text = file_contents('ReferenceLetter.txt')
# print(text)
# print(sent_tokenize(text))


# In[117]:


def extract_phone_numbers(text):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(text)
    return [re.sub(r'\D', '', number) for number in phone_numbers]


# In[118]:


def extract_email_addresses(text):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(text)


# In[119]:


def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences


# In[141]:


def extract_names(text):
    names = []
    sentences = ie_preprocess(text)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                        
                if chunk.label() == 'PERSON':
                    
                    names.append(' '.join([c[0] for c in chunk]))
    return names


# In[142]:


if __name__ == '__main__':
    numbers = extract_phone_numbers(text)
    emails = extract_email_addresses(text)
    names = extract_names(text)


# In[139]:


from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                        continuous_chunk.append(named_entity)
                        current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)
            
    return continuous_chunk

txt =  file_contents('txt/LetterofContract1.txt')
# txt = file_contents('ReferenceLetter.txt')
get_continuous_chunks (txt)

import boto3
import json
import csv
import ast
import pandas as pd
from IPython.display import display, HTML
comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')


# print('Calling DetectEntities')
response=(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
# print(response)

x = json.loads(response, strict=False)["Entities"]

#convert to table

df = pd.DataFrame.from_dict(x, orient='columns')
# display(df)
display(df.to_html(justify="center"))
# df.to_csv('output2.csv')


#entites = list(set([x['Type'] for x in response1['Entities']]))


#print (entites)
# print('End of DetectEntities\n')