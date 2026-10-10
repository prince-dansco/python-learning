people =[
    {'name':'prince', 'house':'john'},
    {'name':'john', 'house':'john'},
    {'name':'sera', 'house':'john'},
    {'name':'success', 'house':'john'},
]

def f(person):
    return person['house']


people.sort(key=lambda person: person['house'])
# people.sort(key=f)

print(people)