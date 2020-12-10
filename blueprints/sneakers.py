from flask import (
    Blueprint,
    request,
    jsonify,
)
from flask.views import MethodView
from mysql_con import con, cur
from Products import SneakersProduct
bp = Blueprint('sneakers', __name__)


class SneakersView(MethodView):
    def post(self):
        data = request.json
        name = data['name']
        count = data['quantity']
        manufacturer = data['brand']
        price = data['price']
        size = data['size']
        color = data['color']
        item = SneakersProduct(None, price, name, count, manufacturer, size, color)
        cur.execute('INSERT INTO sneakers(price, named, quantity, brand, size, color) VALUES (%s, %s, %s, %s, %s, %s)',
                    (item.price, item.name, item.quantity, item.brand, item.size, item.color))
        con.commit()
        return '', 200


class SneakersIDView(MethodView):
    def get(self, sneakersID):
        cur.execute(f'SELECT * FROM sneakers WHERE id = {sneakersID}')
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

    def delete(self, sneakersID):
        cur.execute(f'DELETE FROM sneakers WHERE id = {sneakersID}')
        con.commit()
        return '', 200

    def patch(self, sneakersID):
        data = dict(request.json)
        update = 'UPDATE sneakers '
        where = f'WHERE id = {sneakersID}'
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


bp.add_url_rule('', view_func=SneakersView.as_view('sneakers'))
bp.add_url_rule('/<int:sneakersID>', view_func=SneakersIDView.as_view('sneakers_id'))

