#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import nltk, random, spacy, argparse
import collections as col
nlp = spacy.load('en_core_web_sm')

def read(path):
    data=[]
    with open(path, 'r', encoding='iso-8859-1') as f:
        for line in f.readlines():
            temp = line.strip()
            if temp!='':
                data.append(temp)
    return data

def read_dialogue(path):
    data=[]
    with open(path, "r", encoding='iso-8859-1') as f:
        for line in f.readlines():
            temp = line.split("+++$+++")
            if temp!=[]:
                data.append(temp)
    return data

def check(s):
    doc = nlp(" ".join(s))
    negation = [tok for tok in doc if tok.dep_ == 'neg']
    d = {'pos':0, 'neg':0, 'neu':0, 'nb_negation':0}
    for w in s:
        if w.lower() in pos_words:
            d['pos']+=1
        if w.lower() in neg_words:
            d['neg']+=1
        if w.lower() not in pos_words and w.lower() not in neg_words:
            d['neu']+=1
        if len(negation)>=1:
            d['nb_negation'] = len(negation)
    return d
     
def write(name, data):
    with open(name, 'w') as f:
        for e in data:
            f.writelines(e)
            f.writelines('\n')

def data_load(args):
    data = read_dialogue(args.data_dir)
    data = [s[-1].strip() for s in data]
    d = dict(col.Counter(data))
    data = sorted(d.items(), key=lambda x:x[1], reverse=True)
    data1 = []
    for i, e in enumerate(data):
        if i%10000==0:
            print(f'processing {i} sentences')
        if e[1]>=3:
            data1.append([nltk.word_tokenize(e[0]), e[1]])
    data = data1
    res_d = []
    for e in data:
        res_d.append(check(e[0]))
    return res_d, data


def data_annotation(res_d, data):
    class_list = {'pos':[], 'neg':[], 'neu':[]}
    """the proposed method"""
    print("pos:%d  neg:%d  neu:%d"%(len(class_list['pos']), len(class_list['neg']), len(class_list['neu'])))   
    write('./positive.txt', class_list['pos'])
    write('./negative.txt', class_list['neg'])
    write('./neutral.txt', class_list['neu'])
    
def args_init():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data_dir', type = str, default = "./movie_lines.txt")
    parser.add_argument('--pos_dir', type = str, default = "../pos_neg_word_list/positive_word.txt")
    parser.add_argument('--neg_dir', type = str, default = "../pos_neg_word_list/negative_word.txt")
    return parser.parse_args()
  
#%%
if __name__ == '__main__':
    args = args_init()
    pos_words=read(args.pos_dir)
    neg_words=read(args.neg_dir)
    res_d, data = data_load(args)
    data_annotation(res_d, data)