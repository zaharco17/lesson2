# практика: возраст

def  age_c (age):
 if age <= 6:
  return 'детский сад'
 elif 6 < age <= 17:
  return  'школа'
 elif 17 < age <= 23:
  return 'ВУЗ'
 else:
  return 'работа'

age = float(input('укажите свой возраст \n'))

Cotegory = age_c(age)

print('возрастная группа (',Cotegory,')')