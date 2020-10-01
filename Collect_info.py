from urllib import request
from bs4 import BeautifulSoup as bs
import re


def info(url):
  allContent=""
  htmlDoc=request.urlopen(url)
  soupObject=bs(htmlDoc,'html.parser')
  paraContents=soupObject.findAll('p')

  for paraContent in paraContents:
      allContent+=paraContent.text
  return allContent    
