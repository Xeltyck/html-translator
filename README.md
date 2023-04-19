# html-translator
This is an Html translator. In order to translate the Html file, BeautifulSoup and Google's Translate API are used. An Html input file is requred and strings will be hard coded in an putput file. 

```open("index.html","r",encoding="utf-8")``` - "index.html" must be replaced for the Html file name. File must be located in the script's directory.

```translate = translator.translate(x.text,src="en",dest="hi")``` - source and destination languages can be set changing the ```src="en"``` and ```"dest="hi""``` parameters. Official parameters for the supported languages can be found at [googletrans 3.0.0 documantation.](https://py-googletrans.readthedocs.io/en/latest/)

[As an example, a YouTube clone website was translated to Hindi using the script](https://xeltyck.github.io/html-translator/). 
