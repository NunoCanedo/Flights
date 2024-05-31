from requests_html import HTMLSession


url = 'https://www.kayak.co.uk/flights/LGW-OPO/2024-05-27/2024-05-30?sort=bestflight_a&fs=stops=~0&attempt=3&lastms=1714327533800'

s = HTMLSession()

r = s.get(url)
print()

r.html.render(sleep=1)

data = r.html.xpath('//*[@id="app-root"]/div[1]/div/div/div/div[1]/div[4]', first=True)

print(data)