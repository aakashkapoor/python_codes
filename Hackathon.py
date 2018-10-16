# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:10:41 2018

@author: Delol
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
#importing the dataset
dataset=pd.read_excel('Corpus.xlsx',sheetname='Sheet1')
print ("Column Headings")
print dataset.columns

#cleaning the texts

import re
import pycrfsuite
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk.help
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
corpus = []
for i in range(0, 900):
    review = re.sub('[^a-zA-Z]',' ', dataset['raw_article'][i])
    review = review.lower()
    nltk.help.upenn_tagset('NVN')
    nltk.pos_tag(review)
    review = review.split()
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    print review
    
for i,doc in enumerate (docs):
    tokens=[t for t,label in doc]
    tagged=nltk.pos_tag(tokens)
    data.append([(w,pos,label) for (w,label),(word,pos) in zip(doc,tagged)])
def word2features(doc, i):
        word = doc[i][0]
        postag = doc[i][1]

    # Common features for all words
        features = [
        'bias',
        'word.lower=' + word.lower(),
        'word[-3:]=' + word[-3:],
        'word[-2:]=' + word[-2:],
        'word.isupper=%s' % word.isupper(),
        'word.istitle=%s' % word.istitle(),
        'word.isdigit=%s' % word.isdigit(),
        'postag=' + postag
    ]

    # Features for words that are not
    # at the beginning of a document
        if i > 0:
            word1 = doc[i-1][0]
            postag1 = doc[i-1][1]
            features.extend([
            '-1:word.lower=' + word1.lower(),
            '-1:word.istitle=%s' % word1.istitle(),
            '-1:word.isupper=%s' % word1.isupper(),
            '-1:word.isdigit=%s' % word1.isdigit(),
            '-1:postag=' + postag1
            ])
        else:
        # Indicate that it is the 'beginning of a document'
            features.append('BOS')

    # Features for words that are not
    # at the end of a document
        if i < len(doc)-1:
            word1 = doc[i+1][0]
            postag1 = doc[i+1][1]
            features.extend([
            '+1:word.lower=' + word1.lower(),
            '+1:word.istitle=%s' % word1.istitle(),
            '+1:word.isupper=%s' % word1.isupper(),
            '+1:word.isdigit=%s' % word1.isdigit(),
            '+1:postag=' + postag1
            ])
        else:
        # Indicate that it is the 'end of a document'
            features.append('EOS')
        return features
            
from sklearn.model_selection import train_test_split

# A function for extracting features in documents
def extract_features(doc):
    return [word2features(doc, i) for i in range(len(doc))]

# A function fo generating the list of labels for each document
def get_labels(doc):
    return [label for (token, postag, label) in doc]

X = [extract_features(doc) for doc in data]
y = [get_labels(doc) for doc in data]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# For M&A Training data
df=pd.read_excel('MnA_Training.xlsx',sheetname='Train')
X_train=df.Acq_Final;
Y_train=df.Tar_Final;

trainer = pycrfsuite.Trainer(verbose=True)

# Submit training data to the trainer
for xseq, yseq in zip(X_train, y_train):
    trainer.append(xseq, yseq)

# Set the parameters of the model
trainer.set_params({
    # coefficient for L1 penalty
    'c1': 0.1,

    # coefficient for L2 penalty
    'c2': 0.01,  

    # maximum number of iterations
    'max_iterations': 200,

    # whether to include transitions that
    # are possible, but not observed
    'feature.possible_transitions': True
})

# Provide a file name as a parameter to the train function, such that
# the model will be saved to the file when training is finished
trainer.train('crf.model')

# Generate predictions
tagger = pycrfsuite.Tagger()
tagger.open('crf.model')
y_pred = [tagger.tag(xseq) for xseq in X_test]

# Let's take a look at a random sample in the testing set
i = 12
for x, y in zip(y_pred[i], [x[1].split("=")[1] for x in X_test[i]]):
    print("%s (%s)" % (y, x))

# Create a mapping of labels to indices
labels = {"N": 1, "I": 0}

# Convert the sequences of tags into a 1-dimensional array
predictions = np.array([labels[tag] for row in y_pred for tag in row])
truths = np.array([labels[tag] for row in y_test for tag in row])

# Print out the classification report
print(classification_report(
    truths, predictions,
    target_names=["I", "N"]))




    