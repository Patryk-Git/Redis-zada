import redis
import json

redis_db = redis.Redis(host='localhost', port=6379, db=0)

if __name__ == "__main__":


    user = {
        "imie": "Paweł",
        "Nazwisko": "Gaweł",
        "Zawód": "Prawnik"
    }
    redis_db.hset("users", '2', json.dumps(user))

    user = {
        "imie": "Tomek",
        "Nazwisko": "Kowal",
        "Zawód": "Tester"
    }
    redis_db.hset("users", '1', json.dumps(user))


    user = {
        "imie": "Dawid",
        "Nazwisko": "Szulc",
        "Zawód": "Bezrobotny"
    }
    redis_db.hset("users", '3', json.dumps(user))

    user = {
        "imie": "Marek",
        "Nazwisko": "Kondrad",
        "Zawód": "Prawnik"
    }
    redis_db.hset("users", '4', json.dumps(user))
