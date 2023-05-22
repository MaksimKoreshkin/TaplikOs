from playsound import playsound
import os
import shutil
from zipfile import ZipFile
import urllib
from os import listdir

temp = open("modules/MusicPlayer/download", "r")


if len(listdir("modules/MusicPlayer/music")) == 0:
	for url in temp.readlines():
		fn = url.split("/")[len(url.split("/")) - 1]


dir = listdir("modules/MusicPlayer/music")
for i in range(len(dir)):
	print(f"{i}) {dir[i]})")


playsound(f'modules/MusicPlayer/music/{dir[int(input("Введите номер для воспроизведения -  "))]}')
