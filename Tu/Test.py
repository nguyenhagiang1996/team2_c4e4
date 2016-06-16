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
#-------------------------
app = Flask(__name__,static_url_path='')


@app.route('/')
def index():
    return render_template("index.html")

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

@app.route('/BMI_request<bmr>,<BMI>')
def BMI_request(bmr,BMI):
    return render_template('BMI_request.html',bmr=bmr,BMI=BMI)

@app.route('/BMI',methods=['GET','POST'])
def bmi():
    if request.method == 'POST':
        if request.form['gender'] == "Male":
            bm = 66.47 + (13.75  * int(request.form['weight'])) + (5.0 * int(request.form['height'])) - (6.75 * int(request.form['age']))
            BMI = int(request.form['weight']) / (int(request.form['height']) / 100) ** 2
        elif request.form['gender'] == "Female":
            bmr = 665.09 + (9.56 * int(request.form['weight'])) + (1.84 * int(request.form['height'])) - (4.67 * int(request.form['age']))
            BMI = int(request.form['weight']) / (int(request.form['height']) / 100) ** 2
        return redirect(url_for('BMI_request',bmr=bmr,BMI=BMI))
    return render_template("BMI.html" )
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
