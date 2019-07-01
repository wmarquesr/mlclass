#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Aydano Machado <aydano.machado@gmail.com>
"""
import sys

import pandas as pd
import numpy as np
import math
from random import randint
from sklearn.neighbors import KNeighborsClassifier
import requests

def euclidian_distance(element1, element2):

    sum = 0

    for i in range(0, np.size(element1, 0)):
        sum += (element1[i] - element2[i])**2

    distance = math.sqrt(sum)

    return distance

def KMeansClassifier(k, npdata):

    #Finding initial centroids.
    centroids = []
    distances = []
    label_type1 = np.array([])
    label_type2 = np.array([])
    label_type3 = np.array([])

    for i in range(0, k):
        centroids.append(randint(0, np.size(npdata, 0)))


    # label_types = np.array(centroids)
    # label_types = np.empty([1, k])

    #Assigning each xi to nearest cluster
    for i in range(0, np.size(npdata, 0)):
        distances = []
        min_dist = sys.maxsize

        for j in range(0, len(centroids)):

            distances.append(euclidian_distance(npdata[i], npdata[j]))

            if distances[j] < min_dist:
                min_dist = distances[j]

        for w in range(0, len(centroids)):
            if distances[w] == min_dist:
                if w == 0:
                    np.append(label_type1, npdata[i])
                    # print(npdata[i])
                elif w == 1:
                    np.append(label_type2, npdata[i])
                else:
                    np.append(label_type3, npdata[i])

    print(label_type1)




print('\n - Lendo o arquivo com o dataset sobre abalone')
data = pd.read_excel('abalone_dataset.xlsx')

# Criando X and y par ao algorítmo de aprendizagem de máquina.\
print(' - Criando X e y para o algoritmo de aprendizagem a partir do arquivo abalone_dataset')

# # Caso queira modificar as colunas consideradas basta algera o array a seguir.
# feature_cols = ['sex', 'length', 'diameter', 'height',
#                 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight']
# X = data[feature_cols]
# y = data.Outcome

# Ciando o modelo preditivo para a base trabalhada
print(' - Criando modelo preditivo')
# neigh = KNeighborsClassifier(n_neighbors=3)
# neigh.fit(X, y)
# discretize_data(data)

# Discretizing sex feature.
npdata = data.to_numpy()
npdata[npdata == 'M'] = 1
npdata[npdata == 'F'] = 2
npdata[npdata == 'I'] = 3

kmeans = KMeansClassifier(3, npdata)

#realizando previsões com o arquivo de
# print(' - Aplicando modelo e enviando para o servidor')
# data_app = pd.read_excel('abalone_app.xlsx')

# # Enviando previsões realizadas com o modelo para o servidor
# URL = "https://aydanomachado.com/mlclass/03_Validation.php"
#
# #TODO Substituir pela sua chave aqui
# DEV_KEY = "Machine big deep data learning vovozinha science"
#
# # json para ser enviado para o servidor
# data = {'dev_key':DEV_KEY,
#         'predictions':pd.Series(y_pred).to_json(orient='values')}
#
# # Enviando requisição e salvando o objeto resposta
# r = requests.post(url = URL, data = data)
#
# # Extraindo e imprimindo o texto da resposta
# pastebin_url = r.text
# print(" - Resposta do servidor:\n", r.text, "\n")
#
# y_pred = neigh.predict(data_app)