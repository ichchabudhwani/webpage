# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "ICHCHA BUDHWANI" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "VINAY BUDHWANI" # write your name
    age = "37" # write your age

    return render_template('father.html' , name = name , age = age)


# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "RESHAM BUDHWANI" # write your name
    age = "37" # write your age

    return render_template('mother.html' , name = name , age = age)


# define the route to friends webpage


# add other routes, if you want
@app.route("/sister")
def sister():

    name = "SMRITI BUDHWANI" # write your name
    age = "11" # write your age

    return render_template('sister.html' , name = name , age = age)
@app.route("/brother")
def brother():

    name = "AADESH BUDHWANI" # write your name
    age = "6" # write your age

    return render_template('friend.html' , name = name , age = age)




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
