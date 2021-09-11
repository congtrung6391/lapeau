from flask import json

from .db import get_db

class Record():
    def __init__(self, id_, username, image_url, createdAt):
        self.id = id_
        self.username = username
        self.image_url = image_url
        self.createdAt = createdAt

    @staticmethod
    def get(id_):
        print(id_)
        db = get_db()
        result = db.execute("SELECT * FROM record WHERE id = ?", (id_,))
        record = result.fetchone()
        if not record:
            return None

        record = Record(
            id_=record[0], username=record[1], image_url=record[2], createdAt=record[3]
        )
        return record

    @staticmethod
    def create(id_, username, image_url, createdAt):
        print(id_)
        db = get_db()
        db.execute(
            "INSERT INTO record (id, username, image_url, createdAt) VALUES (?, ?, ?, ?)",
            (id_, username, image_url, createdAt,)
        )
        db.commit()

    @staticmethod
    def generate_id():
        db = get_db()
        cur = db.cursor()
        res = db.execute("SELECT COUNT(id) as cnt FROM record")
        resFetched = res.fetchone()
        resDict = dict(zip([c[0] for c in res.description], resFetched))
        cnt = resDict['cnt']
        cnt += 1
        print(cnt)
        return cnt

    @staticmethod
    def getByUsername(username):
        print(username)
        db = get_db()
        result = db.execute("SELECT * FROM record WHERE username = ?", (username,))
        records = result.fetchall()
        if not records:
            return {}

        results = {}
        idx = 0
        for record in records:
            results[idx] = json.dumps(Record(
                id_=record[0], username=record[1], image_url=record[2], createdAt=record[3]
            ).__dict__)
            idx += 1
        print(results)
        return results