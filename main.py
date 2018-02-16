class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
	from git import Repo as REPO
	from bs4 import BeautifulSoup as BS
except ImportError:
	print("{0}One or more dependencies are missing! Please make sure that you have installed all the dependencies, before start cloning!".format(colors.FAIL), colors.ENDC)
with open("manifest.xml", "r") as file:
	try:
		file = open("manifest.xml", "r")
		manifest = BS(file, 'xml')
		urls = manifest.select("repo")
		for i in range(len(urls)):
			URL = urls[i]
			REPO.clone_from(URL['url'], URL['path'])
	except FileNotFoundError:
		print(colors.FAIL, "No input file found! Please see the", colors.OKBLUE, "manifest.xml.tempelate", colors.ENDC, colors.FAIL, "file and modify it according to your own use and put that file with name manifest.xml in the same directory, where this script is! :)", colors.ENDC, colors.ENDC)
