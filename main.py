import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import nltk

# try:
#     dl_list = ['names', 'stopwords', 'vader_lexicon', 'punkt', 'averaged_perceptron_tagger', 'state_union']
#     nltk.download(dl_list)
# except Exception as e:
#     print(e)

base_path = '/mount/sangsplaygrounddev/ngsplaygroundfileshare/'

dev_path = os.path.join(base_path, 'dev.tsv')

df = pd.read_csv(dev_path,  sep='\t', header=None)
# print(df.columns)
# print(df.describe())
print(df.iloc[0])
