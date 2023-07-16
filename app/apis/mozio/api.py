from decouple import config
import time
import requests


class MozioAPI:
    API_KEY = config("API_KEY")
    BASE_URL = config("BASE_URL")
    MAX_POLLING_TIME = 10
    POLLING_TIME = 2
    HEADERS = {
        'Content-Type': 'application/json',
        'API-KEY': API_KEY
    }

    def search(
        self, start_address: str,
        end_address: str,
        mode: str,
        pickup_datetime: str,
        num_passengers: int,
        currency: str,
        campaign: str
    ) -> str:
        url = self.BASE_URL + 'v2/search/'
        body = {
            "start_address": start_address,
            "end_address": end_address,
            "mode": mode,
            "pickup_datetime": pickup_datetime,
            "num_passengers": num_passengers,
            "currency": currency,
            "campaign": campaign,
        }

        response = requests.post(url, json=body, headers=self.HEADERS)
        return response.json()['search_id']

    def poll_search(self, search_id: str) -> list:
        all_results = []
        url = self.BASE_URL + f'v2/search/{search_id}/poll/'
        start_time = time.time()
        result_time = 0
        response = requests.get(url, headers=self.HEADERS)
        while result_time <= self.MAX_POLLING_TIME:
            current_time = time.time()
            result_time = current_time - start_time
            response = requests.get(url, headers=self.HEADERS)
            all_results.append(response.json()['results'])
            if not response.json()['more_coming']:
                break
            time.sleep(self.POLLING_TIME)
      
        return all_results
