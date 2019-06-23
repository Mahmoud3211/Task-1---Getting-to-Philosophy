"""
@author: Mahmoud Nada
"""


import time
from bs4 import BeautifulSoup
import requests
import urllib

initial = "https://en.wikipedia.org/wiki/Special:Random"
philosophy = "https://en.wikipedia.org/wiki/Philosophy"

def extract_first_link(url):
    request = requests.get(url)
    html = request.text
    bs = BeautifulSoup(html, "html.parser")
    target_div = bs.find(id="mw-content-text")
    extracted_link = None
    for paragraph in target_div.find_all('p'):
        if paragraph.find("a"):
            extracted_link = paragraph.find("a").get('href')
            break

    if not extracted_link:
        return

    target_link = urllib.parse.urljoin('https://en.wikipedia.org/', extracted_link)

    return target_link

def search_target(links_list, target_url, max_iterations=25):
    if links_list[-1] == target_url:
        print(links_list[-1])
        print("Philosophy Article Has Been Found Successfully")
        return False
    elif len(links_list) > max_iterations:
        print("Max Iterations Over Urls has Been Exceeded Without Finding Philosophy Article")
        return False
    elif links_list[-1] in links_list[:-1]:
        print("Article is Already found once")
        return False
    else:
        return True

articles = [initial]

while search_target(articles, philosophy):
    print(articles[-1])

    first_link = extract_first_link(articles[-1])
    if not first_link:
        print("no links found in the article")
        break

    articles.append(first_link)
    time.sleep(2)

