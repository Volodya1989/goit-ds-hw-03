# main.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure


# Connect to MongoDB Atlas
def connect_to_db():
    try:
        client = MongoClient('base_mongoDB_url')  # Replace with your MongoDB URI
        db = client.cat_db
        return db.cats
    except ConnectionFailure:
        print("Failed to connect to the database.")
        return None


def create_cat(collection, name, age, features):
    cat = {"name": name, "age": age, "features": features}
    collection.insert_one(cat)


def read_all_cats(collection):
    for cat in collection.find():
        print(cat)


def find_cat_by_name(collection, name):
    cat = collection.find_one({"name": name})
    print(cat if cat else "Cat not found.")


def update_cat_age(collection, name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print("Updated" if result.modified_count else "No changes made.")


def add_feature_to_cat(collection, name, feature):
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    print("Feature added." if result.modified_count else "No changes made.")


def delete_cat_by_name(collection, name):
    result = collection.delete_one({"name": name})
    print("Deleted." if result.deleted_count else "Cat not found.")


def delete_all_cats(collection):
    result = collection.delete_many({})
    print(f"Deleted {result.deleted_count} cats.")


def main():
    collection = connect_to_db()
    if collection is None:
        return

    # Example usage
    create_cat(collection, "Barsik", 3, ["loves jumping", "orange"])
    read_all_cats(collection)
    find_cat_by_name(collection, "Barsik")
    update_cat_age(collection, "Barsik", 5)
    add_feature_to_cat(collection, "Barsik", "friendly")
    delete_cat_by_name(collection, "Barsik")
    delete_all_cats(collection)


if __name__ == "__main__":
    main()
