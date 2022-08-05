school={'1a': 24, '1b': 30, '2b': 25, '6b': 32, '7a': 25}
print(school)

school['2b'] = school['2b'] + 4
school['8a'] = 35
del school['1b']

s = 0
for i in school.values():
    s += i

print(school)
print(s)