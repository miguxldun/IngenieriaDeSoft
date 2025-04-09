fake_db = []

def get_items():
    return fake_db

def add_item(item):
    fake_db.append(item)
    return item

def update_item(item_id, item):
    for i, existing in enumerate(fake_db):
        if existing.id == item_id:
            fake_db[i] = item
            return item
    raise Exception("Item not found")

def delete_item(item_id):
    for i, existing in enumerate(fake_db):
        if existing.id == item_id:
            del fake_db[i]
            return {"message": "Item deleted"}
    raise Exception("Item not found")
