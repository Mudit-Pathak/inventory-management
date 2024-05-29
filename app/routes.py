from flask import Blueprint, request, jsonify
from app import db
from app.models import InventoryItem

bp = Blueprint('inventory', __name__)

@bp.route('/items', methods=['POST'])
def add_item():
    data = request.json
    item = InventoryItem(name=data['name'], quantity=data['quantity'], price=data['price'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item added successfully'}), 201

@bp.route('/items', methods=['GET'])
def view_items():
    items = InventoryItem.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'price': item.price} for item in items])

@bp.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = InventoryItem.query.get_or_404(id)
    data = request.json
    item.name = data.get('name', item.name)
    item.quantity = data.get('quantity', item.quantity)
    item.price = data.get('price', item.price)
    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})

@bp.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = InventoryItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})
 
