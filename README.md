# 프로젝트: MongoDB에서 Neo4j로 데이터 마이그레이션

## 개요

이 프로젝트는 MongoDB에 저장된 **상품-사용자 구매 데이터**를 Neo4j로 Migration하여 Graph DB 학습과 활용 방안에 대한 경험을 목표로 함.

Docker Compose를 사용하여 MongoDB와 Neo4j 컨테이너를 관리하며, Python 스크립트를 통해 데이터를 Mocking 및 Migration, 관계를 생성합니다. 추후 Hadoop과 같은 대규모 데이터 처리 도구의 활용 가능성도 염두에 두고 프로젝트를 설계하였습니다.

---

## 프로젝트 구조

```
hadooppractice/
├── mongodb/
│   ├── Dockerfile
├── neo4j/
│   ├── Dockerfile
├── python-app/
│   ├── Dockerfile
│   ├── insert_mock_data.py  # MongoDB에 데이터를 추가하는 스크립트
│   ├── mongo_to_neo4j.py    # Neo4j로 데이터를 마이그레이션하는 스크립트
│   ├── requirements.txt
├── docker-compose.yml
```

---

## 주요 기능

1. **Mock 데이터 삽입**:

   - `insert_mock_data.py` 스크립트를 통해 MongoDB에 사용자와 상품 Mock Data를 생성 및 추가

2. **Neo4j로 마이그레이션**:

   - `mongo_to_neo4j.py`를 사용하여 MongoDB에서 데이터를 읽고 Neo4j에 노드와 관계를 생성
   - 구매 데이터를 중심으로 사용자와 상품 간의 관계를 그래프 데이터베이스로 전환하여 관계 기반 분석의 토대 마련

3. **Docker 기반 환경 설정**:

   - Docker Compose를 사용하여 MongoDB와 Neo4j 컨테이너를 간편하게 관리 및 실습

---

## 실행 방법

### 1. 요구사항 설치

- Docker 및 Docker Compose 필요.

### 2. Docker Compose 실행

```bash
# 프로젝트 디렉토리에서 실행
$ docker-compose up --build
```

- 위 명령어는 MongoDB, Neo4j, 데이터 삽입 스크립트(`data-seed`), 마이그레이션 스크립트(`migration`) 컨테이너를 실행

### 3. 데이터 마이그레이션 확인

- Neo4j 브라우저에 접속하여 데이터와 관계를 확인 가능

  - URL: [http://localhost:7474](http://localhost:7474)
  - 기본 로그인 정보:
    - 사용자 이름: `neo4j`
    - 비밀번호: `strongpassword`

- 다음 쿼리를 실행하여 데이터와 관계를 확인:

```cypher
MATCH (n) RETURN n LIMIT 10;
```

---

## 참고 사항

- Neo4j 컨테이너의 시작 시간이 느린 경우, Migration 스크립트가 먼저 실행되어 에러가 발생할 수 있어 Migration 진행 전 Neo4j 실행을 보장하는 지연 및 대기 로직 포함.

- `docker-compose.yml`에 정의된 환경 변수들을 필요에 맞게 수정하여 MongoDB 및 Neo4j의 설정을 변경가능

---

## 기술 스택

- **데이터베이스**: MongoDB, Neo4j
- **스크립트 언어**: Python
- **컨테이너**: Docker, Docker Compose

---

## 향후 개선 방향

1. 데이터 마이그레이션 과정에 대한 로그 추가.
2. 비동기 처리 또는 재시도 메커니즘 도입으로 안정성 향상.
3. Hadoop 같은 대규모 데이터 처리 도구를 활용하여 확장성 향상.
4. 특정 도메인(예: 추천 시스템, 소셜 네트워크)에서 Neo4j의 이점을 극대화할 수 있는 데이터 모델 개선.

---

## 실행 결과

- 아래는 Neo4j 브라우저에서 확인한 데이터 시각화 결과
