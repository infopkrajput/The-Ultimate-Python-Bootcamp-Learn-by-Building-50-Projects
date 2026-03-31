from operator import add
import random
import string
from flask import Flask, request, redirect, url_for, render_template

from methods import (
    init_db,
    insert_url,
    get_url,
    increment_visit_count,
    get_all_urls,
    delete_url
)

app = Flask(__name__)
init_db()

def generate_short_code(length=6):    
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form.get("url")
        short_code = generate_short_code()
        insert_url(original_url, short_code)
        return redirect("/")

    all_urls = get_all_urls()
    return render_template("index.html", all_urls=all_urls)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_data = get_url(short_code)
    if url_data:
        increment_visit_count(short_code)
        return redirect(url_data[1])
    else:
        return render_template("404.html")
    

@app.route('/delete/<short_code>', methods=["POST"])
def delete(short_code):
    delete_url(short_code)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
    