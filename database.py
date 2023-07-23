from pymongo import MongoClient
client = MongoClient('mongodb+srv://rajaniamin:2LhEZThNmHaH4rPc@cluster0.kbn2b4w.mongodb.net/')
db = client['PROJECTJENNY']
user = db['users']
projects=db['projects']
tasks=db['tasks']
resource=db['resources']
activeUser=db['activeUser']
count=db['counter']