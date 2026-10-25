from mcp.server.fastmcp import FastMCP
# create the mcp server
mcp = FastMCP("Procurement Server")

# create the mcp tool
@mcp.tool()
def calculate_purchase_total(unit_price: float, quantity: int) -> float:
    """
    Calculate the total purchase amount.
    """
    return unit_price * quantity


@mcp.tool()
def calculate_discounted_amount(amount: float, discount_percentage: float) -> float:
    """
    Calculate the amount after applying a discount.
    """
    discount = amount * discount_percentage / 100

    return amount - discount


if __name__ == "__main__":
    mcp.run()
