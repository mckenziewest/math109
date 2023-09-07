with open("homework_sets.html") as file:
    all_text = file.read()


name_map = {}

for chapter in [a for a in range(1,5)] + ["R"]:
    for section in range(1,9):
        name = f"Homework_{chapter}.{section}"
        if chapter == "R":
            name = f"Homework_{chapter}"
        clean_name = name.replace("_"," ")
        if name in all_text:
            name_map[clean_name] = {}
            name_map[clean_name]["name"] = "🌱 " + clean_name
            name_map[clean_name]["modules"] = ["WeBWorK"]
            name_map[clean_name]["assignment_group_name"] = "Homework"

            practice = clean_name.replace("Homework","PRACTICE")
            name_map[practice] = {}
            name_map[practice]["name"] = "🌻 " + practice
            name_map[practice]["modules"] = ["Practice"]
            name_map[practice]["assignment_group_name"] = "Practice"
        if chapter == "R":
            break

import json
json_object = json.dumps(name_map, indent=4)

with open("name_map.json","w") as file:
    file.write(json_object)