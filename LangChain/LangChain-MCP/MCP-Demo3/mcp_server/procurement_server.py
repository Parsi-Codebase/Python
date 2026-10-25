from mcp.server.fastmcp import FastMCP
mcp=FastMCP('Procurement Server')
PRODUCTS = {
    "DELL-LATITUDE-5450": {
        "name": "Dell Latitude 5450",
        "supplier": "Dell Technologies",
        "unit_price": 78500,
        "currency": "INR",
        "available_quantity": 125,
    },
    "HP-840-G11": {
        "name": "HP EliteBook 840 G11",
        "supplier": "HP India",
        "unit_price": 82000,
        "currency": "INR",
        "available_quantity": 50,
    },
}
@mcp.tool()
def get_product_details(product_code: str) -> dict:
    """
    Get the current price, supplier and availability
    of a product from the procurement system.
    """

    product = PRODUCTS.get(product_code)

    if product is None:
        return {
            "found": False,
            "message": f"Product {product_code} was not found."
        }

    return {
        "found": True,
        "product_code": product_code,
        **product,
    }
@mcp.tool()
def get_products():
    '''
    get the details of all the products
    '''
    return PRODUCTS
    
if __name__=='__main__':
    mcp.run()

