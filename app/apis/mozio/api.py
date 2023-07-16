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
        """Method to create a post request for the API to search for 
        transportations available within the given address

        Returns:
            str: returns the search id from the API request
        """
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
        """Method that creates a for loop to poll the data from the API until exceeds the limit time or 
        'more_coming' key value is false 

        Args:
            search_id (str): ID returned from search method

        Returns:
            list: returns a list containing all the polling results
        """
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

    def booking(
            self,
            search_id: str,
            result_id: str,
            email: str,
            first_name: str,
            last_name: str,
            country_code_name: str,
            phone_number: str
    ) -> dict:
        """_summary_

        Returns:
            dict: returns the API response as a dictionary
        """
        url = self.BASE_URL + 'v2/reservations/'
        body = {
            "search_id": search_id,
            "result_id": result_id,
            "email": email,
            "country_code_name": country_code_name,
            "phone_number": phone_number,
            "first_name": first_name,
            "last_name": last_name,
            "airline": "AA",
            "flight_number": "33",
            "customer_special_instructions": ""
        }

        response = requests.post(url, json=body, headers=self.HEADERS)
        return response.json()

    def poll_booking(self, search_id: str) -> str:
        """Method that creates a for loop to poll the data from the API until exceeds the limit time or 
        the API returns a key value 'status' containing the current status of the API polling

        Args:
            search_id (str): ID returned from search method

        Returns:
            str: returns the booking id
        """
        url = self.BASE_URL + f"v2/reservations/{search_id}/poll/"
        start_time = time.time()
        result_time = 0
        while result_time <= self.MAX_POLLING_TIME:
            current_time = time.time()
            result_time = current_time - start_time
            response = requests.get(url, headers=self.HEADERS)
            if response.json()['status'] == 'completed':
                break

            time.sleep(self.POLLING_TIME)

        return response.json()['reservations'][0]['id']

    def cancellation(self, reservation_id: str) -> dict:
        """Method for creating a delete request to cancel the booking transportation

        Args:
            reservation_id (str): ID from the booking transportation 
            returned by the 'poll_booking' method

        Returns:
            dict: returns the API response as a dictionary
        """
        url = self.BASE_URL + f"v2/reservations/{reservation_id}/"
        response = requests.delete(url, headers=self.HEADERS)

        return response.json()
