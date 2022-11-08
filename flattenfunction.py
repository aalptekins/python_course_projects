"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı 
listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

given_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

empty_list= []

def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            empty_list.append(i)

flatten(given_list)

print(empty_list)