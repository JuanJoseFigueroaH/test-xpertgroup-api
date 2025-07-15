def user_entity(user: dict) -> dict:
    return {
        "id": str(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "password": user["password"],
        "username": user["username"],
    }

def user_in_db(user: dict) -> dict:
    return {
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "password": user["password"],
        "username": user["username"],
    }
