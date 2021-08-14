import pymongo
import warnings

warnings.filterwarnings("ignore")

uri = "mongodb://localhost:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&3t.uriVersion=3&3t.connection.name=localhost&3t.alwaysShowAuthDB=true&3t.alwaysShowDBFromUserRole=true"
client = pymongo.MongoClient(uri)
db = client.sample_mflix
print("collection_name: ", db.collection_names())
countries = ['Kosovo']
query = {"countries": {"$in": countries}}
print("query ==> ", query)
res = db.movies.find(query, projection={"title": 1})
for doc in res:
    print(doc)

# print(db.count_documents({}))
# result = db.find({""})
# for doc in db:
#     print(doc)