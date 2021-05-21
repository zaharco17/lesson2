# практика (сравнение строк)
def st (a, b):
 if type(a )!=str or type( b ) !=str:
  return 0
 elif len(a )== len(b):
  return  1
 elif len(a ) > len(b) and a != 'learn' and  b != 'learn':
  return  2
 elif len(a) != len(b) and (a == 'learn' or b == 'learn'):
  return 3
 else:
  return '1я строка меньше 2й'

#проверка с различными значениями 
for i in range(3):
 a = input(' a = ')
 b = input('b = ')
 c = st (a, b)
 print (c)