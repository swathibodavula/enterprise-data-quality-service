#Create a function named validate_order_id that accepts an order ID and returns whether it is present and nonblank.

def validate_order_id(order_id: str | None) -> bool:
    """
    Validate the order ID.

    Args:
        order_id (str | None): The order ID to validate.

    Returns:
        bool: True if the order ID is valid, False otherwise."""

    if order_id is None:
        return False

    if isinstance(order_id, str) and order_id.strip() != "":
        return True
    return False

print(validate_order_id("ORD-1001"))  # Returns True
print(validate_order_id(""))          # Returns False
print(validate_order_id(None))        # Returns False
print(validate_order_id("   "))       # Returns False