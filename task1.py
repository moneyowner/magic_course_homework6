# Есть в task1.json список товаров. Написать функцию
# которая принимает функцию которая трансформирует
# цену в нужную валюту.
# Результат также сохраните в modified_task1.json.
# Считайте, что изначально цены в рублях.
import  json

def transform_json_prices(filename, transform_func: callable):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for product in data:
        product["price"] = transform_func(product["price"])

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def rub_to_usd(value):
    return value//9


if __name__ == "__main__":
    transform_json_prices("task1.json", rub_to_usd)