from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.item import ItemModel


class Item(Resource):

    @jwt_required
    def post(self):

        user_id = get_jwt_identity()

        item_parser = reqparse.RequestParser()
        item_parser.add_argument(
            'item_name',
            type=str,
            required=True,
            help='This field cannot be blank.'
        )
        item_parser.add_argument(
            'category',
            type=str,
            required=True,
            help='This field cannot be blank.'
        )
        item_parser.add_argument(
            'city',
            type=str,
            required=True,
            help='This field cannot be blank.'
        )
        item_parser.add_argument(
            'picture',
            type=str,
            required=True,
            help='This field cannot be blank.'
        )
        item_parser.add_argument(
            'price',
            type=float,
            required=True,
            help='This field cannot be blank.'
        )
        item_parser.add_argument(
            'description',
            type=str,
            required=True,
            help='This field cannot be blank.'
        )
        item_parser.add_argument(
            'phone_number',
            type=str,
            required=True,
            help='This field cannot be blank.'
        )
        data = item_parser.parse_args()

        item = ItemModel(
            user_id,
            data['item_name'],
            data['category'],
            data['city'],
            data['phone_number']
        )
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return {'message': 'Item created successfully.'}, 201


class ItemTrack(Resource):
    def get(self, item_id):
        item = ItemModel.find_by_id(item_id)
        if item:
            return item.json()
        return {'message': 'Item Not found.'}, 404 #status code

    def put(self, item_id):
        pass

    def delete(self, item_id):
        item = ItemModel.find_by_id(item_id)
        if item:
            item.delete_from_db()
            return {'message': 'Order deleted.'}
        return {'message': 'order not found.'}, 404


