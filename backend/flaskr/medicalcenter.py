from .db import get_db

class Medicalcenter():
    def __init__(self, id_, name, address, phone):
        self.id = id_
        self.name = name
        self.address = address
        self.phone = phone

    @staticmethod
    def get(id):
        db = get_db()
        medicalcenter = db.execute(
            "SELECT * FROM medicalcenter WHERE id = ?", (id)
        ).fetchone()
        if not medicalcenter:
            return None

        medicalcenter = medicalcenter(
            id_=medicalcenter[0], name=medicalcenter[1], address=medicalcenter[2], phone=sympton[3]
        )
        return medicalcenter

    @staticmethod
    def create(id_, name, address, phone):
        db = get_db()
        db.execute(
            "INSERT INTO medicalcenter (id, name, address, phone) "
            "VALUES (?, ?, ?, ?)",
            (id_, name, address, phone),
        )
        db.commit()