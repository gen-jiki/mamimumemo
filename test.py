import os
import time
import random

def speak(moji):
  os.system('cls')
  print(moji)
  time.sleep(0.5)

speak("Hello, world!")
speak("I'm gen-jiki.")
speak("End.")

hoge = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
huga = ["□","■"]
piyo = ""
player = {"x":0, "y":0}
hoge[player["y"]][player["x"]]=1

for k in range(30):
  piyo=""
  hoge = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  player["x"]=random.randrange(4)
  player["y"]=random.randrange(4)
  hoge[player["y"]][player["x"]]=1
  for i in range(len(hoge)):
    for j in range(len(hoge[i])):
      piyo+=huga[hoge[i][j]]
    piyo+="\n"
  speak(piyo)