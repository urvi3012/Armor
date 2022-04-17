########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user
from __init__ import create_app, db
# import requests, tableauserverclient as TSC
# from secret import SECRET_KEY, TABLEAU_AUTH, USERS_LIST, PASSWORD_LOGIN

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from geopy.geocoders import Nominatim

#driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
########################################################################################
# our main blueprint
main = Blueprint('main', __name__)


# def getLocation():
#     options = Options()
#     options.add_argument("--use-fake-ui-for-media-stream")
#     timeout = 20
    
#     driver.get("https://mycurrentlocation.net/")
#     wait = WebDriverWait(driver, timeout)
#     time.sleep(3)
#     longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
#     longitude = [x.text for x in longitude]
#     longitude = str(longitude[0])
#     latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
#     latitude = [x.text for x in latitude]
#     latitude = str(latitude[0])
#     driver.quit()
#     return (latitude,longitude)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')    

@main.route('/result',methods=['POST']) # home page that return 'index'
def index_():
    #lat,long = getLocation()
    # geolocator = Nominatim(user_agent="MyApp")
    # coordinates = " "+" , ".join([lat,long])
    # location = geolocator.reverse(coordinates)

    # address = location.raw['address']
    text = request.form['text']
    print(text)
    return render_template('output.html', data=text)

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)



app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode