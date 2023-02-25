#Join a list of strings into one string
my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_lst_str = '::'.join(map(str, my_lst))
print(my_lst_str)
#out 1::2::3::4::5::6::7::8::9::10

my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_lst_str = '---'.join(map(str, my_lst))
print(my_lst_str)
#out 1---2---3---4---5---6---7---8---9---10
# we can use any symbol for join a string
