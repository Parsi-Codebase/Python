from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Procurement Server")


@mcp.tool()
def calculate_total(
    price: float,
    quantity: int
) -> float:
    """
    Calculate the total cost.
    """
    return price * quantity


@mcp.tool()
def calculate_discount(
    amount: float,
    percentage: float
) -> float:
    """
    Calculate the discount amount.
    """
    return amount * percentage / 100


if __name__ == "__main__":
    mcp.run()