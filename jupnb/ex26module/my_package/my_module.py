# my_module.py
print('Module! in my_module.py')
def summ(a,b):
  return a + b
def diff(a,b):
  return a - b

if __name__ == '__main__':
  print('Programm!')
  print('print from m_module.py as from programm')
  a=5
  b=7
  print('{} + {} = {}'.format(a,b,summ(a,b)))
  print('{} - {} = {}'.format(a,b,diff(a,b)))