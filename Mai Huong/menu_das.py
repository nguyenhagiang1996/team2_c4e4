from urllib import request  ## request de down web ve
import bs4
import pymongo

link = "https://www.facebook.com/dasdiet/photos/?tab=album&album_id=448042411940665"
uri = "mongodb://huong:123456@ds025973.mlab.com:25973/data_kcal"
client = pymongo.MongoClient(uri)
db = client.get_default_database()
db_shop = db['shop_das']

r = request.urlopen(link)  ## connect to dantri.com
html_source = r.read()  ## read html

soup = bs4.BeautifulSoup(html_source, "html.parser")

posts = soup.find_all('div', {"class":"_53s fbPhotoCurationControlWrapper fbPhotoStarGridElement fbPhotoStarGridNonStarred _53s fbPhotoCurationControlWrapper"})
for post in posts:
    title = post.a['aria-label']
    link = "https://www.facebook.com" + post.a['href']
    image = post['data-starred-src']
    db_shop.insert_one(
        {'title': title,
         'link': link,
         'image' : image
         }
    )