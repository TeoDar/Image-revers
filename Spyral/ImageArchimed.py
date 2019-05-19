#!Python3
#ImageArchimed - Выставляет исходное изображение по спирали архимеда

import os, numpy
from PIL import Image

F = round((1+numpy.sqrt(5))/2,3) #Пропорция золотого сечения
IMAGE_FILENAME = "Arh.jpg" #Название открываемого изображения
NUM_TURN = 8


Image0 = Image.open(IMAGE_FILENAME) #Записываю картинку в переменную Image0
Widht_Im, Height_Im = Image0.size #Запись размеров изображения

#if Widht_Im <= Height_Im: #Если изображение повёрнуто не горизонтально, поворачивает его
#   Image0 = Image0.rotate(90)
Xsize = [0, Widht_Im, ]
Ysize = [0, Height_Im, ]
Cycle = 0

for i in range(1,NUM_TURN): #Получаю координаты касания спирали с прямоугольником
    Xsize.append(round(int(Xsize[i] / F)))
    Ysize.append(round(int(Ysize[i] / F)))
print(Xsize," ",Ysize)
Xcor = { #Задаю эмпирически полученные координаты точек X
    0:0,
    1:Xsize[1],
    2:Xsize[1]-Xsize[2],
    3:0,
    4:Xsize[3],
    5:Xsize[1]-Xsize[2],
    6:Xsize[1]-Xsize[2]-Xsize[4],
    7:Xsize[3]+Xsize[6]
}
Ycor = { #Задаю эмпирически полученные координаты точек Y
    0:0,
    1:Ysize[2],
    2:Ysize[1],
    3:Ysize[1]-Ysize[3],
    4:Ysize[2],
    5:Ysize[2]+Ysize[4],
    6:Ysize[1]-Ysize[3],
    7:Ysize[2]+Ysize[4]
}
for i in range(NUM_TURN):
    print("{",Xcor[i], ",", Ycor[i],"}")
    NewImage = Image0.copy()
for i in range(1,NUM_TURN):
    NewImage = NewImage.resize((Xsize[i],Ysize[i]))
    Image0.paste(NewImage.rotate(i*90,expand=True),(Xcor[i],Ycor[i]))
Image0.show()