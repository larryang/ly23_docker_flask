"""This test the homepage"""

def test_request_main_menu_links(client):
    """This tests the navbar links"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/">Home</a>' in response.data
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/python_dev">Python Dev</a>' in response.data
    assert b'<a class="nav-link" href="/aaa_testing">AAA Testing</a>' in response.data
    assert b'<a class="nav-link" href="/oop">Object Orientated Programming</a>' in response.data
    assert b'<a class="nav-link" href="/solid">SOLID/Design Pattern</a>' in response.data

def test_request_index(client):
    """This tests the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"LY23 IS601 2022 Spring Project 1" in response.data
    assert b"carousel" in response.data

def test_request_about(client):
    """This tests the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About LY23 Page" in response.data
    assert b"software engineer" in response.data

def test_request_git(client):
    """This tests git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Using Git" in response.data

def test_request_docker(client):
    """This tests docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Using Docker" in response.data

def test_request_python(client):
    """This tests python and flask page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Using Python and Flask" in response.data

def test_request_cicd(client):
    """This tests CI/CD page """
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"Implementing Continuous Integration and Continuous Delivery" in response.data

def test_request_python_dev(client):
    """This tests Python Development page"""
    # for pylint & others
    response = client.get("/python_dev")
    assert response.status_code == 200
    assert b"Python Development" in response.data

def test_request_aaa(client):
    """"This tests AAA Testing page"""
    response = client.get("/aaa_testing")
    assert response.status_code == 200
    assert b"Arrange, Act, Assert Testing" in response.data

def test_request_oop(client):
    """This tests OOP page"""
    response = client.get("/oop")
    assert response.status_code == 200
    assert b"Object Orientated Programming" in response.data

def test_request_solid(client):
    """This tests SOLID and Design Patterns page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID and Design Patterns" in response.data

def test_request_page_not_found(client):
    """This tests page 5"""
    response = client.get("/page5")
    assert response.status_code == 404
