# demonstrate hashtable usage


# TODO: create a hashtable all at once
from subprocess import list2cmdline


List1 = dict({"key1": 1, "key2":2, "key3":3})
print(List1)
# TODO: create a hashtable progressively
List2 = {}
List2["key1"]= 1
List2["key2"]=20
List2["key3"]=30
print(List2)
# TODO: try to access a nonexistent key
#print(List2[4])

# TODO: replace an item
List1[1]="Zweite"
print(List1)

# TODO: iterate the keys and values in the dictionary
for key, value in List2.items():
    print("key:",key, "value:",value)