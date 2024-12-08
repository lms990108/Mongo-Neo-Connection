from pymongo import MongoClient

# MongoDB 연결 정보
MONGO_URI = "mongodb://root:example@mongodb:27017/"
client = MongoClient(MONGO_URI)
db = client["mock_data"]

# 데이터 정의
users = [
    {"user_id": "u1", "name": "Alice", "purchases": ["p1", "p3"]},
    {"user_id": "u2", "name": "Bob", "purchases": ["p2"]},
]
products = [
    {"product_id": "p1", "name": "Laptop", "category": "Electronics"},
    {"product_id": "p2", "name": "Tablet", "category": "Electronics"},
    {"product_id": "p3", "name": "Desk Chair", "category": "Furniture"},
]

# 데이터 삽입
db.users.insert_many(users)
db.products.insert_many(products)

print("Mock data inserted successfully!")
