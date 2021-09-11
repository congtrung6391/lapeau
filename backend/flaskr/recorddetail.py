from .db import get_db

class Recorddetail():
    def __init__(self, id_, id_recorddetail, id_sickness, result):
        self.id = id_
        self.id_recorddetail = id_recorddetail
        self.id_sickness = id_sickness
        self.result = result

    @staticmethod
    def get(id_):
        db = get_db()
        recorddetail = db.execute(
            "SELECT * FROM record_detail WHERE id = ?", (id_,)
        ).fetchone()
        if not recorddetail:
            return None

        recorddetail = Recorddetail(
            id_=recorddetail[0], id_record=recorddetail[1], id_sickness=recorddetail[2], result=sympton[3]
        )
        return recorddetail

    @staticmethod
    def getByRecordid(record_id):
        db = get_db()
        recorddetails = db.execute(
            "SELECT * FROM record_detail WHERE id_record = ?", (record_id,)
        ).fetchone()
        if not recorddetails:
            return {}

        results = {}

        for detail, idx in recorddetails:
            results.append(idx, Recorddetail(
                id_=recorddetail[0], id_record=recorddetail[1], id_sickness=recorddetail[2], result=sympton[3]
            ))
        return results

    @staticmethod
    def create(id_, id_record, id_sickness, result):
        db = get_db()
        db.execute(
            "INSERT INTO record_detail (id, id_record, id_sickness, result) "
            "VALUES (?, ?, ?, ?)",
            (id_, id_record, id_sickness, result,)
        )
        db.commit()

    @staticmethod
    def generate_id():
        db = get_db()
        cur = db.cursor()
        res = db.execute("SELECT COUNT(id) as cnt FROM record_detail")
        resFetched = res.fetchone()
        resDict = dict(zip([c[0] for c in res.description], resFetched))
        cnt = resDict['cnt']
        cnt += 1
        print(cnt)
        return cnt