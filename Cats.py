from constructor import Cat

cats = [
    {
     'name': 'Барон',
     'sex': 'мальчик',
     'age': 2
    },
    {
     'name': 'Сэм',
     'sex': 'мальчик',
     'age': 2
    },
    ]

for cat in cats:
    cat_obj = Cat(name=cat.get('name'),
                      sex=cat.get('sex'),
                      age=cat.get('age'))
    print(cat_obj.name, cat_obj.sex, cat_obj.age)