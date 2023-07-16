from apis.mozio.api import MozioAPI

if __name__ == "__main__":
    api = MozioAPI()

    search_id = api.search(
        start_address="44 Tehama Street, San Francisco, CA, USA",
        end_address="SFO",
        mode="one_way",
        pickup_datetime="2023-12-01 15:30",
        num_passengers=2,
        currency="USD",
        campaign="Luiz Felippo dos Santos Coelho",
    )
    data = api.polling(search_id)
    