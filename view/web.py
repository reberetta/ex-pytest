import sys
sys.path.append('.')

from sqlalchemy.sql.expression import true, update
from flask import Flask, render_template, request, redirect

from controllers.category_controller import CategoryController

from models.category import Category

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/category')
def category():
    category_list = CategoryController().read_all()
    for i in category_list:
        print(i.name)
    return render_template('category.html', cat=category_list)

@app.route('/category/create')
def category_create_form():
    return render_template('category_create.html')

@app.route('/category', methods=['POST'])
def category_create():
    controller = CategoryController()
    name = request.form.get('name')
    description = request.form.get('description')
    new_cat = Category(name, description)
    controller.save(new_cat)
    return redirect('/category')

@app.route('/category/update/<int:id>')
def category_update_form(id):
    cat = CategoryController().read_by_id(id)
    return render_template('category_update.html', cat=cat)

@app.route('/category/update', methods=['POST'])
def category_update():
    controller = CategoryController()
    update_cat = controller.read_by_id(int(request.form.get('id')))
    update_cat.name = request.form.get('name')
    update_cat.description = request.form.get('description')
    controller.save(update_cat)
    return redirect('/category')

@app.route('/category/delete/<int:id>')
def category_delete(id):
    controller = CategoryController()
    cat = controller.read_by_id(id)
    controller.delete(cat)
    return redirect('/category')

app.run(debug=True)