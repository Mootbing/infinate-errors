import ctypes
import os
import threading

Texts = []

print(os.listdir())

try:
    with open("SampleText.txt") as f:
        Texts = f.readlines()
except:
    raise SystemExit("Text file died, reclone repo or smth")

def SetUp(Index):
    if Index + 1 >= len(Texts):
        return
    ctypes.windll.user32.MessageBoxW(0, Texts[Index], str(round((Index/len(Texts)) * 100)) + "%", 0)
    SetUp(Index + 1)

SetUp(0)