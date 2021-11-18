from flask import Flask, render_template, request
import sqlite3

# application instance Setup 
app = Flask(__name__)

# Routes to Landing Page
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':

        #connecting to database
        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        # HTML Form
        name = request.form['name']
        password = request.form['password']
        print(name, password)

        # SQL Query
        query = "SELECT name,password FROM users where name= '"+name+"' and '"+password+"' "
        cursor.execute(query)
        results = cursor.fetchall()

        # Validation
        if len(results) == 0:
            print("Sorry, Incorrect Credentials Provided. Try Again")
        else:
            return render_template("logged_in.html")
        

    return render_template('index.html')

if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True, host='0.0.0.0')