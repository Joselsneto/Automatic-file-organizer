from os import listdir
from os.path import isfile, join
import shutil
import json
import time

def getFiles(path):
  files = [f for f in listdir(path) if isfile(join(path, f))]
  return files

def getRules():
  with open('rules.json') as json_file:
    rules = json.load(json_file)
    return rules

def organizeByExtension(files, rules, source):
  for f in files:
    extensions = f.split('.')
    if(len(extensions) == 1):
      continue
    extension = extensions[-1]
    moveTo = ''
    try:
      moveTo = rules[extension]
    except:
      continue    
    sourcePath = source + f
    destinationPath = moveTo + f
    new_path = shutil.move(sourcePath, destinationPath)
    print(new_path)

def mapRules(rules):
  r = {}
  for rule in rules['rules']:
    for e in rule['extensions']:
      r[e] = rule['moveTo']
  return r

def fileOrganizer():
  rules = getRules()
  files = getFiles(rules['source'])
  organizeByExtension(files, mapRules(rules), rules['source'])

if __name__ == "__main__":
  while(True):
    fileOrganizer()
    time.sleep(10)