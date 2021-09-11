from .db import get_db

class Symptom():
    def __init__(self, id_, name, description, id_sickness):
        self.id = id_
        self.url = url
        self.description = description
        self.id_sickness = id_sickness

    @staticmethod
    def get(id):
        db = get_db()
        symptom = db.execute(
            "SELECT * FROM symptom WHERE id = ?", (id)
        ).fetchone()
        if not symptom:
            return None

        symptom = symptom(
            id_=symptom[0], name=symptom[1], description=symptom[2], id_sickness=sympton[3]
        )
        return symptom

    @staticmethod
    def create(id_, name, description, id_sickness):
        db = get_db()
        db.execute(
            "INSERT INTO symptom (id, name, description, id_sickness) "
            "VALUES (?, ?, ?, ?)",
            (id_, name, description, id_sickness),
        )
        db.commit()