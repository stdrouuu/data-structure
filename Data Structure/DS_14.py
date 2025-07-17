#Review
#Dictionary
#key dan value -> Key: Value
#commas
#{}
#keys must unique, immutable (cannot be changed)

dict1 = {"Name": "Fredi", "Age": 45, "Class": "CS"}
print(dict1["Name"])

dict1["Name"] = "Erick"
print(dict1["Name"])

print(dict1)
del dict1["Age"]
print(dict1)
