# 베이스 이미지 설정
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치를 위한 requirements 파일 복사
COPY requirements.txt .

# Python 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 마이그레이션 스크립트 복사
COPY mongo_to_neo4j.py .

# 환경 변수 설정 (선택 사항)
# ENV MONGO_URI=mongodb://root:example@mongodb:27017/
# ENV NEO4J_URI=bolt://neo4j:strongpassword@neo4j:7687

# 마이그레이션 스크립트 실행
CMD ["python", "mongo_to_neo4j.py"]
