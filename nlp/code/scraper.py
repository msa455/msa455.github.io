from lxml import html
import requests
import pickle

bible = 'http://ogden.basic-english.org/bbe/bbe.html'
chapters = []

page = requests.get(bible)
tree = html.fromstring(page.content)
x = tree.xpath('//table/tr/td/text()')
for a in x:
    b = a.strip()
    if b == 'Genesis':
        switch_pos = len(chapters)
    if b != "" and b!='|' and b not in chapters:
        if ',' not in b:
            chapters.append(b)
        else:
            cc = b.split()[0].split(',')
            name = ' '.join(b.split()[1:])
            for c in cc:
                chapters.append(c + " " + name)

chapters = chapters[switch_pos:] + chapters[:switch_pos]
aux = chapters[20]
chapters[20] = chapters[21]
chapters[21] = aux

x = tree.xpath('//table/tr/td/a')
links = []
for a in x:
    try:
        b = a.attrib['href'].strip().split("#")[0].split("$")[0]
        if b == 'bbegen1.html':
            switch_pos = len(links)-1
        if b not in ['bbe.html'] and b not in links:
            links.append(b)
    except:
        continue

links = links[switch_pos:] + links[:switch_pos]
links = links[:39] + ["bbe2samuel.html","bbe2sam9.html"] + links[39:]
aux = links[76]
links[76] = links[77]
links[77] = aux

pickle.dump(chapters,open("chapters.pk","wb"))
pickle.dump(links,open("links.pk","wb"))

links = pickle.load(open("links.pk","rb"))

for i in range(len(links)):
    link = links[i]
    page = requests.get("http://ogden.basic-english.org/bbe/" + link)
    tree = html.fromstring(page.content)
    x = tree.xpath("string()")

    if link == "bbeisaiah.html":
        x = ["1:1\n"]

    output = open("BE_Bible","a")
    for a in x:
        output.write(a)
    output.close()
    print("Scraped link",i,link,len(x))

# First 10 lines of BE_Bible need to be removed
# John's don't have verse numbers