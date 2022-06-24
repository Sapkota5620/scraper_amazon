import string
import lxml
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from a_class import product_info

HEADERS = {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
}

HEADERSS = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
'Accept-Language': 'en-US en;q=0.5'}

session = HTMLSession()
URL = 'https://www.amazon.com/s?k=projector&link_code=qs&sourceid=Mozilla-search&tag=moz-us-20'




#check to see if the div has search-results and assin in place
#productTitle = soup.find('span', attrs = {'id': 'productTitle'})
#avgCustomerR = soup.find('span', attrs = {'id': 'acrCustomerReviewText'})
#product_from_user = input("What product do you want to look through?")

#find the pages of results
def get_Title(div):
    try:
        title = div.find('span', attrs = { 'class': 'a-size-medium a-color-base a-text-normal'}).string

    except:
        title = "ERROR"
    print(title)
    return title

def get_Price(div):
    price = 0.00
    try:
        prices = div.find_all("span", attrs = { 'class': "a-offscreen"}).string
        priceO = float(prices[0][1:]) 
        priceT = float(prices[1][1:]) 
        if len(prices) > 1:
           if priceO > priceT:
               price = priceT
    except:
        price = -1

    print(price)
    return price

def get_review_total(div):
    try:
        total = div.find("span", attrs = { 'class': "a-icon-alt"}).string
        total = int(total.repalce(",", ""))
    except:
        total = -1
    print(total)
    return total
def get_review_stars(div):
    try:
        review_star = div.find("span", attrs = { 'class': "a-icon-alt"}).string
    except:
        review_star = "ERROR"
    print(review_star)
    return review_star
def get_product_id(div):
    try:
        product_id = div.get("data-asin")
    except:
        product_id = "ERROR"

    print(product_id)
    return product_id
def get_sponsored_tag(div):
    try:
        sponsored = "Yes" if div.find("div", attrs = { 'class': "a-row a-spacing-micro"}) else "NO" 
 
    except:
        sponsored = "ERROR"

    print(sponsored)
    return sponsored

def get_link(div):
    ref = "https://www.amazon.com/dp/"
    try:
        link = div.find('a', attrs = { 'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        href = ref + link.get('href') 
    except:
        href = "ERROR"
    print(href)
    return href


def get_all_elements(divs):
    product = product_info()
    for div in divs:
        product.title = get_Title(div)
        product.price = get_Price(div)  
        product.reviewTotal = get_review_total(div)
        product.reviewStars = get_review_stars(div)
        product.productId = get_product_id(div)
        product.sponsoredTag = get_sponsored_tag(div)
        product.link = get_link(div)

    print("exit after getting variables")

    return product
def create_list(len):
    product_list = [product_info] * (30 * len)
    return product_list

def create_soup(url):
    webpage = requests.get(url, headers = HEADERSS)
    print(webpage.status_code)
    webpage.raise_for_status()
    soup = BeautifulSoup(webpage.content, 'lxml')
    return soup

def next_page(i):
    if i == 0:
        return URL
    
    return "https://www.amazon.com/s?k=projector&i=electronics&page={}&qid=1655496248&ref=sr_pg_1".format(i)

def  print_to_notepad(list):
    fh = open(r"C:\Users\User\PracticeCs\Web Scraping\AmazonHighRated\notes.txt", 'w')
    fh.write('{: ^55}{: ^12}{: ^13}{: ^14}{: ^12}\n'.format('Title', 'Price', 'Sponsored_Tag', 'Total_Reviews_Count', ' Review_Star'))
    for i in range(len(list)):
        fh.write(('{:55}{}{}{}{}\n'.format(list[i].title, list[i].price, list[i].sponsoredTag, list[i].reviewTotal, list[i].reviewStars)))
    fh.close

def main():
    '''
        ##Steps by Step
        1) Determine what products to find
        2) Construct a URL
        3) Create a SESSION(URL)
        4) Create a Soup with create_soup(URL)
            
            5) GO THROUGH THE ELEMENT
                5.1) FIND YOUR VARIABLES
                5.2) STORE THE VARIABLE
    '''    
    product_list = create_list(10)
    count = 0
    for i in range(2):
        divs = create_soup(next_page(i)).find_all("div",attrs = {"data-component-type" : "s-search-result"})
        product_list[i] = get_all_elements(divs)
    
    print_to_notepad(product_list)


if __name__ == '__main__':
    main()        

