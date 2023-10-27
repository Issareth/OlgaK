#ПЗ-1
#Программа рисующая прямоугольный треугольник с заданной высотой

height_triangle=10 #Высота треугольника
height_counter=0 #Счётчик высоты построения

while height_counter<=height_triangle:
   n=0
   while (n<height_counter):
      print('*',end="")
      n=n+1
   print("")
   height_counter=height_counter+1
