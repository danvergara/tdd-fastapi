"""
tests/test_ping.py
"""


def test_ping(test_app):
    """test the ping endpoint"""
    # Given
    # test_app

    # When
    response = test_app.get("/ping")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev",
        "ping": "pong",
        "testing": True,
    }
