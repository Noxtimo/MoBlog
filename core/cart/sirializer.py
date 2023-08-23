import json
from product.models import Product

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Product):
            return {
                "name": obj.name,
                "price": obj.price,
                # Include other attributes as needed
            }
        return super().default(obj)

product_json = json.dumps(Product, cls=CustomEncoder)
