"""tests/test_summaries.py"""

import json


def test_create_summary(test_app_with_db):
    """test the creation of a new summary in db using the edpoint /summaries"""
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"}),
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


def test_read_summary(test_app_with_db):
    """test the read a summary action"""
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"}),
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.get(f"/summaries/{summary_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["summary"]
    assert response_dict["created_at"]


def test_read_summary_incorrect_id(test_app_with_db):
    """test failing at look for a summary in db"""
    response = test_app_with_db.get("/summaries/999/")

    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"


def test_read_all_summaries(test_app_with_db):
    """test get all summaries in db"""
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"}),
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == summary_id, response_list))) == 1


def test_remove_summary(test_app_with_db):
    """test remove summary from db"""
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"}),
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.delete(f"/summaries/{summary_id}/")
    assert response.status_code == 200
    assert response.json() == {"id": summary_id, "url": "https://foo.bar"}


def test_remove_summary_incorrect(test_app_with_db):
    """test an expected failure at the time to delete a summary"""
    response = test_app_with_db.delete("/summaries/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "summary not found"


def test_update_summary(test_app_with_db):
    """test update a summary in db"""
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"}),
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.put(
        f"/summaries/{summary_id}/",
        data=json.dumps({"url": "https://foo.bar", "summary": "updated"}),
    )
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["summary"] == "updated"
    assert response_dict["created_at"]


def test_update_summary_incorrect_id(test_app_with_db):
    """test handle error at the time to update a summary with a wrong id"""
    response = test_app_with_db.put(
        "/summaries/999/",
        data=json.dumps({"url": "https://foo.bar", "summary": "updatd"}),
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "summary not found"


def test_update_summary_invalid_json(test_app_with_db):
    """test handle error at the time to update a summary with a wrong json request"""
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"}),
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.put(f"/summaries/{summary_id}/", data=json.dumps({}),)
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "summary"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ],
    }


def test_update_summary_invalid_keys(test_app_with_db):
    """test handle error at the time to update a summary passing a wrong key"""
    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"}),
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.put(
        f"/summaries/{summary_id}/", data=json.dumps({"url": "https://foo.bar"}),
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "summary"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ],
    }
