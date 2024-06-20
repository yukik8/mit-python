def is_in(str1, str2) -> bool:
    for s1 in str1:
        for s2 in str2:
            print(f'str1 = "{s1}", str2 = "{s2}", answer = "{s1 in s2 or s2 in s1}"')

str1 = ('hello', 'hi, world', 'abc')
str2 = ('hello, world', 'hi', 'world')
print(is_in(str1,str2))
