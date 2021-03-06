importing essential libraries
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df = pd.read_csv('Downloads\iris.csv')
df

df.head()

df.tail()

df.isnull().sum()


Visualization
#Catplot
sns.catplot(x = 'species', hue = 'species', kind = 'count', data = df)

#Bar plot for Species Vs Petal Width
plt.bar(df['species'],df['petal_width'])

#Paired Plot
sns.set()
sns.pairplot(df[['sepal_length','sepal_width','petal_length','petal_width','species']], hue = "species", diag_kind="kde")


Data processing
df.describe()

df.columns

df.info()

df

#dropping the 'species' column
X = df.drop(['species'], axis=1)
X


Encoding the categorical feature as a one-hot numeric feature
Label_Encode = LabelEncoder()
Y = df['species']
Y = Label_Encode.fit_transform(Y)
Y

df['species'].nunique()

X = np.array(X)
X

Y


Spliting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=0)
X_train

X_train.shape
(105, 4)
X_test.shape
(45, 4)
Y_test.shape
(45,)
Y_train.shape
(105,)


Model Preparation
KNN Algorithm

#training the model
from sklearn.preprocessing import StandardScaler
standard_scaler = StandardScaler().fit(X_train)
X_train_std = standard_scaler.transform(X_train)
X_test_std = standard_scaler.transform(X_test)

X_train_std

Y_train

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_std,Y_train)


predict_knn=knn.predict(X_test_std)
accuracy_knn=accuracy_score(Y_test,predict_knn)*100

accuracy_knn


K mean Clustering
df

color_map=np.array(['Red','green','blue'])
figure=plt.scatter(df['petal_length'],df['petal_width'],c=color_map[Y],s=30)

X

from sklearn.cluster import KMeans
k_means =KMeans(n_clusters=3,random_state=2, n_jobs=4)
k_means.fit(X)

y_k_means = k_means.fit_predict(X)

centers = k_means.cluster_centers_

centers

color_map=np.array(['Red','green','blue'])

labels=np.array(['Iris-setosa','Iris-virginica','Iris-versicolour'])
figure=plt.scatter(df['petal_length'],df['petal_width'],c=color_map[k_means.labels_],s=20)


Decision Tree
X_train.size

Y_train.size

from sklearn import tree
D_tree = tree.DecisionTreeClassifier()
D_tree.fit(X_train,Y_train)

pred_tree=D_tree.predict(X_test)
accuracy=accuracy_score(Y_test,pred_tree)*100

accuracy
