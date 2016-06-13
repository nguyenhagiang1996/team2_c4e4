from flask import Flask, render_template,request,redirect
app = Flask(__name__,static_url_path='')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def index_return():
    return render_template("index.html")

@app.route('/resturants')
def resturants():
    return render_template("resturants.html")

@app.route('/BMI',methods=['GET','POST'])
def bmi():
    if request.method == 'POST':
        print(request.form['render'])
        if request.form['render'] == request.form['male']:
            bmr = 66.47 + (13.75  * int(request.form['weight'])) + (5.0 * int(request.form['height'])) - (6.75 * int(request.form['age']))
            print(bmr)
        elif request.form['render'] == request.form['female']:
            bmr = 665.09 + (9.56 * int(request.form['weight'])) + (1.84 * int(request.form['height'])) - (4.67 * int(request.form['age']))
            print(bmr)
        return redirect('/resturants')
    return render_template("BMI.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login',methods=['GET','POST'])#vut thuoc tinh vao day
def login():
    if request.method == 'POST':
        print("username is: ",request.form['username'])
        print("password is: ",request.form['password'])
        return redirect('/')
    return render_template("login.html")

if __name__ == '__main__':
    app.run()
