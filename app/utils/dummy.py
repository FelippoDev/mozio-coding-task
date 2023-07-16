class Dummy:
    first_name = "Luiz Felippo"
    last_name = "Coelho"
    email = "coelho.luizfelippo@gmail.com"
    phone_number = "8776665544"
    country_code_name = "US"
    start_address = "44 Tehama Street, San Francisco, CA, USA"
    end_address = "SFO"
    mode = "one_way"
    pickup_datetime = "2023-12-01 15:30"
    num_passengers = 2
    currency = "USD"
    campaign = "Luiz Felippo dos Santos Coelho"

    def select_transportation(self, results: list) -> str:
        lower_price = 999999
        result_id = None
        for providers in results:
            for data in providers:
                if "Dummy External Provider" in data['steps'][0]['details']['provider_name']:
                    price = float(data['steps'][0]['details']['price']['price']['value'])
                    if price < lower_price:
                        lower_price = price
                        result_id = data['result_id']
        
        return result_id
