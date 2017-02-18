from {{cookiecutter.package_name}} import sample_module


def test_hello_world():
    response = sample_module.hello_world('Maya')
    assert response == 'Hello, Maya!'
