import nltk

nltk.download("punkt") 
nltk. download("wordnet")

from nltk.stem import PorterStemmer

stemmer=PorterStemmer()

import pickle

import json

import numpy as np

words=[]
classes=[]
word_tag_list=[]
ignorewords=['?','!',"'s","'m",'.',',']
train_data_file=open("intents.json").read()

intents=json.loads(train_data_file)
#print(intents)


def get_stem_words(words,ignore_words): 
    stem_words=[] 
    for word in words: 
        if word not in ignore_words: 
            w= stemmer.stem(word.lower()) 
            stem_words.append(w) 
    return stem_words 
    

for j in intents["abbas"]: 
    for pattern in j["patterns"]: 
        pattern_word= nltk.word_tokenize(pattern) 
        words.extend(pattern_word) 
        word_tag_list.append((pattern_word,j["tags"])) 
    if j["tags"] not in classes: 
        classes.append(j["tags"]) 
        stem_words= get_stem_words(words,ignorewords) 
# print("what is word", stem_words) 
# print(word_tag_list) 
# print(classes)

def create_bot_corpus (stem_words, classes):

    stem_words=sorted(list(set(stem_words)))
    classes=sorted(list(set(classes)))

    #print(stem_words)

    pickle.dump(stem_words,open("words.pkl","wb"))
    pickle.dump(stem_words,open("classes.pkl","wb"))
    return stem_words, classes

stem_words, classes=create_bot_corpus (stem_words, classes)
     
training_data=[]
number_of_tags=len(classes)
labels=[0]*number_of_tags



for word_tag in word_tag_list:
    print(word_tag)
    bag_of_words=[]
    pattern_word= word_tag[0]
    print(pattern_word)

    for i in pattern_word:
        index=pattern_word.index(i)
        print(index)
        word=stemmer.stem(i.lower())
        print(word)
        pattern_word[index]=word
for j in stem_words: 
    if j in pattern_word: 
        bag_of_words.append(1) 
    else: 
        bag_of_words.append(0) 
        print(bag_of_words)