# manage.py
from app import app, db  # Import app and db from your app.py file

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create all database tables
    app.run(debug=True)   # Run the Flask application
