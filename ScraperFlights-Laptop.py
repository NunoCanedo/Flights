from requests_html import HTMLSession
from bs4 import BeautifulSoup


url = 'https://www.skyscanner.net/transport/flights/lgw/opo/240519/240528/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1'

s = HTMLSession()

r = s.get(url)


r.html.render(sleep=2)

soup = BeautifulSoup(r.text)

print(soup)