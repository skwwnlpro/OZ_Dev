# - **[Mongo DB] 5문제 풀기**

#     **[문제 1: 특정 장르의 책 찾기]**

#     - **문제 설명**:
#     데이터베이스에 새로운 필드로 **`genre`**를 책 데이터에 추가하였습니다. 사용자는 "fantasy" 장르의 모든 책을 찾고 싶어합니다.
#     - **쿼리 작성 목표**:
#     "fantasy" 장르에 해당하는 모든 책의 제목과 저자를 찾는 MongoDB 쿼리를 함수로 만들어 문제를 해결해 봅니다.
collection = db["books"]


def book_find(db, genre):
    book_collection = db.books
    query = {"genre": genre}
    genre_component = {"_id": 0, "title": 1, "author": 1}

    books = book_collection.find(query, genre_component)
    for i in books:
        print(i)


book_find(db, "fantasy")


#     **[문제 2: 감독별 평균 영화 평점 계산]**

#     - **문제 설명**:
#     각 영화 감독별로 그들의 영화 평점의 평균을 계산하고 싶습니다. 이를 통해 어떤 감독이 가장 높은 평균 평점을 가지고 있는지 알아볼 수 있습니다.
#     - **쿼리 작성 목표**:
#     모든 영화 감독의 영화 평점 평균을 계산하고, 평균 평점이 높은 순으로 정렬하는 MongoDB 쿼리를 함수로 만들어 문제를 해결해 봅니다.
collection = db["movies"]


def movie_avg(db):
    movie_collection = db.movies
    pipeline = [
        {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},
        {"$sort": {"average_rating": -1}},
    ]
    results = movie_collection.aggregate(pipeline)
    for result in results:
        print(result)


movie_avg(db)

#     **[문제 3: 특정 사용자의 최근 행동 조회]**

#     - **문제 설명**:
#     특정 사용자의 최근 행동 로그를 조회하고자 합니다. 이 때, 최신 순으로 정렬하여 최근 5개의 행동만을 보고 싶습니다.
#     - **쿼리 작성 목표**:
#     사용자 ID가 1인 사용자의 최근 행동 5개를 시간 순으로 정렬하여 조회하는 MongoDB 쿼리를 함수로 만들어 문제를 해결해 봅니다.
collection = db["action"]


def action_log(db, userId, limit=5):
    action_collection = db.action
    query = {"userId": userId}
    sort_standard = [("timestamp", -1)]

    actions = action_collection.find(query).sort(sort_standard).limit(limit)
    for action in actions:
        print(action)


action_log(db, 1)


#     **[문제 4: 출판 연도별 책의 수 계산]**

#     - **문제 설명** :
#     데이터베이스에 저장된 책 데이터를 이용하여 각 출판 연도별로 출판된 책의 수를 계산하고자 합니다. 이 데이터는 시간에 따른 출판 트렌드를 분석하는 데 사용될 수 있습니다.
#     - **쿼리 작성 목표** :
#     각 출판 연도별로 출판된 책의 수를 계산하고, 출판된 책의 수가 많은 순서대로 정렬하는 MongoDB 쿼리를 함수로 만들어 문제를 해결해 봅니다.
collection = db["publish"]


def publish_year_cal(db):
    publish_collection = db.publish
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
    ]

    results = publish_collection.aggregate(pipeline)
    for result in results:
        print(result)


publish_year_cal(db)

#     **[문제 5: 특정 사용자의 행동 유형 업데이트]**

#     - **문제 설명**:
#     특정 사용자의 행동 로그 중, 특정 날짜 이전의 "view" 행동을 "seen"으로 변경하고 싶습니다. 예를 들어, 사용자 ID가 1인 사용자의 2023년 4월 10일 이전의 모든 "view" 행동을 "seen"으로 변경하는 작업입니다.
#     - **쿼리 작성 목표**:
#     사용자 ID가 1인 사용자의 2023년 4월 10일 이전의 "view" 행동을 "seen"으로 변경하는 MongoDB 업데이트 쿼리를 함수로 만들어 문제를 해결해 봅니다.
from datetime import datetime

collection = db["usertype"]


def action_type(db, userId, date, old_action, new_action):
    action_type_collection = db.usertype
    query = {"user_id": userId, "action": old_action, "timestamp": {"$lt": date}}

    update = {"$set": {"action": new_action}}

    result = action_type_collection.update_many(query, update)
    print(f"Updated {result.modified_count} documents.")


action_type(db, 1, datetime(2023, 4, 10), "view", "seen")
