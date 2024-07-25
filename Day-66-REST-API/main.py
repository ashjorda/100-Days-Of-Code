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


@app.route("/search")
def search_cafes():
    search_string = request.args.get('loc')
    location_results = []
    with app.app_context():
        result = db.session.execute(db.select(Cafe).where(Cafe.location == search_string)).scalars().all()
        if not result:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
        else:
            for location in result:
                cafe_attributes = {
                    'can_take_calls': location.can_take_calls,
                    'coffee_price': location.coffee_price,
                    'has_sockets': location.has_sockets,
                    'has_wifi': location.has_wifi,
                    'id': location.id,
                    'img_url': location.img_url,
                    'location': location.location,
                    'map_url': location.map_url,
                    'name': location.name,
                    'seats': location.seats
                }
                location_results.append(cafe_attributes)
            return jsonify(cafe=location_results)


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_new_cafe():
    new_cafe = Cafe(
        can_take_calls=bool(request.form.get('can_take_calls')),
        has_sockets=bool(request.form.get('has_sockets')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_toilet=bool(request.form.get('has_toilet')),
        coffee_price=request.form.get('coffee_price'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        map_url=request.form.get('map_url'),
        name=request.form.get('name'),
        seats=request.form.get('seats'),
    )
    with app.app_context():
        db.session.add(new_cafe)
        db.session.commit()
    return jsonify(response={'success': "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    with app.app_context():
        # price_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        new_price = request.args.get('new_price')
        if not new_price:
            price_to_update = db.get_or_404(Cafe, cafe_id)
            price_to_update.coffee_price = new_price
            db.session.commit()
            return jsonify({'success': "Successfully updated the price."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def cafe_closed(cafe_id):
    with app.app_context():
        api_key = request.args.get('api-key')
        # delete_cafe = db.get_or_404(Cafe, cafe_id)
        delete_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if not delete_cafe:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        elif api_key == 'TopSecretAPIKey':
            db.session.delete(delete_cafe)
            db.session.commit()
            return jsonify({'success': "Successfully deleted cafe."})
        else:
            return jsonify({'error': "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True, port=8001)
