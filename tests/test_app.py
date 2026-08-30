from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_signup_rejects_duplicate_email():
    activity_name = "Chess Club"
    payload = {"email": "michael@mergington.edu"}

    response = client.post(f"/activities/{activity_name}/signup", params=payload)

    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_delete_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "daniel@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    assert response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]
