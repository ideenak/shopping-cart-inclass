from shopping_cart import to_usd, findprod


def test_to_usd():
    result = to_usd(10)
    assert result == "$ 10.00"

def test_findprod():
    
    products = [
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    ]


    idnum_L = []
    
    idnum = 3
        
    idnum_L.append(idnum)
    sum_price = 0
    for i in idnum_L:
        result = findprod(i, sum_price, products,idnum)
    
    assert result == 2.49
