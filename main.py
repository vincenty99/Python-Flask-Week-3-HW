#Week 3 HW
#We are going to us flask: https://flask.palletsprojects.com/en/2.0.x/

from flask import Flask, render_template, request
#import the flask module - this is our web server

# we want to render code in our html so we import 'render_template'
# we want to get data from the webpage and do something with it in the webserver - so we import request

#Here we create the app object - python object creation and we initalize with the names and locations of our html folder with our dynamic templates, and our static templates that dont change
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)


# Here we have all of our routes... These are the url endpoints that are associated with different functions.  By default they process GET requests


@app.route("/")
def hello_world():
    return render_template('base.html') #this returns the base.html template in the template directory


@app.route("/New York Jets", methods=['POST'])# here we explicitly call the type of webrequest this manages - A post - a post sends data with the request - it is supposed to be more secure
def go_shopping():
    data = request.form['email'] #this is how we pull form data from a post request
    #details ={name:"sdd",difficulty:'""',img:""}
    #cocktails = [{name:"",picture:""},{name:"",picture:""},]
    return render_template('nyjet.html',
      email=data, #this is how we include dynamic data with our webpage
      something="This is the 2021 NY Jet Draft Class!")




if __name__ == "__main__": 
	app.run( 
		host='0.0.0.0', 
		port=5565
	) #THIS STARTS THE WEBSERVER
