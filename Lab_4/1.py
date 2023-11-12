import json

def calculate_sum_of_products(json_file_path):

    with open(json_file_path, 'r') as file:
        data = json.load(file)
    sum_of_products = 0

    for dictionary in data:
        score = dictionary["score"]
        weight = dictionary["weight"]
        product = score * weight
        sum_of_products += product

    sum_of_products = round(sum_of_products, 3)
    return sum_of_products

json_file_path = "input4.1.json"
result = calculate_sum_of_products(json_file_path)
print(result)






















