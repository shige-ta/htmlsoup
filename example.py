from htmlsoup import htmlsoup

soup = htmlsoup().get_html_parser("https://news.yahoo.co.jp")

# 主要ニュースのURL取得
uls = soup.find_all("li", class_="topicsListItem ")
for link_url in uls:
    url = link_url.find("a").get("href")
    print(url)

links = htmlsoup().get_all_links("https://news.yahoo.co.jp")
print(links)