import urllib.request as req


def getData(url):
    requset = req.Request(
        url,
        headers={
            "Cookie":
            "over18=1",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        })

    with req.urlopen(requset) as response:
        data = response.read().decode("utf-8")

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")

    titles = root.find_all("div", class_="title")

    for title in titles:
        info = []
        if title.a != None:
            info.append(title.a.string)

            like_count_parent = title.find_previous_sibling("div",
                                                            class_="nrec")
            like_count1 = like_count_parent.find("span", class_="hl f2")
            like_count2 = like_count_parent.find("span", class_="hl f3")

            if like_count1 != None:
                info.append(like_count_parent.span.string)
            elif like_count2 != None:
                info.append(like_count_parent.span.string)
            else:
                info.append("0")

            articleURL = "https://www.ptt.cc" + title.a["href"]
            requset2 = req.Request(
                articleURL,
                headers={
                    "Cookie":
                    "over18=1",
                    "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
                })

            with req.urlopen(requset2) as response2:
                data2 = response2.read().decode("utf-8")
            root2 = bs4.BeautifulSoup(data2, "html.parser")

            upper_tag = root2.find("span",
                                   class_="article-meta-tag",
                                   string="時間")

            if upper_tag != None:
                wanted_tag = upper_tag.find_next_sibling(
                    "span", class_="article-meta-value")
                if wanted_tag != None:
                    info.append(wanted_tag.string)
                else:
                    info.append("")
                file.write(", ".join(info) + "\n")

    nextLink = root.find("a", string="‹ 上頁")

    return nextLink["href"]


with open("article.csv", "w", encoding="utf-8") as file:
    pageURL = "https://www.ptt.cc/bbs/Lottery/index.html"
    count = 0
    while count < 3:
        pageURL = "https://www.ptt.cc" + getData(pageURL)
        count += 1
