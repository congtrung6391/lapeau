from .db import get_db

class Sickness():
    def __init__(self, id_, name, reason, description):
        self.id = id_
        self.name = name
        self.reason = reason
        self.description = description

    @staticmethod
    def get(id):
        db = get_db()
        sickness = db.execute(
            "SELECT * FROM sickness WHERE id = ?", (id)
        ).fetchone()
        if not sickness:
            return None

        sickness = sickness(
            id_=sickness[0], name=sickness[1], reason=sickness[2], description=sympton[3]
        )
        return sickness

    @staticmethod
    def create(id_, name, reason, description):
        db = get_db()
        db.execute(
            "INSERT INTO sickness (id, name, reason, description) "
            "VALUES (?, ?, ?, ?)",
            (id_, name, reason, description),
        )
        db.commit()