from flask import Flask, render_template, request
import re
from numpy import average
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
import pandas as pd
import datetime
from mer2 import get_url, get_data

item_url_ls=[]
item_ls=[]
# price_list=[]
# ave=0

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calc",methods=['GET','POST'])
def calculation():
    if request.method == "GET":
        return render_template('calculation.html')
    elif request.method == "POST":
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(r"C:\Users\81809\Downloads\chromedriver_win32\chromedriver.exe",options=options)
        browser.implicitly_wait(3)
        keyword = request.form['keyword'] 
        csv_date = datetime.datetime.today().strftime("%Y%m%d")
        csv_file_name = keyword +'_'+ csv_date + '.csv'
        item_url_ls=get_url(keyword,browser)
        item_ls=get_data(keyword,item_url_ls,browser)
        pd.DataFrame(item_ls).to_csv(csv_file_name)
        return render_template('calculation.html')
        

if __name__ == "__main__":
    app.run(debug=True)