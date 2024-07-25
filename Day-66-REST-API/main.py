from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def cafe():
    with app.app_context():
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        random_cafe = random.choice(cafes)
        return jsonify(cafe={
            'can_take_calls': random_cafe.can_take_calls,
            'coffee_price': random_cafe.coffee_price,
            'has_sockets': random_cafe.has_sockets,
            'has_wifi': random_cafe.has_wifi,
            # 'id': random_cafe.id,
            'img_url': random_cafe.img_url,
            'location': random_cafe.location,
            'map_url': random_cafe.map_url,
            'name': random_cafe.name,
            'seats': random_cafe.seats
        })


@app.route("/all")
def all_cafes():
    with app.app_context():
        results = []
        cafe_result = db.session.execute(db.select(Cafe)).scalars().all()
        for result in cafe_result:
            cafe_attributes = {
                'can_take_calls': result.can_take_calls,
                'coffee_price': result.coffee_price,
                'has_sockets': result.has_sockets,
                'has_wifi': result.has_wifi,
                'id': result.id,
                'img_url': result.img_url,
                'location': result.location,
                'map_url': result.map_url,
                'name': result.name,
                'seats': result.seats
            }
            results.append(cafe_attributes)
        return jsonify(cafe=results)



# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True, port=8001)
