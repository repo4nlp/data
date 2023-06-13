# Data Construction Procedure
We herein describe how to obtain dialogue utterances and annotation procedures of utterances.

## Prerequisites 
Install all necessary packages for data processing:
```
pip install -r requirements.txt
```
After installing spacy, please run ```python -m spacy download en_core_web_sm``` to download the ```en_core_web_sm``` module.

## Data extraction and automatic annotation 
Please obtain the Cornell movie dialogs corpus [here](https://www.kaggle.com/datasets/rajathmc/cornell-moviedialog-corpus). After downloading the original corpus, please put *movie_lines.txt* in whatever directory you like. 


<img src="https://github.com/repo4nlp/data/blob/main/data.png" width="250" height="200">

Then, please obtain a positive word list and negative word list from the [Mining and summarizing customer reviews (Hu and Liu, KDD-2004)](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html). There are supposed to be 4783 positive words and 2006 negative words in each list, and make sure that each line in each list contains one word.

Please put dialogue data, positive word list, and negative word list as indicated below and run the following command:

```shell
python data_processing.py 
  --data_dir 'movie_lines.txt' 
  --pos_dir 'positive_word.txt' 
  --neg_dir 'negative_word.txt' 
```

The extracted data will be saved in the current directory with names *positive.txt*, *negative.txt*, and *neutral.txt*, respectively.
