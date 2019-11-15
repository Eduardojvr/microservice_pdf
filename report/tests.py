from django.test import TestCase
from django.test import Client
import json

# Create your tests here.

class TestViews(TestCase):
    def setup(self):
        pass

    def test_xsml_all_doctors(self):
        client = Client()
        data = [{"email":"email@gmail.com",
        "segunda":"12:00 ~ 13:00 ",
        "terca":"12:00 ~ 13:00",
        "quarta":"12:00 ~ 13:00",
        "quinta":"12:00 ~ 13:00",
        "sexta":"12:00 ~ 13:00",
        "sabado":"12:00 ~ 13:00",
        "domingo":"12:00 ~ 13:00"}]
        response = client.post('/report/xsml_all_doctors',json.dumps(data), content_type="application/json")
        assert response.status_code == 200

    def test_all_doctors(self):
        client = Client()
        data = [{"email":"email@gmail.com",
        "segunda":"12:00 ~ 13:00 ",
        "terca":"12:00 ~ 13:00",
        "quarta":"12:00 ~ 13:00",
        "quinta":"12:00 ~ 13:00",
        "sexta":"12:00 ~ 13:00",
        "sabado":"12:00 ~ 13:00",
        "domingo":"12:00 ~ 13:00"}]
        response = client.post('/report/all_doctors',json.dumps(data), content_type="application/json")
        assert response.status_code == 200
