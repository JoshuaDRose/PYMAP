import subprocess as sp
try:
  sp.run(['pip', 'install', '-r', 'requirements.txt'])
  print("Everything has been installed. Please run the __main__.py file either directly or from the command prompt")
except:
  print("Please install python 3 and ensure that pip is on your system path then re-run this program")
  print("Executable cannot be made on this project as it requires external assets such as png files which do not work with python in py2exe module")
  input()
