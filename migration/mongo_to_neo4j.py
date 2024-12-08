import time
from pymongo import MongoClient
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# MongoDB 연결
mongo_client = MongoClient("mongodb://root:example@mongodb:27017")
mongo_db = mongo_client["mock_data"]

# Neo4j 연결 설정
NEO4J_URI = "bolt://neo4j:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "strongpassword"

# Neo4j 연결 함수 (비동기 대기)
def wait_for_neo4j_connection(uri, user, password, retries=10, delay=5):
    """
    Neo4j가 준비될 때까지 대기합니다.
    :param uri: Neo4j URI
    :param user: 사용자 이름
    :param password: 비밀번호
    :param retries: 재시도 횟수
    :param delay: 재시도 간격(초)
    :return: Neo4j driver
    """
    for i in range(retries):
        try:
            driver = GraphDatabase.driver(uri, auth=(user, password))
            # 연결 테스트
            with driver.session() as session:
                session.run("RETURN 1")
            print("Successfully connected to Neo4j!")
            return driver
        except ServiceUnavailable:
            print(f"Neo4j connection failed. Retrying in {delay} seconds... ({i + 1}/{retries})")
            time.sleep(delay)
    raise Exception("Neo4j connection failed after multiple retries.")

# Neo4j 연결
neo4j_driver = wait_for_neo4j_connection(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

# MongoDB 데이터 읽기 및 Neo4j로 전송
def migrate_data():
    users = mongo_db.users.find()
    products = mongo_db.products.find()

    with neo4j_driver.session() as session:
        # 상품 데이터 전송
        for product in products:
            session.run(
                """
                MERGE (p:Product {product_id: $product_id})
                SET p.name = $name, p.category = $category
                """,
                product_id=product["product_id"], name=product["name"], category=product["category"]
            )

        # 사용자 데이터 전송 및 관계 생성
        for user in users:
            session.run(
                """
                MERGE (u:User {user_id: $user_id})
                SET u.name = $name
                """,
                user_id=user["user_id"], name=user["name"]
            )
            for product_id in user["purchases"]:
                session.run(
                    """
                    MATCH (u:User {user_id: $user_id}), (p:Product {product_id: $product_id})
                    MERGE (u)-[:PURCHASED]->(p)
                    """,
                    user_id=user["user_id"], product_id=product_id
                )

    print("Data migration completed!")

if __name__ == "__main__":
    migrate_data()
