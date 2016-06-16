from urllib import request  ## request de down web ve
import bs4
import pymongo

link = "http://dasdiet.vn/NewsCategory.aspx?catID=763333fd-fa73-4216-bcf6-cde6f78bd751"
uri = "mongodb://huong:123456@ds025973.mlab.com:25973/data_kcal"
client = pymongo.MongoClient(uri)
db = client.get_default_database()
db_recipes = db['carb_recipes']

r = request.urlopen(link)  ## connect to dantri.com
html_source = r.read()  ## read html

soup = bs4.BeautifulSoup(html_source, "html.parser")

storyCats = soup.find_all("div", {"class" : "storyCat"})
for storyCat in storyCats:
    photoCat = storyCat.find('a', {"class" : "photoCat"})
    link = "http://dasdiet.vn/" + storyCat.a['href']
    # print(link)
    image = photoCat.img['src']
    # print(image)
    titleCat = storyCat.find('a', {"class" : "titleCat"})
    title = titleCat.string
    # print(title)
    summaryCat = storyCat.find('div', {"class" : "summaryCat"})
    summary = summaryCat.string
    # print(summary)
    # print('-----------------')
    db_recipes.insert_one(
                {'title': title,
                 'link': link,
                 'img': image,
                 'summary' : summary
                 }
    )


