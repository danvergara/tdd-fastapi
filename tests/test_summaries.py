"""tests/test_summaries.py"""

import json


def test_create_summary(test_app_with_db):
    """test the creation of a new summary in db using the edpoint /summaries"""
    response = test_app_with_db.post(
        "/summaries/",
        data=json.dumps({"url": "https://foo.bar"}),
    )

    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


def test_create_summaries_invalid_json(test_app):
    """teste the error handling when the request body is invalid"""
    response = test_app.post("/summaries/", data=json.dumps({}))

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
