from {{cookiecutter.project_slug}}.main import hello


def test_hello():
    assert hello("Test") == "Hello, Test!"


def test_hello_default():
    assert hello() == "Hello, World!"
