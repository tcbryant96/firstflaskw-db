from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import AddressForm, ProvideForm, SignUpForm, LoginForm, PhoneForm, ProvideForm
from app.models import User, Address, Number
from flask_login import login_user, logout_user, login_required, current_user



@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
           flash('A User with that username or email already exist.', 'danger') 
           return redirect(url_for('signup'))
        new_user = User(email=email, username=username, password=password)
        flash(f"{new_user.username} has been created.", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/address', methods= ["Get", "Post"])
@login_required
def view_address():    
    addresses= Address.query.filter_by(user_id=current_user.id)
    return render_template('address.html', addresses=addresses)

@app.route('/create', methods = ["GET", "POST"])
@login_required
def create():
    form= AddressForm()
    if form.validate_on_submit():
        address = form.address.data
        apartment = form.apartment.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip = form.zip.data
        new_address = Address(address=address, apartment=apartment, city=city, state=state, country=country, zip=zip, user_id=current_user.id)
        flash(f'{new_address.address} has been created.', 'secondary')
        return redirect(url_for('view_address'))
    return render_template('createaddress.html', form=form)

@app.route('/login', methods= ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
             login_user(user)
             flash(f'welcome back {user.username}!', 'success')
             return redirect(url_for('index'))
        else:
            flash('Username or password is incorrect. Please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form =form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have succesfully logged out.', "success")
    return redirect(url_for('index'))




@app.route('/address/<address_id>/edit', methods = ["GET", "Post"])
@login_required
def edit_address(address_id):
    address_to_edit= Address.query.get_or_404(address_id)
    if address_to_edit.author != current_user:
        flash("You do not have permission to edit this address", "danger")
        return redirect(url_for('view_address'))
    form = AddressForm()
    if form.validate_on_submit():
        address = form.address.data
        apartment = form.apartment.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip = form.zip.data
        address_to_edit.update(address=address, apartment=apartment, city=city, state=state, country=country, zip=zip, user_id=current_user.id)
        flash(f"{address_to_edit.address} has been updated", "success")
        return redirect(url_for('view_address'))
    return render_template('edit_address.html', address=address_to_edit, form=form)


@app.route('/address/<address_id>/delete')
@login_required
def delete_address(address_id):
    address_to_delete = Address.query.get_or_404(address_id)
    if address_to_delete.author != current_user:
        flash("You don't have permission to delete this address", 'danger')
        return redirect(url_for('index'))
    address_to_delete.delete()
    flash(f"{address_to_delete.address} has been deleted", 'secondary')
    return redirect(url_for('view_address'))

@app.route('/phonebook',  methods = ["GET", "Post"])
@login_required
def phone_book():
    numbers= Number.query.filter_by(user_id=current_user.id)
    return render_template('phone_book.html', numbers=numbers)

@app.route('/phonebook/add',  methods = ["GET", "Post"])
@login_required
def add_num():
    form = PhoneForm()
    if form.validate_on_submit():
        number= form.number.data
        provider= form.provider.data
        provided_to= form.provided_to.data
        new_num = Number(number=number, provider=provider, provided_to= provided_to, user_id= current_user.id)
        flash(f'{new_num.number} has been created.', 'secondary')
        return redirect(url_for('phone_book'))
    return render_template('add_num.html', form=form)

@app.route('/phonebook/<phone_id>/edit', methods = ["GET", "Post"])
@login_required
def edit_phone_num(phone_id):
    num_to_edit= Number.query.get_or_404(phone_id)
    if num_to_edit.author != current_user:
        flash("You do not have permission to edit this number", "danger")
        return redirect(url_for('index'))
    form = PhoneForm()
    if form.validate_on_submit():
        number= form.number.data
        provider= form.provider.data
        num_to_edit.update(number=number, provider=provider, user_id=current_user.id)
        flash(f"{num_to_edit.number} has been updated", "secondary")
        return redirect(url_for('phone_book'))
    return render_template('edit_num.html', number=num_to_edit, form=form)

@app.route('/phonebook/<phone_id>/delete')
@login_required
def delete_num(phone_id):
    num_to_delete = Number.query.get_or_404(phone_id)
    if num_to_delete.author != current_user:
        flash("You don't have permission to delete this number", 'danger')
        return redirect(url_for('index'))
    num_to_delete.delete()
    flash(f"{num_to_delete.number} has been deleted", 'secondary')
    return redirect(url_for('phone_book'))

@app.route('/phonebook/<phone_id>/provide_to')
@login_required
def add_provide_to(phone_id):
    num_provide_to =Number.query.get_or_404(phone_id)
    if num_provide_to.author != current_user:
        flash("You don't have permission to edit this number", 'danger')
        return redirect(url_for('index'))
    form= ProvideForm()
    if form.validate_on_submit:
        number=number.data
        provider=provider.data
        provided_to= provided_to.data
        new_num = Number(number=number, provider=provider, provided_to= provided_to, user_id= current_user.id)
        flash(f'{new_num.provided_to} has been added to {new_num.number}.', 'secondary')
        return redirect(url_for('phone_book'))
    return render_template('provide_to.html', number=num_provide_to, form=form)
