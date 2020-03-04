from . import mongo

def getUsers(skip, take, name, sortBy, direction):
    userContext = mongo.db.users
    filter = {"isDeleted": { "$ne": True }}
    if name:
        filter["$text"] = {"$search": name}

    query = userContext.find(filter)
    if sortBy:
        query = query.sort([(sortBy, direction)])
    query = query.skip(skip).limit(take)
    return query

def createUser(data):
    if "id" in data:
        data["_id"] = data["id"]    
        del data["id"]
    userContext = mongo.db.users
    result = userContext.insert_one(data)
    return result.acknowledged

def getUserById(id):
    userContext = mongo.db.users
    return userContext.find_one({"_id": id})

def updateUserById(id, data):
    userContext = mongo.db.users
    result = userContext.update_one({"_id": id}, {"$set": data})
    return result.acknowledged

def deleteUser(id, hard=False):
    return deleteUserHardDeleteDelete(id) if hard else deleteUserSoftDelete(id)

def deleteUserSoftDelete(id):
    return updateUserById(id, {"isDeleted": True})

def deleteUserHardDelete(id):
    userContext = mongo.db.users
    result = userContext.delete_one({"_id": id})
    return result.deleted_count == 1