from flask import Flask, render_template,request,redirect,url_for
#---------------------------------- connect database lowcarb
import mongoengine
from mongoengine import Document, StringField
host = "ds025973.mlab.com"
port = 25973
db_name = "data_kcal"
user_name = "huong"
password = "123456"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

class Carb_recipes(Document):
    title = StringField()
    img = StringField()
    link = StringField()
    summary = StringField()
#-------------------------
#---------------------------------- connect database shop
import mongoengine
from mongoengine import Document, StringField
host = "ds025973.mlab.com"
port = 25973
db_name = "data_kcal"
user_name = "huong"
password = "123456"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

class Shop_das(Document):
    title = StringField()
    link = StringField()
    image = StringField()
#-------------------------
app = Flask(__name__,static_url_path='')
#----------------------- search
import pymongo
db_uri = "mongodb://huong:123456@ds025973.mlab.com:25973/data_kcal"

db = pymongo.MongoClient(db_uri).get_default_database()
kcal_collection = db['kcal']




@app.route('/')
def index():
    if request.method == 'POST':
        x = request.form['name']
        def collect_choice(x):
            data_find = kcal_collection.find({'NAME': x})
            for i in data_find:
                short_descript = print(i['SHORT_DESCRIPT'])
                traffic_light = print("Traffic_light: ", i['TRAFFIC_LIGHT'])
                carb = print("carb: ", i['CARB'])
                kcal = print("kcal: ", i['KCAL'])
            collect_choice(x.upper())
            return redirect('search',short_descript = short_descript ,traffic_light = traffic_light,carb = carb ,kcal =kcal)
        return render_template("index.html")

@app.route('/search<short_descript>,<traffic_light>,<carb>,<kcal>')
def search(short_descript,traffic_light,carb,kcal):
    return render_template("search.html",short_descript = short_descript ,traffic_light = traffic_light,carb = carb ,kcal =kcal)

@app.route('/index')
def index_return():
    return render_template("index.html")
# -------------------------------------------------
@app.route('/lowcarb')
def lowcarb():
    return render_template("lowcarb.html",data = Carb_recipes.objects)

@app.route('/shop')
def shop():
    return render_template("shop.html",data_shop = Shop_das.objects)

@app.route('/orders')
def orders():
    return render_template("orders.html")
#--------------------------------------------------BMI


@app.route('/BMI_request<bmr>,<BMI>,<calo>')
def BMI_request(bmr,BMI,calo):
    return render_template('BMI_request.html',bmr=bmr,BMI=BMI,calo=calo)

@app.route('/BMI',methods=['GET','POST'])
def bmi():
    if request.method == 'POST':
        if request.form['gender'] == "Male":
            bmr = 66.47 + (13.75  * int(request.form['weight'])) + (5.0 * int(request.form['height'])) - (6.75 * int(request.form['age']))
            BMI = int(request.form['weight']) / (int(request.form['height']) / 100) ** 2
        elif request.form['gender'] == "Female":
            bmr = 665.09 + (9.56 * int(request.form['weight'])) + (1.84 * int(request.form['height'])) - (4.67 * int(request.form['age']))
            BMI = int(request.form['weight']) / (int(request.form['height']) / 100) ** 2

        if request.form['Level of activity'] == "1":
            calo = bmr * 1.2
        elif request.form['Level of activity'] == "2":
            calo = bmr * 1.35
        elif request.form['Level of activity'] == "3":
            calo = bmr * 1.55
        elif request.form['Level of activity'] == "4":
            calo = bmr * 1.75
        elif request.form['Level of activity'] == "5":
            calo = bmr * 1.95

        return redirect(url_for('BMI_request', bmr=bmr, BMI=BMI, calo = calo))
    return render_template("BMI.html")
#--------------------------------------------------------------------


@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login',methods=['GET','POST'])#vut thuoc tinh vao day
def login():
    if request.method == 'POST':
        return redirect('/')
    return render_template("login.html")

if __name__ == '__main__':
    app.run()
