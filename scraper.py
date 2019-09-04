import requests
import bs4
import json

#request site page by passing in url and returning a html document
def getPage():
    URL="https://classybrain.com/google-my-business-categories-2018/"
    raw_page_data=requests.get(URL)
    raw_page_data.raise_for_status()
    return raw_page_data;
   

def toJson(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

#scrape the site for property details
def scrapeSite(site):
    content=[]
    property={}
    categories=[]
    soup = bs4.BeautifulSoup(site.text,'html.parser')
    content=soup.find_all('tbody')
    #print(content)
 
    for link in content:
        
        for linke in link.find_all('td'):
                categories.append(linke.get_text())
                print(categories)
       
    
    return categories;

if __name__ == "__main__":
 data= scrapeSite(getPage())
 toJson(data)
