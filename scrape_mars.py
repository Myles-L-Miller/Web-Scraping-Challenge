from splinter import Browser
from bs4 import BeautifulSoup as Soup
import time
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    URL="https://mars.nasa.gov/news/"
    browser.visit(URL)
    time.sleep(1)
    html=browser.html
    News_Soup=Soup(html, "html.parser")
    News_Title=News_Soup.find_all("div", class_="content_title")
    News_Title=News_Title[1].get_text()
    News_Title

    News_Para=News_Soup.find_all("div", class_="article_teaser_body")
    News_Para=News_Para[0].get_text()
    News_Para

    ImageURL="https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(ImageURL)
    time.sleep(1)
    browser.links.find_by_partial_text("FULL IMAGE").click()
    html=browser.html
    Image_Soup=Soup(html, "html.parser")
    Image=Image_Soup.find_all("img", class_="fancybox-image")[0]["src"]
    Image


    Featured_Image="https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/"+Image
    Featured_Image
    DF=pd.read_html("https://space-facts.com/mars/")[0]
    DF

    Data={
        "News_Title":News_Title, 
        "News_Para": News_Para,
        "Featured_Image": Featured_Image,
        "Mars_Facts": DF.to_html()
    }
    return Data