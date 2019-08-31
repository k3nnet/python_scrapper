import requests
import bs4

#request site page by passing in url and returning a html document
def getPage():
    URL="https://www.property24.com/apartments-to-rent/midrand/gauteng/16"
    raw_page_data=requests.get(URL)
    raw_page_data.raise_for_status()
    return raw_page_data;
   

#scrape the site for property details
def scrapeSite(site):
    content=[]
    property={}
    properties=[]
    soup = bs4.BeautifulSoup(site.text,'html.parser')
    content=soup.select('.p24_content')
    #print(content)
 
    for link in content:
        print()
        print()
        print()
        property['price']=link.select('.p24_price')[0].get_text().strip()
        property['bedrooms']=link.select('span[title="Bedrooms"]>span')[0].get_text()
        properties.append(property)
    list_of_properties=(properties)

    for property in list_of_properties:
        print("price:",property.get('price'))
        print("no Bedrooms:",property.get('bedrooms'))

   
    #print(list_of_properties)
    return list_of_properties

if __name__ == "__main__":
  scrapeSite(getPage())
