my_dict={'Dima' : 2005, 'Artur' : 2000}
print(my_dict)
print(my_dict['Dima'], my_dict.get('Sasha'))
my_dict.update({'Tamer' : 2005,
               'Anton': 1977})
del my_dict['Dima']
print(my_dict)
my_set={1,2,1,3,4,2,2,'Dima',0.4,1}
print(my_set)
my_set.update([5,'String'])
print(my_set)
my_set.remove(5)
my_set.discard('Dima')
print(my_set)