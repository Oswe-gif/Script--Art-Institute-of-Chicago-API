import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--id")
parser.add_argument("-s","--search")
parser.add_argument("-f","--fields", action="extend", nargs="+")
parser.add_argument("-a","--artworks")
parser.add_argument("-m", "--mail")
args = parser.parse_args()

url="https://api.artic.edu/api/v1/artworks"

if args.id:
    url +="/"+args.id
if args.search:
    url += "/search?q=" +args.search
if args.fields:
    filteredFields=",".join(args.fields)
    if args.search:    
        url +="&fields="+filteredFields #un array
    else:
        url += "?fields=" +filteredFields #un objeto




print(url)
resp = requests.get(url)
if args.artworks: #array
    resp = resp.json()["data"][:int(args.artworks)]
    print(resp)
else: #obj
    print(resp.json()["data"])
