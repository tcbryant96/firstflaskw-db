from app import app
from flask import render_template
from app.forms import registerform
from app.models import User 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'] )
def register():
    form = registerform()
    if form.validate_on_submit():
        name = form.name.data
        phone_num = form.phone_num.data
        address= form.address.data
        new_user = User(name=name, phone_num=phone_num, address=address)
    return render_template('register.html', form=form)