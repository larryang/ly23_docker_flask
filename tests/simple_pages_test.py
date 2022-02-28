"""This test the homepage"""

def test_request_main_menu_links(client):
    """This tests the navbar links"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/page1">Page 1</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Page 2</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Page 3</a>' in response.data
    assert b'<a class="nav-link" href="/page4">Page 4</a>' in response.data

def test_request_index(client):
    """This tests the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"LY23 Bootstrap Index Webpage" in response.data

def test_request_about(client):
    """This tests the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About LY23 Page" in response.data

def test_request_page1(client):
    """This tests page1"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Page 1" in response.data

def test_request_page2(client):
    """This tests page2"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Page 2" in response.data

def test_request_page3(client):
    """This tests page3"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Page 3" in response.data

def test_request_page4(client):
    """This tests page 4"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Page 4" in response.data

def test_request_page_not_found(client):
    """This tests page 5"""
    response = client.get("/page5")
    assert response.status_code == 404
