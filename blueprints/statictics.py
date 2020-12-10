from flask import (
    Blueprint,
    request,
    jsonify,
)
from flask.views import MethodView
from mysql_con import con, cur
from Products import SneakersProduct, TshirtProduct
bp = Blueprint('statistics', __name__)


class BrandStat(MethodView):
    def get(self):
        cur.execute('SHOW tables')
        tables = cur.fetchall()
        res = {}
        for table in tables:
            res[table[0]] = {}
            cur.execute(f'SELECT DISTINCT brand FROM {table[0]}')
            stat = cur.fetchall()
            for st in stat:
                res[table[0]][st[0]] = []
                # print(f"SELECT * FROM {table[0]} WHERE brand = '{st[0]}'")
                cur.execute(f"SELECT * FROM {table[0]} WHERE brand = '{st[0]}'")
                for data in cur.fetchall():
                    if table[0] == 'sneakers':
                        product = SneakersProduct(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                        res[table[0]][st[0]].append(product.dict_product())
                    elif table[0] == 'tshirt':
                        product = TshirtProduct(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                        res[table[0]][st[0]].append(product.dict_product())
        return jsonify(res), 200


class SizeStat(MethodView):
    def get(self):
        cur.execute('SHOW tables')
        tables = cur.fetchall()
        res = {}
        for table in tables:
            res[table[0]] = {}
            cur.execute(f'SELECT DISTINCT size FROM {table[0]}')
            stat = cur.fetchall()
            for st in stat:
                res[table[0]][st[0]] = []
                cur.execute(f"SELECT * FROM {table[0]} WHERE size = '{st[0]}'")
                for data in cur.fetchall():
                    if table[0] == 'sneakers':
                        product = SneakersProduct(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                        res[table[0]][st[0]].append(product.dict_product())
                    elif table[0] == 'tshirt':
                        product = TshirtProduct(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                        res[table[0]][st[0]].append(product.dict_product())
        return jsonify(res), 200


bp.add_url_rule('/brand', view_func=BrandStat.as_view('brand'))
bp.add_url_rule('/size', view_func=SizeStat.as_view('size'))
