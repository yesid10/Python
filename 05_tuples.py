my_tuple = tuple();
print(my_tuple);

my_tuple = (35, 1.77, "Yesid", "Vanegas");
print(my_tuple);
print(type(my_tuple));

# print(my_tuple[0]);
# print(my_tuple[1]);
# print(my_tuple[-2]);


print(my_tuple.count("Yesid"))
print(my_tuple.index("Vanegas"))

my_other_tuple = (35, 1.77, "Yesid", "Vanegas");

my_sum_tuple = my_tuple + my_other_tuple;

print(my_sum_tuple[0:2]);

