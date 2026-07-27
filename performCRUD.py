# import requests
# api='http://127.0.0.1:8000/products'
# get_data= requests.get(api)
# print(get_data.json())

'''1. GET All Products'''

# import requests

# api = "http://127.0.0.1:8000/products"

# response = requests.get(api)

# print(response.status_code)
# print(response.json())

'''2. GET Product by ID'''

# import requests

# product_id = 1

# api = f"http://127.0.0.1:8000/products/{product_id}"

# response = requests.get(api)

# print(response.status_code)
# print(response.json())


'''3. POST (Create Product)'''


# import requests

# api = "http://127.0.0.1:8000/products"

# data = {
#     "name": "Nothing Phone 3",
#     "category": "Mobiles",
#     "price": 45999,
#     "stock": 20,
#     "brand": "Nothing"
# }

# response = requests.post(api, json=data)

# print(response.status_code)
# print(response.json())



'''4. PUT (Update Product)'''

# import requests

# product_id = 2

# api = f"http://127.0.0.1:8000/products/{product_id}"

# data = {
#     "name": "Samsung Galaxy S25 Ultra",
#     "category": "Mobiles",
#     "price": 109999,
#     "stock": 15,
#     "brand": "Samsung"
# }

# response = requests.put(api, json=data)

# print(response.status_code)
# print(response.json())


'''5. DELETE Product'''


# import requests

# product_id = 3

# api = f"http://127.0.0.1:8000/products/{product_id}"

# response = requests.delete(api)

# print(response.status_code)
# print(response.json())