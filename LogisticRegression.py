
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:46:46 2019

@author: suraj
"""

import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt 
dataset=pd.read_csv('Social_Network_Ads.csv')
X=dataset.iloc[:,[2,3]].values
Y=dataset.iloc[:,4].values

from sklearn.cross_validation import train_test_split
X_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=.25,random_state =0)

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
X_train=sc_x.fit_transform(X_train)
x_test=sc_x.transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)


y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

from matplotlib.colors import ListedColormap
x_set,y_set=X_train,y_train
X1,X2=np.meshgrid(np.arange(start=x_set[:0].min()-1,stop=x_set[:,0].max()+1,step=0.01),np.arange(start=x_set[:1].min()-1,stop=x_set[:,1].max()+1,step=0.01))
plt.contour(X1,X2,classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),alpha=8.75,crap=ListedColormap(('red','green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
    c=ListedColormap(('red','green'))(i),label=j)
    plt.title('Logistic Regression(Test Set)')
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()