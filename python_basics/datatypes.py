#Task 1: Python Data Types in Action
int_var = 5
float_var = 16.76
complx_var = 3+4j
list_var = [1,2,3,4,5]
tuple_var = (10, 20, 30)
dict_var = {'car': 'BMW', 'owner': 'John', 'miles': 120000}
set_var = {1,3,7,8,4}
bool_var = False

print("Value:", int_var, "Type:", type(int_var))
print("Value:", float_var, "Type:", type(float_var))
print("Value:", complx_var, "Type:", type(complx_var))
print("Value:", list_var, "Type:", type(list_var))
print("Value:", tuple_var, "Type:", type(tuple_var))
print("Value:", dict_var, "Type:", type(dict_var))
print("Value:", set_var, "Type:", type(set_var))
print("Value:", bool_var, "Type:", type(bool_var))

int_to_float = float(int_var)
float_to_int = int(float_var)

print("Integer converted to Float:", int_to_float, "Type:", type(int_to_float))
print("Float converted to Integer:", float_to_int, "Type:", type(float_to_int))
