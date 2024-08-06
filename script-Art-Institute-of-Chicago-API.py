import requests
import argparse
from fpdf import FPDF
import json

def filterAPI():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id")
    parser.add_argument("-s","--search")
    parser.add_argument("-f","--fields", action="extend", nargs="+")
    parser.add_argument("-a","--artworks")
    parser.add_argument("-m", "--mail")
    args = parser.parse_args()

    urlBase="https://api.artic.edu/api/v1/artworks"
    urlSearch="https://api.artic.edu/api/v1/artworks/search?q="
    urlIDArtworks="https://api.artic.edu/api/v1/artworks/"
    #urlImage="https://www.artic.edu/iiif/2/{identifier}/full/843,/0/default.jpg"

    respSearch=""
    respID=[]
    if args.search:
        urlSearch +=args.search 
        respSearch =convertToList(requests.get(urlSearch)) #id,title,_score
        print(respSearch)
        #respSearch = convertToList(respSearch)
        for i in respSearch:
            print(i["id"])
            responseimagenURL = requests.get(urlIDArtworks+str(i["id"])).json()["data"]["image_id"]
            respID.append(responseimagenURL) # image_ids
                
    print(urlSearch)
    print(respID)


    if args.fields:
        filteredFields=",".join(args.fields)
        url += "?fields=" +filteredFields
        if args.search:
            url += "&search?q=" +args.search
        else:
            url += "&search?q=id,title,_score"
    elif args.search:
        url += "/search?q=" +args.search
    elif args.id:
        url +="/"+args.id
    else:
        url += "?fields=id,title"



    #else:
    #    url += "?fields=id,title"




    #print(url)
    resp = requests.get(url)
    resp = convertToList(resp)
    #print(resp)
    if args.artworks and not args.id:
        resp = resp.json()["data"][:int(args.artworks)]
        return convertToPdf("Reporte",resp)
    else:
        return convertToPdf("Reporte",resp)
    

def convertToList(response):
    if(isinstance(response.json()["data"], list)):
        return response.json()["data"]
    return [str(response.json()["data"])]

def convertToPdf(title, content):
    pdf = FPDF("P", "mm", "Letter")
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.add_page()
    pdf.set_font("times","",16)
    
    pdf.cell(0, 10, title, align="C",new_x="LMARGIN", new_y="NEXT")
    for i in content:
        for key,value in i.items():
            print(key)
            pdf.multi_cell(180,10,str(key)+": " +str(value), new_x="LMARGIN", new_y="NEXT")
        pdf.cell(180,10,"-------------------------------------------------------------------------------------", new_x="LMARGIN", new_y="NEXT")

    return pdf.output("test.pdf")

    
filterAPI()




