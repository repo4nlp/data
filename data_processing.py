#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk, random, spacy, argparse, utlis
import collections as col
nlp = spacy.load('en_core_web_sm')

def check(s):
    """
    yield # of positive words, negative words, neutral words and negation words for each sentence
    """
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
     

def data_load(args):
    data = utlis.read_dialogue(args.data_dir)
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
    """annotation procedure. please refer to the paper for more details"""
    class_list = {'pos':[], 'neg':[], 'neu':[]}
    N=0
    for d, e in zip(res_d, data):
        if e[0]==[] or e[0][-1]=='?':
            N+=1
            continue
        if d['pos']>=1 and d['neg']==0 and e[0][-1]!='?':
            if d['nb_negation']%2==0:
                class_list['pos'].append(" ".join(e[0]))
            else:
                class_list['neg'].append(" ".join(e[0]))
                
        if d['neg']>=1 and d['pos']==0 and e[0][-1]!='?':
            if d['nb_negation']%2==0:
                class_list['neg'].append(" ".join(e[0]))  
            else:
                class_list['pos'].append(" ".join(e[0]))  
            
        if d['neg']==0 and d['pos']==0 and e[0][-1]!='?':
            class_list['neu'].append(" ".join(e[0]))    
    print("pos:%d  neg:%d  neu:%d"%(len(class_list['pos']), len(class_list['neg']), len(class_list['neu'])))   
    return class_list
    
    
def args_init():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data_dir', type = str, default = "./cornell_movie-dialogs_corpus/movie_lines.txt")
    parser.add_argument('--pos_dir', type = str, default = "./positive_word.txt")
    parser.add_argument('--neg_dir', type = str, default = "./negative_word.txt")
    return parser.parse_args()


#%%
if __name__ == '__main__':
    args = args_init()
    pos_words=utlis.read(args.pos_dir)
    neg_words=utlis.read(args.neg_dir)
    res_d, data = data_load(args)
    class_list = data_annotation(res_d, data)
    utlis.write('positive.txt', class_list['pos'][:10])
    utlis.write('negative.txt', class_list['neg'][:10])
    utlis.write('neutral.txt', class_list['neu'][:10])
