

from collections import namedtuple

class1 = {'Li', 'Audry', 'Jia', 'Migel', 'Tanya'}
class2 = {'Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'}
class3 = {'Migel', 'Zhang', 'Hiroto', 'Anita', 'Jia'}

print('Students in all three classes:',sorted(class1&class2&class3))
print('All students:', sorted(class1 | class2 | class3))
print('Students in class1 but not class2 or class3:', sorted(class1 - class2 - class3))

list = [1,2,3]
list[1], list[2] = list [2], list[1]
print('List after swap:',list)

casablance_tuple = 'Casablanca','1942','romantic drama'
(title, year, genre) = casablance_tuple
print('My favorite movie is:', title)

Movie = namedtuple('Movie', 'title, year, genre')
Movie_tuple = Movie('Casablanca','1942','romantic drama')
print('My favorite movie is:', title)

Moviestars = namedtuple('Moviestars','title, year, genre, stars')
favoritemovie = Moviestars('Casablanca','1942','romantic drama',['Humphrey Bogart','Ingrid Bergman'])
favoritemovie.stars.append('Claude Rains')
print('My favorite star is:', favoritemovie.stars[1])
print(favoritemovie)
