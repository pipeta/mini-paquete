from bs4 import BeautifulSoup

import requests

import pandas as pd

def scrap_t13():
    """Datos de la pagina t13 seccion reportajes
    
    Muestra informacion del titulo del reportaje y el link del video 
    
    """
    
    list_text = list()
    
    list_href = list()

    url = "https://www.t13.cl/reportajest13"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    content = soup.find("div", {"id": "reportajest13-more-news-list", "class": "content"})

    links = content.find_all("a", class_= "item")

    for link in links:
        
        list_href.append(link["href"])
        list_text.append(link.text)

    df = pd.DataFrame({'Titulo':list_text, 'Link':list_href},index=range(1,len(list_text)+1))
    
