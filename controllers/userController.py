from flask import Blueprint, request
from flask_api import status
from dal import userCollection
import json
import re
from validator import userValidator

userRoutes = Blueprint("users", __name__)

@userRoutes.route("/", methods=["GET", "POST"])
def user_list():
    """
    List or create users.
    """
    if request.method == "POST":
        data = request.get_json()
        result = userValidator.validator.validate(data)

        if not result:
            return userValidator.validator.errors, status.HTTP_400_BAD_REQUEST
        if "id" in data:
            user = userCollection.getUserById(data["id"])
            if user is not None:
                return "User Exist with same Id", status.HTTP_400_BAD_REQUEST
        success = userCollection.createUser(data)
        if success:
            return "User Created", status.HTTP_201_CREATED
        return "Error in Creating User", status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        page = request.args.get("page", 1, int)
        limit = request.args.get("limit", 5, int)
        name = request.args.get("name", "", str)
        sort = request.args.get("sort", "", str)
        return getUsers(page, limit, name, sort), status.HTTP_200_OK

@userRoutes.route("/<int:id>/", methods=["GET", "PUT", "DELETE"])
def user_update(id):
    """
    Retrieve, update or delete user instances.
    """
    if request.method == "PUT":
        data = request.get_json()
        if "id" in data:
            del data["id"]
        validator = userValidator.partialValidator(data)
        result = validator.validate(data)
        if not result:
            return validator.errors, status.HTTP_400_BAD_REQUEST
        success = userCollection.updateUserById(id, data)
        if success:
            return "User Updated", status.HTTP_201_CREATED
        return "Error in updating User", status.HTTP_500_INTERNAL_SERVER_ERROR

    elif request.method == "DELETE":
        success = userCollection.deleteUser(id)
        if success:
            return "User Deleted", status.HTTP_201_CREATED
        return "Error in deleting User", status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        user = userCollection.getUserById(id)
        if user is None:
            return "User not found", status.HTTP_404_NOT_FOUND
        return json.dumps(user, default=str), status.HTTP_200_OK

def getUsers(page,limit=5,name=None,sort=None):
    skip = limit*(page-1)
    direction = 1
    sortBy = ""
    if sort:
        direction = -1 if sort.startswith("-") else 1
        sortBy = sort.lstrip("-")
    
    users = userCollection.getUsers(skip, limit, name, sortBy, direction)
    return json.dumps(list(users), default=str)