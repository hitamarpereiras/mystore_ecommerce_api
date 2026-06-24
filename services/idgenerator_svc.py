import uuid


def generate_id():
    return uuid.uuid4().hex[:8].upper()

def generate_idStore():
    return uuid.uuid4().hex[:12].upper()

def generate_idProduct():
    return uuid.uuid4().hex[:14].lower()

def generate_OrderCode():
    return uuid.uuid4().hex[:15].lower()
