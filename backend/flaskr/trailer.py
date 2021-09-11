from .db import get_db

class Trailer():
    def __init__(self, id_, url, id_sickness):
        self.id = id_
        self.url = url
        self.id_sickness = id_sickness

    @staticmethod
    def get(id):
        db = get_db()
        trailer = db.execute(
            "SELECT * FROM trailer WHERE id = ?", (id)
        ).fetchone()
        if not trailer:
            return None

        trailer = trailer(
            id_=trailer[0], url=trailer[1], id_sickness=trailer[2]
        )
        return trailer

    @staticmethod
    def create(id_, url, id_sickness):
        db = get_db()
        db.execute(
            "INSERT INTO trailer (id, name, id_sickness) "
            "VALUES (?, ?, ?)",
            (id_, url, id_sickness),
        )
        db.commit()