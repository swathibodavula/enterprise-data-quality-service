from src.data_quality.validator import validate_order_id

def test_valida_order_id():
    #Test with a valid order ID
    assert validate_order_id("ORD-1001") == True

    #Test with an empty string
    assert validate_order_id("") == False

    #Test with None
    assert validate_order_id(None) == False

    #Test with a string containing only whitespace
    assert validate_order_id("   ") == False