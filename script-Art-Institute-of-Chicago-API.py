import requests
import argparse
from fpdf import FPDF
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from progress.bar import Bar

parser = argparse.ArgumentParser()
parser.add_argument("--id")
parser.add_argument("-s","--search")
parser.add_argument("-f","--fields", action="extend", nargs="+")
parser.add_argument("-a","--artworks")
parser.add_argument("-m", "--mail")
args = parser.parse_args()

def filterAPI():
    url="https://api.artic.edu/api/v1/artworks"
    if args.id:
        url +="/"+args.id
        if args.fields:
            filteredFields=",".join(args.fields)
            url += "?fields="+filteredFields
        else:
            url += "?fields=id,title,_score,image_id"
    elif args.search:
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
    if resp.status_code==400:
        information=f"code: {resp.status_code}. -details: {resp.content}"
        raise Exception(information)
        
    
    resp = convertToList(resp)
    convertToPdf("Report",resp)
    if args.mail:
        sendEmail("Report","I attach the report",args.mail)

    

def convertToList(response):
    if(isinstance(response.json()["data"], list)):
        return response.json()["data"]
    return [response.json()["data"]]

def convertToPdf(title, content):
    pdf = FPDF("P", "mm", "Letter")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("times","",16)
    filteredFields=""
    if args.fields:
        filteredFields= ",".join(args.fields)
    pdf.cell(0, 10, title, align="C",new_x="LMARGIN", new_y="NEXT")
    bar = Bar("Generating PDF", max=len(content))
    for i in content:
        bar.next()
        for key,value in i.items():
            if "image_id" == key:
                    try:
                        pdf.cell(10, 10, link=pdf.image(f"https://www.artic.edu/iiif/2/{value}/full/843,/0/default.jpg",w = 35, h = 35,),new_x="LMARGIN", new_y="NEXT")
                    except:
                        pdf.multi_cell(180,10,"photo not avaible", new_x="LMARGIN", new_y="NEXT")                
            if key=="_score":
                if not filteredFields or "_score" in filteredFields:
                    pdf.multi_cell(180,10,str(key)+": " +str(value), new_x="LMARGIN", new_y="NEXT")
            elif key!="image_id":
                pdf.multi_cell(180,10,str(key)+": " +str(value), new_x="LMARGIN", new_y="NEXT")
        pdf.cell(180,10,"-------------------------------------------------------------------------------------", new_x="LMARGIN", new_y="NEXT")
    bar.finish()
    print("A PDF has been genereted on your local machine.")
    return pdf.output("Report.pdf")

def sendEmail(subject,text,emailReciver):
    load_dotenv()
    bar = Bar("Sending Email", max=2)

    password = os.getenv("EMAIL_PASSWORD_SENDER")
    emailSender = os.getenv("EMAIL_SENDER")
    em =EmailMessage()
    em["From"]= emailSender
    em["To"]=emailReciver
    em["Subject"]=subject
    em.set_content(text)
    with open('test.pdf', 'rb') as content_file:
        content = content_file.read()
        bar.next()
        em.add_attachment(content, maintype='application', subtype='pdf', filename='test.pdf')

    context= ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465,context=context) as smtp:
            smtp.login(emailSender, password)
            smtp.sendmail(emailSender, emailReciver,em.as_string())
            bar.next()
        print("Email sent successfully")
    except:
        print()
        print("Email not valid")
    bar.finish()
    


filterAPI()






