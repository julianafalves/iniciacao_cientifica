import urllib
#import requests
from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup
import pandas as pd

'''
1. Lê a url de cada gene
2. Lê o HTML de cada pagina
3. Lê o nome e os alelos de cada snp utilizando beautifulSoup
3. Usa beautifulSoup para pegar as classes de html desejadas
4. Cria do datafreame utilizando pandas
5. Converte em csv
'''
genes = ["APOE",'BIN1','CLU','ABCA7','CR1','PICALM','MS4A6A','CD33','MS4A4E','CD2AP']
#create dataset
df = pd.DataFrame()
for x in range (len(genes)-1):
    url = "https://www.ncbi.nlm.nih.gov/snp/?term="+genes[x]+"+AND+human"
    #url = "https://pythonscraping/pages/page1.html"
    html =  urlopen(url)
    #html = requests.get(url)
    bs = BeautifulSoup(html,'html.parser')

    #let supps = document.getElementsByClassName('supp')
    supps = bs.find_all('div', class_='supp')
    #genes names
    snp_name =[]

    #for(let i=0;i<supps.length;i++)
    for i in range(len(supps)): 
        #console.log(supps[i].children[0].children[0].innerText)
        snp_name.append(supps[i].contents[0].contents[0].get_text())


    #genes alelos
    snp_alelos = []

    #let alelos = document.getElementsByClassName('snpsum_dl_left_align')
    alelos = bs.find_all('dl', class_='snpsum_dl_left_align')
    for i in range(len(alelos)):
        #console.log(alelos[i].children[3].children[0].innerText)
        snp_alelos.append(alelos[i].contents[3].contents[0].get_text())
        
#df = pd.Series(snp_name)
#df = pd.Series(snp_alelos)

teste = pd.Series({'Nome': snp_name,'Alelos':snp_alelos})
df=pd.DataFrame([teste])

df.to_csv('Juliana\Desktop\pandasfile.csv')
