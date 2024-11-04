# resources.py
from flask import request, jsonify
from app import app, db
from models import Driver

@app.route('/driver', methods=['POST'])
def add_driver():
    data = request.get_json()
    new_driver = Driver(
        license=data['license'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email_id=data['email_id'],
        address=data['address']
    )
    db.session.add(new_driver)
    db.session.commit()
    return jsonify(new_driver.to_dict()), 201
