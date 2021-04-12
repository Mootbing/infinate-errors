import ctypes
import os
from tkinter import messagebox
import sys
from threading import Thread
import tkinter as tk
import MessageBox
import time

Texts = []
Windows = []
Threads = []

try:
    with open("SampleText.txt") as f:
        Texts = f.readlines()
except:
    raise SystemExit("Text file died, reclone repo or smth")

def MakeNewVirusWindow(IntParam):
    virus = MessageBox.MessageBox(tk.Toplevel(), str(round((IntParam/len(Texts)) * 100)) + "%", Texts[IntParam], IntParam)


def SetEverythingUp():
    for i in range(len(Texts)):
        x = Thread(target=lambda : [MakeNewVirusWindow(i)])
        x.start()
        Threads.append(x)

if __name__ == "__main__":
    SetEverythingUp()