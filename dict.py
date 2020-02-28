
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer={}
for i in range(len(person)):
    key = person[i][0]
    value = person[i][1]
    answer[key] = value

    answer['nombre'] = 'Rodrigo'

print(answer['nombre'])

