from os import listdir
from os.path import isfile, join
import shutil
import json
import time
import re

def getFiles(path):
  files = [f for f in listdir(path) if isfile(join(path, f))]
  return files

def getRules():
  with open('rules.json') as json_file:
    rules = json.load(json_file)
    return rules

def moveFiles(sourcePath, destinationPath):
  new_path = shutil.move(sourcePath, destinationPath)
  print(new_path)

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
    moveFiles(sourcePath, destinationPath)

def organizeByRegex(files, rules, source):
  for f in files:
    for r in rules:
      x = re.search(r[0], f)
      if(x == None):
        continue
      sourcePath = source + f
      destinationPath = r[1] + f
      moveFiles(sourcePath, destinationPath)

def mapRules(rules):
  extensionRules = {}
  regexRules = []
  for rule in rules['rules']:
    try:
      for e in rule['extensions']:
        extensionRules[e] = rule['moveTo']
    except:
      regexRules.append([rule['regex'], rule['moveTo']])      
  return extensionRules, regexRules

def fileOrganizer():
  rules = getRules()
  files = getFiles(rules['source'])
  extensionRules, regexRules = mapRules(rules)
  organizeByRegex(files, regexRules, rules['source'])
  organizeByExtension(files, extensionRules, rules['source'])

if __name__ == "__main__":
  while(True):
    fileOrganizer()
    time.sleep(10)