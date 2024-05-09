import os
import sys
import re

#import pathlib
#from pathlib import Path

#import networkx as nx
#import matplotlib.pyplot as plt

from git import Repo

cwd = os.getcwd()
print(cwd)

CODE_ROOT_FOLDER="./pokemon-showdown-master/"

if not os.path.exists(CODE_ROOT_FOLDER):
  Repo.clone_from("https://github.com/smogon/pokemon-showdown", CODE_ROOT_FOLDER)

repo = Repo(CODE_ROOT_FOLDER)

def file_path(file_name):
    return CODE_ROOT_FOLDER+file_name

def imports(file):

    def extract_import_from_line(line):
      x = re.search("^import (\S+)", line) 
      x = re.search("^from (\S+)", line) 
      return x.group(1)

    # extracts all the imported modules from a file
    lines = [line for line in open(file)]
    
    all_imports = []
    for line in lines:
        try:
            all_imports.append(extract_import_from_line(line))
        except:
            continue

    return all_imports

print(imports(file_path('server/index.ts')))