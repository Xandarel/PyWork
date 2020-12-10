from flask import (
    Blueprint,
    request,
    jsonify,
)
from flask.views import MethodView
from mysql_con import con, cur
from Products import TshirtProduct


bp = Blueprint('tshirts', __name__)


class TshirtView(MethodView):
    def post(self):
        data = request.json
        name = data['name']
        count = data['quantity']
        manufacturer = data['brand']
        price = data['price']
        size = data['size']
        color = data['color']
        item = TshirtProduct(None, price, name, count, manufacturer, size, color)
        cur.execute('INSERT INTO tshirt(price, named, quantity, brand, size, color) VALUES (%s, %s, %s, %s, %s, %s)',
                    (item.price, item.name, item.quantity, item.brand, item.size, item.color))
        con.commit()
        return '', 200


class TshirtIDView(MethodView):
    def get(self, tshirtID):
        cur.execute(f'SELECT * FROM tshirt WHERE id = {tshirtID}')
        data = cur.fetchone()
        res = {'id': data[0],
               'price': data[1],
               'name': data[2],
               'quantity': data[3],
               'brand': data[4],
               'size': data[5],
               'color': data[6]
               }
        return jsonify(res), 200

    def delete(self, tshirtID):
        cur.execute(f'DELETE FROM sneakers WHERE id = {tshirtID}')
        con.commit()
        return '', 200

    def patch(self, tshirtID):
        data = dict(request.json)
        update = 'UPDATE sneakers '
        where = f'WHERE id = {tshirtID}'
        set = 'SET '
        if 'price' in data.keys():
            set += f"price = {data['price']},"
        if 'name' in data.keys():
            set += f"named = {data['name']},"
        if 'quantity' in data.keys():
            set += f"quantity = {data['quantity']},"
        if 'brand' in data.keys():
            set += f"brand = {data['brand']},"
        if 'size' in data.keys():
            set += f"size = {data['size']},"
        if 'color' in data.keys():
            set += f"color = {data['color']},"
        cur.execute(update + set[:-1] + where)
        con.commit()


bp.add_url_rule('', view_func=TshirtView.as_view('tshirts'))
bp.add_url_rule('/<int:tshirtID>', view_func=TshirtIDView.as_view('tshirts_id'))

