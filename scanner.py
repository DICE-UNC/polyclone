#Copyright 2014 Drexel Univeristy
from os import listdir, path
from sets import Set
import subprocess as sp
from time import sleep
import re

def read_conversions(path):
  conversions = []
  
  fin = open(path, "r")
  
  l = fin.readline()
  l = fin.readline()
  l = fin.readline()
  l = fin.readline()
  l = l.strip('\n' )
  inputs = re.split('[, \t]', l.split("#")[1])
   
  l = fin.readline()
  l = l.strip('\n' ) 
  outputs = re.split('[, \t]', l.split("#")[1])

  for i in inputs:
    for o in outputs:
      if len(i) and len(o) and i <> o:
        conversions.append([i, o])
    
  return conversions

def scan_scripts():
  for filename in listdir(scriptdir):
    scriptpath = path.join(scriptdir, filename)
    if filename[-1] == '~' or filename[0] == '.' or not path.isfile(scriptpath):
      continue

    conversions = read_conversions(scriptpath)
    if conversions:
      for conversion in conversions:
        source = conversion[0]
        target = conversion[1]
        all_target_extensions.add(target)
        newKey = source + ':' + target
        command_map[newKey] = filename
        if source in conversion_dict:
          if target not in conversion_dict[source]:
            conversion_dict[source].append(target)
        else:
          conversion_dict[source] = [target]
  for key in conversion_dict:
    sortedList = sorted(conversion_dict[key])
    conversion_dict[key] = sortedList

def scan_tests():
  files = []
  for filename in listdir(testdir):
    testpath = path.join(testdir, filename)
    if filename[-1] == '~' or filename[0] == '.' or not path.isfile(testpath):
      continue
    files.append(filename)
  return files

scriptdir = path.join(path.dirname(__file__), 'scripts')
testdir = path.join(path.dirname(__file__), 'testfiles')

all_target_extensions = Set() 
command_map = {}
conversion_dict = {}

scan_scripts()

