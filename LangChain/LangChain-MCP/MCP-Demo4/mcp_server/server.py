from mcp.server.fastmcp import FastMCP
mcp=FastMCP('Product Server')
PRODUCTS = {
    "P101": {
        "id": "P101",
        "name": "Laptop",
        "price": 75000,
        "stock": 12
    },
    "P102": {
        "id": "P102",
        "name": "Monitor",
        "price": 18000,
        "stock": 5
    },
    "P103": {
        "id": "P103",
        "name": "Keyboard",
        "price": 2500,
        "stock": 20
    }
}


@mcp.tool()
def get_product(product_id: str):
    """
    Get product details including price and current stock.
    """

    product = PRODUCTS.get(product_id)

    if product is None:
        return {
            "error": f"Product {product_id} not found"
        }

    return product
@mcp.tool()
def search_products(name: str):
    """
    Search products by name.
    """

    results = []

    for product in PRODUCTS.values():
        if name.lower() in product["name"].lower():
            results.append(product)

    return results

@mcp.tool()
def check_stock(product_id: str):
    """
    Check the current stock quantity of a product.
    """

    product = PRODUCTS.get(product_id)

    if product is None:
        return {
            "error": f"Product with ID {product_id} was not found."
        }

    return {
        "product_id": product["id"],
        "product_name": product["name"],
        "stock": product["stock"]
    }


if __name__ == "__main__":
    mcp.run()
