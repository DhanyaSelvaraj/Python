Basics of Dictionary:

>>> dict={"name":"Dhanya","age":21,"place":"Salem"}
>>> dict
{'name': 'Dhanya', 'age': 21, 'place': 'Salem'}
>>> dict["name"]
'Dhanya'
>>> dict["age"]
21
>>> dict["place"]
'Salem'
>>> dict.keys()
dict_keys(['name', 'age', 'place'])
>>> dict.values()
dict_values(['Dhanya', 21, 'Salem'])
>>> x=dict.copy()
>>> x
{'name': 'Dhanya', 'age': 21, 'place': 'Salem'}
>>> x.clear()
>>> x
{}
>>> dict["qualification"]="BE"
>>> dict
{'name': 'Dhanya', 'age': 21, 'place': 'Salem', 'qualification': 'BE'}
>>> dict.popitem()
('qualification', 'BE')
>>> dict
{'name': 'Dhanya', 'age': 21, 'place': 'Salem'}
>>> dict.update({"designation":"Software Enginer"})
>>> dict
{'name': 'Dhanya', 'age': 21, 'place': 'Salem', 'designation': 'Software Enginer'}
>>> dict={1:{"name":"Dhanya","age":21,"place":"Salem"},2:{"name":"Sanjay","age":20,"place":"Salem"},3:{"name":"Vivin","age":1,"place":"Salem"}}
>>> dict
{1: {'name': 'Dhanya', 'age': 21, 'place': 'Salem'}, 2: {'name': 'Sanjay', 'age': 20, 'place': 'Salem'}, 3: {'name': 'Vivin', 'age': 1, 'place': 'Salem'}}
>>> dict[4]={"name":"Vivetha","age":3,"place":"Salem"}
>>> dict
{1: {'name': 'Dhanya', 'age': 21, 'place': 'Salem'}, 2: {'name': 'Sanjay', 'age': 20, 'place': 'Salem'}, 3: {'name': 'Vivin', 'age': 1, 'place': 'Salem'}, 4: {'name': 'Vivetha', 'age': 3, 'place': 'Salem'}}