from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import learning_curve
from sklearn.model_selection import cross_val_predict
from sklearn.feature_selection import mutual_info_classif
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn import metrics
from sklearn import svm
#from sklearn.externals import joblib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import string
import joblib

def readcsv():
    df=pd.read_csv("trial.csv",)#read labelled tweets
    #df2=df.reindex(np.random.permutation(df.index))
    #X=df2.text
    #y=df2.label
    X = df.text
    y = df.label
    return X, y

def drawrocNB(y_test,y_pred):
    fpr,tpr,threshold=roc_curve(y_test,y_pred)
    print("Drawing")
    roc_auc=auc(fpr,tpr)
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr,tpr,'b',label='NB AUC = %0.2f'%roc_auc,color='b')
    plt.legend(loc='lower right')
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([-0.1,1.2])
    plt.ylim([-0.1,1.2])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()

def savemodel(clf):
    joblib.dump(clf,'finalmodel.pkl') #persisting the model

def createSVM(X,y):

    svm_clf=Pipeline([('vect',CountVectorizer(max_df=0.7)),('tfidf',TfidfTransformer()),('svm',SVC(kernel="linear",C=1))])
    svm_clf=svm_clf.fit(X,y)
    return svm_clf

def createNB(X,y):

    nb_clf=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('nb',MultinomialNB())])
    nb_clf=nb_clf.fit(X,y)
    return nb_clf

def evaluatemodel(y_pred,y_test):
    print( metrics.confusion_matrix(y_test,y_pred))
    accuracy=metrics.accuracy_score(y_test,y_pred)
    print(accuracy)
    report=classification_report(y_test,y_pred)
    print(report)

def main():
    X,y=readcsv()
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)#split data into training and testing sets
    nb_clf=createNB(X_train,y_train)
    y_pred=nb_clf.predict(X_test)

    print("SVM evaluation")
    evaluatemodel(y_pred,y_test)
    drawrocNB(y_test,y_pred)
    savemodel(nb_clf)

if __name__=="__main__":
        main()
