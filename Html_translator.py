from bs4 import BeautifulSoup
from googletrans import Translator
import re

with open("index.html","r",encoding="utf-8") as html_file: # Open file with read and write permits
    content = html_file.read()
    
    soup = BeautifulSoup(content,"html.parser") # Make use of BS4 to parse scrapped HTML.
    #body = soup.find('body')
    
    
    elements = ["p","div","title","button"] # Elements that must be replaced on the HTML file. 
    
    #Translation stage - Make use of Google API and "html.parser"
    translator = Translator()
    for x in soup.find_all(elements):
        #print(x)
        try:
            translate = translator.translate(x.text,src="en",dest="hi")
            x.string.replace_with(translate.text)
            print(translate.text)
        except:
            continue
        #print(x.text)
translated_html = open("translated.html","w",encoding="utf-8") #Make use of encoding="utf-8" to get no error when handling Hindi.
translated_html.write(str(soup))
translated_html.close()