from flask import Blueprint, request, json

# Internal database
from flaskr import db
from flaskr.db import init_db_command
from flaskr.user import User
from flaskr.record import Record
from flaskr.recorddetail import Recorddetail

bp = Blueprint('record', __name__, url_prefix='/record')

@bp.route('/records', methods=['GET'])
def getUserInfo():
    username = 'user01'
    records = Record.getByUsername(username)
    return records, 200

@bp.route("/records/<recordid>", methods=['GET'])
def getRecordDetail(recordid):
  # record_id = request.view_args['recordid']
  details = Recorddetail.getByRecordid(recordid)
  return details, 200
