from requests_html import HTMLSession


url = 'nabled=false&preferdirects=false&ref=home&rtn=1'

s = HTMLSession()

r = s.get(url)
print()

r.html.render(sleep=1)

data = r.html.xpath('//*[@id="app-root"]/div[1]/div/div/div/div[1]/div[4]', first=True)

print(data)