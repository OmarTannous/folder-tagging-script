import os, sys

print("drag the folder into the window and press enter")
name = input()

name = name.strip('\"')

name = name[(name.rfind('\\') + 1):]

os.rename(name, "++ " + name)
