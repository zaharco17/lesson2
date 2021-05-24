'''
Создать список из словарей с оценками учеников разных классов школы вида
 [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
'''

cl1 = {'class': '1a', 'scores': [3,4,5,5,2]}
cl2 = {'class': '2a', 'scores': [4,5,3,5,1]}
cl3 = {'class': '3a', 'scores': [3,5,1,5,2]}
cl4 = {'class': '4a', 'scores': [4,5,5,5,2]}

sc = [cl1, cl2, cl3, cl4]

for i in range(len(sc)):
        sm = sum(sc[ i ]['scores']) 
        d = len(sc[ i ]['scores'])
        sredn = sm / d
        print(sredn)