from tests import myvcr
import requests

@myvcr.use_cassette("google_com.yml")
def test_google():
    response = requests.get("http://google.com")
    assert response.status_code == 200

