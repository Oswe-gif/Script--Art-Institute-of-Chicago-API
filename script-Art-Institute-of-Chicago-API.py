import requests
import argparse
from fpdf import FPDF
import json

parser = argparse.ArgumentParser()
#parser.add_argument("--id")
parser.add_argument("-s","--search")
parser.add_argument("-f","--fields", action="extend", nargs="+")
parser.add_argument("-a","--artworks")
parser.add_argument("-m", "--mail")
args = parser.parse_args()

def filterAPI():
    url="https://api.artic.edu/api/v1/artworks"
    if args.search:
        url += "/search?q=" +args.search
        if args.fields:
            filteredFields=",".join(args.fields)
            url += "&fields="+filteredFields
        else:
            url += "&fields=id,title,_score,image_id"
    else:
        if args.fields:      
            filteredFields=",".join(args.fields)
            url += "?fields=" +filteredFields
        else:
            url += "?fields=id,title,_score,image_id"
    if args.artworks:
        url += "&limit="+args.artworks

    resp = requests.get(url)
    
    resp = convertToList(resp)
    convertToPdf("Reporte",resp)

    

def convertToList(response):
    if(isinstance(response.json()["data"], list)):
        return response.json()["data"]
    return [str(response.json()["data"])]

def convertToPdf(title, content):
    pdf = FPDF("P", "mm", "Letter")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("times","",16)
    filteredFields= ",".join(args.fields)
    pdf.cell(0, 10, title, align="C",new_x="LMARGIN", new_y="NEXT")
    for i in content:
        for key,value in i.items():
            if key=="_score":
                if "_score" not in filteredFields:
                    pass
                else:
                    pdf.multi_cell(180,10,str(key)+": " +str(value), new_x="LMARGIN", new_y="NEXT")
            else:
                pdf.multi_cell(180,10,str(key)+": " +str(value), new_x="LMARGIN", new_y="NEXT")

            print(key)
        pdf.cell(180,10,"-------------------------------------------------------------------------------------", new_x="LMARGIN", new_y="NEXT")

    return pdf.output("test.pdf")

    
filterAPI()




