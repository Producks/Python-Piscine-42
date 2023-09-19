ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = 'World'

#Tuple can't be changed so create a list to be able change it back into tuple
ft_tuple_list = [i for i in ft_tuple]
ft_tuple_list[1] = "Quebec!"
ft_tuple = tuple(ft_tuple_list)

#Set cannot have double
ft_set.discard('tutu!')
ft_set.add('Quebec')

# Change dictionary
ft_dict["Hello"] = "42 Montreal"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)