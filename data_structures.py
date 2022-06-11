my_list = [0, 1]
print(f"{my_list=}")

print(f"{my_list*2=}")
print(f"{[my_list]*2=}")

my_set = {1, 2, 3, 4}
print(f"{my_set=}")

my_set_2 = {3, 4, 5, 6}
print(f"{my_set_2=}")

print(f"union: {my_set.union(my_set_2)}")
print(f"{my_set.intersection(my_set_2)=}")
print(f"{my_set.difference(my_set_2)=}")
print(f"{my_set.symmetric_difference(my_set_2)=}")


my_tuple = (1, 2, 3)
print(f"{my_tuple=}")

my_tuple += (4, 5, 6)
print(f"{my_tuple=}")

print(f"{my_tuple.count(6)=}")
print(f"{my_tuple.count(7)=}")


my_tuple2 = (1, 2, 3, "edureka")
for item in my_tuple2:
    print(item)

print(f"{my_tuple2=}")
print(f"{my_tuple2[0]=}")
print(f"{my_tuple2[:]=}")
print(f"{my_tuple2[3][4]=}")
print(f"{my_tuple2[::-1]=}")
print(f"{my_tuple2[:-1]=}")
print(f"{my_tuple2[:None]=}")


my_dict = {"First": "Python", "Second": "Java", "Third": "Ruby"}
print(f"{my_dict.keys()=}")  # get keys
print(f"{my_dict.values()=}")  # get values
print(f"{my_dict.items()=}")  # get key-value pairs
# print(f"{my_dict.get("First")=}")
# print(f"{my_dict.get("Fourth")=}")
# print(f"{my_dict["Fourth"]=}")
