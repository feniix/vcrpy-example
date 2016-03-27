from tests import myvcr
import requests

import vcrex

@myvcr.use_cassette("google_com.yml")
def test_google():
    response = vcrex.google_body()
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"

