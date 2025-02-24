# -*- coding: utf-8 -*-
"""Breast_Cancer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qVA13sBU6wiGcyYUUgpgOg6F_AiQ1tmT
"""

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from google.colab import files
import numpy as np
import pandas as pd
import joblib

#divindo o conjunto de dados
breast_cancer = load_breast_cancer()
X, y = breast_cancer.data, breast_cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#exibindo os dados de forma tabular

data = pd.DataFrame(data=X, columns=breast_cancer.feature_names)
data["target name"] = pd.Categorical.from_codes(y, breast_cancer.target_names)
data["target"] = y
data.head()

#instanciando e treinando o modelo e o scaler

scaler = StandardScaler()
svmModel = SVC(kernel="rbf", C=1.0, gamma="auto")

X_train_scaled = scaler.fit_transform(X_train) #normalizando os dados
X_test_scaled = scaler.transform(X_test)

svmModel.fit(X_train_scaled, y_train)

#testando e validando o modelo
y_pred = svmModel.predict(X_test_scaled)
resultados = classification_report(y_test, y_pred)
print(resultados)

#salvando o modelo

joblib.dump(scaler, "scalerBreastCancer.pkl")
joblib.dump(svmModel, "svmBreastCancer.pkl")
files.download("scalerBreastCancer.pkl")
files.download("svmBreastCancer.pkl")