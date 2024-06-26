from flask import Blueprint, request
from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return {"users": search_users(request.args)}, 200

def search_users(args):
    id_param = args.get("id")
    name_param = args.get("name", "").lower()
    age_param = args.get("age")
    occupation_param = args.get("occupation", "").lower()

    results = []

    for user in USERS:
        match = False

        if id_param and user["id"] == id_param:
            match = True

        if not match and name_param and name_param in user["name"].lower():
            match = True

        if not match and age_param:
            try:
                user_age = int(user["age"])
                age_param = int(age_param)
                if age_param - 1 <= user_age <= age_param + 1:
                    match = True
            except ValueError:
                pass

        if not match and occupation_param and occupation_param in user["occupation"].lower():
            match = True

        if match:
            results.append(user)

    return results
