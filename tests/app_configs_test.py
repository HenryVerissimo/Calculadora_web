import pytest
from app import create_app


@pytest.mark.parametrize(
    "env, expected",
    [
        ("DEVELOPMENT", {"DEBUG": True, "TESTING": False, "TEMPLATES_AUTO_RELOAD": True}),
        ("TESTING", {"DEBUG": True, "TESTING": True, "TEMPLATES_AUTO_RELOAD": False}),
        ("PRODUCTION", {"DEBUG": False, "TESTING": False, "TEMPLATES_AUTO_RELOAD": False})
    ]
)
def test_app_configurations(env, expected):
    """ Testing Application Environment Configurations """

    app = create_app(env)
    expected = dict(expected)

    for key, value in expected.items():
        assert app.config[key] == value
