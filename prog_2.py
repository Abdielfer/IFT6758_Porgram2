# -*- coding: utf-8 -*-
""" Prog-2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vcadZUIBVEMLb4rkCWDiXuDCl0oUOoee

<center><h1> IFT-6758  </h1></center>
<center><h1> Data Science / Science des données  </h1></center> 
<center><h2> Fall-2021 </h2></center> 
<center><h3> Prog 2 </h3></center> 
<center><h3> </h3></center>

Deadline    : **Nov 20, 11.59 pm EDT** on [Gradescope](https://www.gradescope.com/courses/286503/assignments/1652286)

---

Date limite :  **Le 20 Nov, 23h59 HAE** sur [Gradescope](https://www.gradescope.com/courses/286503/assignments/1652286)

**Please use only the following imports.**

**DO NOT IMPORT ANYTHING OTHER THAN SUB-PACKAGES OF THESE WHEN NECESSARY.**

This is important for running you code!

---

**Veuillez utiliser uniquement les importations suivantes.**

**N'IMPORTEZ RIEN D'AUTRE DES SOUS-PACKAGES DE CEUX-CI LORSQUE NÉCESSAIRE.**

Ceci est important pour exécuter votre code!
"""

# Imports / Importations
import numpy as np
import pandas as pd

from sklearn import preprocessing

from sklearn import feature_extraction 
from sklearn import feature_selection 

from sklearn import linear_model
from sklearn import cluster

from sklearn import model_selection
from sklearn import metrics

# Sample data inits / Initialisations des exemples de données

housing_raw = pd.read_csv('https://raw.githubusercontent.com/ift-6758/files/main/housing_raw.csv')

cluster_data = pd.read_csv('https://raw.githubusercontent.com/ift-6758/files/main/cluster-data.csv')

housing_processed = pd.read_csv('https://raw.githubusercontent.com/ift-6758/files/main/housing_processed.csv')

drug_trials = pd.read_csv('https://raw.githubusercontent.com/ift-6758/files/main/drug_trials.csv')

class Prog2:
  
  def q1(self, df=housing_raw):
    def q1(df=housing_raw):
      """
      Your solution / Votre solution
      """
      df = housing_raw
      ## dicVectorizer  
      neighbours = pd.DataFrame()
      neighbours = df[['Neighborhood']]
      neighboursDict = neighbours.to_dict(orient='records')
      vectorizer = feature_extraction.DictVectorizer(sparse=False, sort = False) # no sparse matrix
      neighboursOneHot = vectorizer.fit_transform(neighboursDict) 
      classCont = df["Neighborhood"].nunique()
      colNames = []
      for i in range(classCont) :
        colNames.append("f"+str(i))
      neighborhood = pd.DataFrame(np.squeeze(neighboursOneHot), columns=colNames)

      # DF Preprocessing 
      df = df.drop(['Neighborhood'],axis=1)
      df = df.drop(['Id'],axis=1)
      df = df._get_numeric_data()
      colum = df.columns
      nanCount = 0
      n = df.shape[1]
      for i in colum:
        nanCount = df[i].isna().sum()
        if nanCount > 0: 
          if np.abs(nanCount/n)*100 >= 60: 
            df = df.drop([i],axis=1)
          else:
              mean = df[i].mean()
              df[i].fillna(mean, inplace=True)
      
      ##  Min Max
      minMax = preprocessing.MinMaxScaler()
      dfColNames = df.columns
      df[dfColNames] = pd.DataFrame(minMax.fit_transform(df[dfColNames]))
      
      # DF reconstruction ...add 'neighborhood one-hot encoded'
      df[colNames] = neighborhood
      return df
    return q1(df)
  
  def q2(self, df = cluster_data, k_values=[2,3,4,5]):
    def q2(df = cluster_data, k_values=[2,3,4,5]):
        """
        Your solution / Votre solution
        Ref: 
        https://towardsdatascience.com/k-means-clustering-from-a-to-z-f6242a314e9a
        https://blog.cambridgespark.com/how-to-determine-the-optimal-number-of-clusters-for-k-means-clustering-14f27070048f
        """
        best_k = None
        best_inertia = float('inf')
        for k in k_values:
            model = cluster.KMeans(n_clusters=k)
            model.fit(df)
            inercy = model.inertia_
            if inercy < best_inertia:
              best_inertia = inercy
              best_k = k

        return best_k, best_inertia
    return q2(cluster_data, k_values)
  
  def q3(self, df = housing_processed, alpha=0.1, target='SalePrice'):
    def q3(df = housing_processed, alpha=0.1, target='SalePrice'):
      """
      Your solution / Votre solution
      """
      y = df[target]
      X = df.drop([target],axis=1)
      # X = np.array(X)
      model = linear_model.Lasso(alpha=alpha)
      selector = feature_selection.SelectFromModel(estimator=model).fit(X, y)
      colNames = selector.feature_names_in_
      # transformed_X = selector.transform(X)
      # ans = pd.DataFrame(transformed_X.columns)
      ans = set(colNames)
      return ans
    return q3(df, alpha, target)

  def q4(self, df = housing_processed, alphas=[0.1,0.01,0.001], k=5, target='SalePrice'):
    def q4(df = housing_processed, alphas=[0.1,0.01,0.001], k=5, target='SalePrice'):
      """
      Your solution / Votre solution
      """
      y = df[target]
      X = df.drop([target],axis=1) 
      model =  linear_model.RidgeCV(alphas=alphas,cv=k).fit(X, y)
      best_kfold_valid_mse = model.score(X, y) 
      best_alpha = model.alpha_
      return best_kfold_valid_mse, best_alpha
    return q4(df, alphas, k, target)

  def q5(self, df=drug_trials, variable='life_expectancy', class_name='drug_type', num_repetitions = 1000, alpha = 0.05, random_state=np.random.RandomState(seed=123)):
    
    def q5(df=drug_trials, variable='life_expectancy', class_name='drug_type', num_repetitions = 1000, alpha = 0.05, random_state=np.random.RandomState(seed=123)):
      """
      Your solution / Votre solution
      """
      diff = np.zeros(num_repetitions)
      alphas = [(alpha/2)*100,(1 - alpha/2)*100]
      min_lim, max_lim = 0,0
      for i in range(num_repetitions):
        ith_resample = df.sample(n=df.shape[0],replace=True, random_state = random_state)
        drug_A = ith_resample.loc[ith_resample[class_name]==0]
        drug_B = ith_resample.loc[ith_resample[class_name]==1]
        diff[i] = drug_A[variable].mean() - drug_B[variable].mean()
      min_lim, max_lim = np.percentile(diff, alphas)
      return min_lim, max_lim
    return q5(df, variable, class_name, num_repetitions, alpha, random_state)


