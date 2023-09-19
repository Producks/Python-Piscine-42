def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print("List : {}".format(type(object)))
    elif isinstance(object, tuple):
        print("Tuple : {}".format(type(object)))
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42

def main():
    return 0

if __name__ == "__main__":
    main()