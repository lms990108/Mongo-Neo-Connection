FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 스크립트 복사
COPY insert_mock_data.py .

# 스크립트 실행을 기본 명령어로 설정
CMD ["python", "insert_mock_data.py"]
