# Data Construction Procedure
We herein dedcribe how to obtain generic response and annotation procedure.

### Acqusition of generic responses 
step 1. Install all necessary packages for data processing:
```
pip install -r requirements.txt
```

step 2. Obtain the original cornell movie dialogs corpus [here](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html). After downloading the original corpus, please put *movie_lines.txt* in whatever directory you like. Also, please download. run the following commend:
```shell
python data_processing.py
```
![image](https://github.com/repo4nlp/data/blob/main/data.png)

The data will be saved in the current directory with names, *positive.txt*, *negative.txt*, and *neutral.txt* respectively.
