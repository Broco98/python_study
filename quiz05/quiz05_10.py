import os

os.chdir('C:\doit')
os.system('dir')
f = os.popen('dir')
print(f.read())

