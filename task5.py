# Напиши функцию multi_filter,
# которая принимает список словарей
# и список функций-фильтров.
# Функция должна возвращать только те элементы,
# которые удовлетворяют всем фильтрам.

# P.s. фуннкции можно не только передавать как аргумент,
# но и складывать в список


def multi_filter_objects(objects, func_filters):
    result = []
    for obj in objects:
        for func in func_filters:
            if not func(obj):
                break
            else:
                result.append(obj)
    return result


def name_lenght_filter(obj):
    return len(obj["name"]) > 7


if __name__ == "__main__":
    data = [
        {
            "name": "Laptop",
            "price": 12
        },
        {
            "name": "Smartphone",
            "price": 6
        },
        {
            "name": "Headphones",
            "price": 1
        },
        {
            "name": "Monitor",
            "price": 3
        },
        {
            "name": "Keyboard",
            "price": 0
        }
    ]
    filters = [name_lenght_filter]
    print(multi_filter_objects(data, filters))