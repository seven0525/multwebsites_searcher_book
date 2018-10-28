# !//usr/bin/env/python
# -*- coding:utf-8 -*-
from flask import Flask, render_template, redirect, request
from os.path import join, dirname, abspath, exists

import amazon_scriping as amazon_scriping
import bookoff_scriping as bookoff_scriping
import TAT_scriping as TAT_scriping

#Flaskの起動
app = Flask(__name__)

@app.route("/")
def show_toppage():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def add_user():
    title = "分析結果"
    key_word = request.form['key_word']
    if not key_word:
        return redirect('/')
    # result, result_img = analyze_books.main(my_user_name)
    amazon_1_name, amazon_2_name, amazon_3_name, amazon_4_name, amazon_5_name = amazon_scriping.main(key_word)
    bookoff_1_name, bookoff_2_name, bookoff_3_name, bookoff_4_name, bookoff_5_name = bookoff_scriping.main(key_word)
    TAT_1_name, TAT_2_name, TAT_3_name, TAT_4_name, TAT_5_name = TAT_scriping.main(key_word)
    # return render_template('index.html', title=title, result=result, result_img=result_img, my_user_name=my_user_name)
    return render_template('index.html', title=title, amazon_1_name=amazon_1_name, amazon_2_name=amazon_2_name, amazon_3_name=amazon_3_name, amazon_4_name=amazon_4_name, amazon_5_name=amazon_5_name,
    bookoff_1_name=bookoff_1_name, bookoff_2_name=bookoff_2_name, bookoff_3_name=bookoff_3_name, bookoff_4_name=bookoff_4_name, bookoff_5_name=bookoff_4_name,
    TAT_1_name=TAT_1_name, TAT_2_name=TAT_2_name, TAT_3_name=TAT_3_name, TAT_4_name=TAT_4_name, TAT_5_name=TAT_5_name)

# # if __name__ == "__main__":
# app.run(host="localhost")

if __name__ == "__main__":
    app.run(debug=True)
