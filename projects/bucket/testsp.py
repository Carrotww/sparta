from pymongo import MongoClient
import requests
client = MongoClient('mongodb+srv://root:1860@cluster0.8fpka1h.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

name_receive = '유형석'

user_check = db.minproject.find_one({'name': '유형석'})

print(user_check)

db.minproject.update_one({'name':f'{name_receive}'}, {'$set': {'age': 22}})
db.minproject.update_one({'name':f'{name_receive}'}, {'$set': {'address': '서울',}})
db.minproject.update_one({'name':f'{name_receive}'}, {'$set': {'hobby': 'dhobby'}})
db.minproject.update_one({'name':f'{name_receive}'}, {'$set': {'MBTI': 'EEE'}})
db.minproject.update_one({'name':f'{name_receive}'}, {'$set': {'spec': 'spec'}})
db.minproject.update_one({'name':f'{name_receive}'}, {'$set': {'style': 'style'}})
db.minproject.update_one({'name':f'{name_receive}'}, {'$set': {'blog': 'blog'}})