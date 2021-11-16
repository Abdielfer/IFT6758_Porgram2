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

"""[4 points]

## Q1. Given a dataframe with housing data, perform the following preprocessing/feature engineering steps:

*   Remove the `Id` column.
*   Remove all non-numerical columns from the dataframe except `Neighborhood`.
*   
    If a column has >= 60% NaN values, remove the columns from the dataset.

    Otherwise, for numerical columns, impute those columns with the statistical median of the particular column.

*   Apply a Min Max Scaler to all the numerical features in the dataframe except `Neighborhood`.

*   Use the `DictVectorizer` to encode Neighborhood into one-hot feature representations and name these additional columns as `f0`,`f1`,`f2`..etc. to replace the `Neighborhood` column.

* Return the final dataframe.

---

## Q1. Étant donné un dataframe avec des données de logement, effectuez les étapes de prétraitement/d'ingénierie des caractéristiques suivantes :


* Supprimez la colonne `Id`.
* Supprimez toutes les colonnes non numériques de la base de données, à l'exception de `Neighborhood`.
*     Si une colonne a >= 60% valeurs NaN, supprimez les colonnes de l'ensemble de données.

     Sinon, pour les colonnes numériques, imputez à ces colonnes avec la médiane statistique de la colonne particulière.

* Appliquez un Min Max Scaler à toutes les caractéristiques numériques de la base de données, à l'exception de `Neighborhood`.

* Utilisez le `DictVectorizer` pour encoder Neighborhood en représentations one-hot de caractéristiques  et nommez ces colonnes supplémentaires comme `f0`,`f1`,`f2`..etc. pour remplacer la colonne `Neighborhood`.

* Retournez le dataframe finale.
"""

def q1(df=housing_raw):
  """
  Your solution / Votre solution
  """
  "Testing  JAKBSD;CJNAS;DC "
  df = None             
  return df

q1()

"""[4 points]

## Q2. Given a dataframe with multiple features `f0`, `f1`, ..., apply KMeans for the given values of `k` and return the value of `k` with the **least** `inertia` of the clustering and this least intertia value.


---

## Q2. Étant donné un dataframe avec plusieurs caractéristiques `f0`, `f1`, ..., appliquez KMeans pour les valeurs données de `k` et retournez la valeur de `k` avec la **plus petite** `inertia` du clustering et cette plus petite valeur d'intertie.
"""

def q2(df = cluster_data, k_values=[2,3,4,5]):
  """
  Your solution / Votre solution
  """
  best_k = None
  best_inertia = None

  return best_k, best_inertia

q2()

"""[4 points]

## Q3. Given a dataframe with housing data to predict the `SalePrice` value, return the best features (NOT `SalePrice`) using Lasso feature selection method. Use [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html?highlight=lasso#sklearn.linear_model.Lasso) and [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel) to achieve this.

* Input  : `df` - dataframe and `alpha` parameter for `Lasso`
* Return : Set (`set()`) of columns with the feature names selected by Lasso

---

## Q3. Étant donné un dataframe des données de logement pour prédire la valeur `SalePrice` (prix de vente), retournez les meilleures caractéristiques (PAS `SalePrice`) en utilisant la méthode de sélection de caractéristiques Lasso. Utilisez  [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html?highlight=lasso#sklearn.linear_model.Lasso) et [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel) pour y parvenir.

* Entrée : `df` - dataframe et paramètre `alpha` pour `Lasso`
* Retour : Ensemble (`set()`) des colonnes avec les noms des caractéristiques sélectionnées par Lasso
"""

def q3(df = housing_processed, alpha=0.1, target='SalePrice'):
  """
  Your solution / Votre solution
  """
  
  return set()

q3()

"""[4 points]

##Q4. Given a dataframe with housing data to predict the `SalePrice` value, return the average value of the validation mean squared error and `alpha` value of the **best** `Ridge` model fit in a $k$-fold Cross Validation setting based on a given set of `alpha` values (of the `Ridge` model). 
 
---

##Q4. Étant donné un dataframe avec des données de logement pour prédire la valeur `SalePrice`, retournez la valeur moyenne de l'erreur quadratique moyenne de validation et la valeur `alpha` du **meilleur** modèle `Ridge` ajusté dans une validation croisée $k$-fold basé sur une liste de valeurs `alpha` (du modèle `Ridge`). 
"""

def q4(df = housing_processed, alphas=[0.1,0.01,0.001], k=5, target='SalePrice'):
  """
  Your solution / Votre solution
  """
  best_kfold_valid_mse = None 
  best_alpha = None

  return best_kfold_valid_mse, best_alpha

q4()

"""[4 points] 

## Q5. Given a dataframe about results from a drug trial with two drugs (`drug_type` `0` and `1`) that aim to improve longevity (`life_expectancy`), use bootstrap estimation to find the confidence interval of difference in mean value of `life_expectancy` of each of these two drugs. 

* Use the pandas [`Dataframe.sample`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) function to sample with replacement, with the bootstrap sample size as the length of the source dataframe and random state passed in the function argument.
* Use `drug_type 0` - `drug_type 1`order for the difference.

**Arguments**

* `df` : a dataframe that includes observations of the two sample classes
* `variable` : the column name of the column that includes observations of the variable of interest  
* `class_name` : the column name of the column that includes group assignment (This column should contain two different group names/values)
* `num_repetitions`: number of times you want the bootstrapping to repeat. Default is 1000.
* `alpha` : likelihood that the true population parameter lies outside the confidence interval. Default is 0.05. 
* `random_state` : enable users to set their own random_state for the sampling, default is `123`. 


**Return**

* The lower limit and upper limit of the confidence interval for the difference in mean `life_expectancy` between the two drug types corresponding to the given `alpha`.


---

## Q5. Étant donné un dataframe sur les résultats d'un essai de médicament avec deux médicaments (`drug_type` `0` et `1`) qui visent à améliorer la longévité (`life_expectancy`/espérance de vie), utilisez l'estimation bootstrap de la différence pour trouver l'intervalle de confiance de la valeur moyenne de la différence de `life_expectancy` de chacun de ces deux médicaments.

* Utilisez la fonction pandas [`Dataframe.sample`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) pour échantillonner avec remplacement, avec la taille de l'échantillon bootstrap comme longueur du dataframe source et l'état aléatoire transmis dans l'argument de la fonction.
* Utilisez l'ordre `drug_type 0` - `drug_type 1` pour la différence.

**Arguments**

* `df` : un dataframe qui comprend les observations des deux classes d'échantillons
* `variable` : le nom de la colonne qui inclut les observations de la variable d'intérêt
* `class_name` : le nom de colonne de la colonne qui inclut les balises de groupe (cette colonne doit contenir deux noms/valeurs de groupe différents)
* `num_repetitions`: le nombre de fois qu'on souhaite que le bootstrapping se répète. La valeur par défaut est 1000.
* `alpha` : probabilité que le véritable paramètre de population se situe en dehors de l'intervalle de confiance. La valeur par défaut est 0,05. 
* `random_state` : pour permettre aux utilisateurs de définir leur propre état aléatoire , la valeur par défaut est `123`


**Retour**

* La limite inférieure (lower limit) et la limite supérieure (upper limit) de l'intervalle de confiance pour la différence de `life_expectancy` (espérance de vie) moyenne entre les deux types de médicaments (drugs) correspondant à l'`alpha` donné.


"""

def q5(df=drug_trials, variable='life_expectancy', class_name='drug_type', num_repetitions = 1000, alpha = 0.05, random_state=np.random.RandomState(seed=123)):
    """
    Your solution / Votre solution
    """

    return lower_limit, higher_limit

q5()

"""Packaging all the above functions into a class for the solution file to submit on Gradescope.

---

Empaqueter toutes les fonctions ci-dessus dans une classe pour le fichier de solution à remettre sur Gradescope.
"""

class Prog2:
  
  def q1(self, df=housing_raw):
    return q1(df)
  
  def q2(self, df = cluster_data, k_values=[2,3,4,5]):
    return q2(cluster_data, k_values)
  
  def q3(self, df = housing_processed, alpha=0.1, target='SalePrice'):
    return q3(df, alpha, target)

  def q4(self, df = housing_processed, alphas=[0.1,0.01,0.001], k=5, target='SalePrice'):
    return q4(df, alphas, k, target)

  def q5(self, df=drug_trials, variable='life_expectancy', class_name='drug_type', num_repetitions = 1000, alpha = 0.05, random_state=np.random.RandomState(seed=123)):
    return q5(df, variable, class_name, num_repetitions, alpha, random_state)