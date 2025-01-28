my_set = set()

my_other_set = {}; #Esto es un diccionario
print(type(my_other_set))

#Objeto de js, y deja de ser diccionario
my_other_set = {
    35,
    1.77,
    "Yesid",
    "Vanegas"
}

print(type(my_other_set));

print(len(my_other_set));

my_other_set.add("Developer");

print(my_other_set);

print("Vanegas" in my_other_set)
my_other_set.remove("Vanegas");
print(my_other_set);

my_other_set.clear();
print(my_other_set);

my_set = {35, 1.77, "Yesid", "Vanegas"};
my_list = list(my_set)
print(my_list)
