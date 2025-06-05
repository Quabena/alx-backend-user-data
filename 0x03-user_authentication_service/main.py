#!/usr/bin/env python3
"""
Main test module for Flask authentication app.
Uses `requests` to call endpoints and validates responses.
"""

import requests


BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Register a new user"""
    res = requests.post(f"{BASE_URL}/users",
                        data={"email": email, "password": password})
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "user created"}

    # Re-registering same user should fail
    res = requests.post(f"{BASE_URL}/users",
                        data={"email": email, "password": password})
    assert res.status_code == 400
    assert res.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempt to login with the wrong password"""
    res = requests.post(f"{BASE_URL}/sessions",
                        data={"email": email, "password": password})
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """Login and return session ID"""
    res = requests.post(f"{BASE_URL}/sessions",
                        data={"email": email, "password": password})
    assert res.status_code == 200
    assert res.json().get("email") == email
    assert res.json().get("message") == "logged in"
    return res.cookies.get("session_id")


def profile_unlogged() -> None:
    """Try accessing profile without being logged in"""
    res = requests.get(f"{BASE_URL}/profile")
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """Access profile with valid session_id cookie"""
    res = requests.get(f"{BASE_URL}/profile",
                       cookies={"session_id": session_id})
    assert res.status_code == 200
    assert "email" in res.json()


def log_out(session_id: str) -> None:
    """Logout using session cookie"""
    res = requests.delete(f"{BASE_URL}/sessions",
                          cookies={"session_id": session_id})
    assert res.status_code == 200
    assert res.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """Request a password reset token"""
    res = requests.post(f"{BASE_URL}/reset_password", data={"email": email})
    assert res.status_code == 200
    assert "reset_token" in res.json()
    return res.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Use reset_token to set a new password"""
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    res = requests.put(f"{BASE_URL}/reset_password", data=data)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "Password updated"}


# Constants
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
