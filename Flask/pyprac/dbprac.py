from pymongo import MongoClient
client = MongoClient('mongodb+srv://root:1860@cluster0.8fpka1h.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# db.users.insert_one({'name':'bobby', 'age':27})
# db.users.insert_one({'name':'john', 'age':20})
# db.users.insert_one({'name':'ann', 'age':20})

# doc = {'name':'bobby', 'age':27}
# db.users.insert_one(doc)

# all_users = list(db.users.find({}, {'_id':False}))
#
# for user in all_users:
#     print(user)

# user = db.users.find_one({'name':'bobby'})
# print(user)
# print(user['age'])

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# db.users.delete_one({'name':'bobby'})

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})