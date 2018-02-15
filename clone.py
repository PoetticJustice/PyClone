from __future__ import print_function
from bs4 import BeautifulSoup as BS
from pygit2 import clone_repository

input = open("manifest.xml", "r")
bs = BS(input, 'lxml')
rawInput = bs.select("url")
buffer = 0
repoURL = []
for i in range(len(rawInput)):
	repoURL.append(rawInput[i].getText())

repo_path = ['common']
for j in repoURL:
	repo = clone_repository(j, repo_path[0])
