#list
hero_list = ['hero_1', 'hero_2', 'hero_3', 12, 12.3]

#access
print(hero_list[0])

#add
print.append('hero_4')

#add in loop
for i in range(4):
    hero_list.append(i)
print(hero_list)

#update
hero_list[3] = 'new_hero'
print(hero_list)

#delete
del hero_list[4]
