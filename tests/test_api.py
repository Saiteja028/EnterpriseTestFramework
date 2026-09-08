def test_getProducts(apireq):
    res = apireq.get("/productsList")
    assert res.status==200
    
    # print(res.status)

def test_post(apireq):
    res = apireq.post(url="productsList",data={
        "name":"sai"
    })
    assert res.status==200
    # print(res)

def test_getAllBrandsList(apireq):
    res = apireq.get("/brandsList")
    assert res.status==200

def test_searchProduct(apireq):
    res = apireq.post(url="searchProduct", params={"search_product": "top"})
    assert res.status==200
    # print(res)