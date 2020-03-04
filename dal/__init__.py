from flask_pymongo import PyMongo
mongo = PyMongo()
def initDb(app):
    mongo.init_app(app)
    # Created Compound text Index for name search feature
    mongo.db.users.create_index([('first_name', 'text'), ('last_name', 'text')], default_language='english')