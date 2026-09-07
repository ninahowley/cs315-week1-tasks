import json

cat_data = {
    "name": "Gizmo",
    "is_cat": True,
    "hobbies": ["sleeping", "playing"],
    "age": 1,
    "address": {
        "work": None,
        "home": ("Boston", "Massachusetts"),
    },
    "friends": [
        {
            "name": "Chupi",
            "hobbies": ["eating", "hunting"]
        },
        {
            "name": "Gatalita",
            "hobbies": ["eating", "sleeping"]
        },
    ],
}

with open("hello_gizmo.json", mode="w", encoding="utf-8") as write_file:
    json.dump(cat_data, write_file)