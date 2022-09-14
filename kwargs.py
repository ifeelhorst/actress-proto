
# List of prim-keys
primaryKeys = [0, 1, 2, 3, 4, 5]
# list of recorded hearts
hearts = ["yes", "yes", "no", "no", "yes", "yes"]


kwargs = {}
print("BEFORE kwargs:", kwargs)

for i in primaryKeys:
    kwargs[i] = hearts[i]

print("AFTER kwargs:", kwargs)

print("spezifisch", kwargs[2])
