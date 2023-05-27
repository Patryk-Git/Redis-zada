import json
import redis
from flask import Flask, request

app = Flask(__name__)
redis_db = redis.Redis(host='localhost', port=6379, db=0)


@app.route("/user/add/<user_id>", methods=["POST"])
def add_user(user_id):
    user_data = request.get_json()
    redis_db.hset("users", user_id, json.dumps(user_data))
    return "User added successfully"

@app.route("/user/delete/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    redis_db.hdel("users", user_id)
    return "User deleted successfully"

@app.route("/user/get/<user_id>", methods=["GET"])
def get_user(user_id):
    user_data = redis_db.hget("users", user_id)
    if user_data:
        return user_data
    else:
        return "User not found"

@app.route("/user/get_all", methods=["GET"])
def get_all_users():
    all_users = redis_db.hgetall("users")
    decoded_users = {key.decode(): value.decode() for key, value in all_users.items()}
    if decoded_users:
        return json.dumps(decoded_users)
    else:
        return "No users found"


@app.route("/user/vote/<user_id>", methods=["POST"])
def vote_user(user_id):
    vote_count = redis_db.hget("users", user_id)
    if vote_count:
        redis_db.hincrby(user_id, "users", int(1))
        return "Vote recorded for user {}".format(user_id)
    else:
        return "User {} does not exist".format(user_id)


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
