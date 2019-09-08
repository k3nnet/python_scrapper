import requests
import bs4
import json

#request site page by passing in url and returning a html document
def getPage():
    URL="https://www.african-markets.com/en/stock-markets/jse/listed-companies"
    raw_page_data=requests.get(URL)
    raw_page_data.raise_for_status()
    return raw_page_data;
   

def toJson(data):
   # print(data)
    with open('stocks.json', 'w') as outfile:
        json.dump(data, outfile)

#scrape the site for property details
def scrapeSite(site):
    content=[]
    
    stocks=[]
    soup = bs4.BeautifulSoup(site.text,'html.parser')
    content=soup.find_all('tbody')
    print()
 
    for link in content[0].find_all('tr'):
        stock={}
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print(link.select('.ari-tbl-col-0')[0])
        stock['name']=link.select('.ari-tbl-col-0')[0].get_text()
        stock['symbol']=link.select('.ari-tbl-col-1')[0].get_text()
        stock['category']=link.select('.ari-tbl-col-2')[0].get_text()
        print(stock)
        stocks.append(stock)  
               
                
    
        
              
               
       
    print(stocks)
    return stocks;

if __name__ == "__main__":
 data= scrapeSite(getPage())
 toJson(data)
