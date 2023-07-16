from apis.mozio.api import MozioAPI
from utils.dummy import Dummy

if __name__ == "__main__":
    MAX_POLLING_TIME = 10
    POLLING_TIME = 2
    dummy = Dummy()
    api = MozioAPI()

    search_id = api.search(
        start_address=dummy.start_address,
        end_address=dummy.end_address,
        mode=dummy.mode,
        pickup_datetime=dummy.pickup_datetime,
        num_passengers=dummy.num_passengers,
        currency=dummy.currency,
        campaign=dummy.campaign,
    )
    result = api.poll_search(search_id)
    provider_id = dummy.select_transportation(result)
    api.booking(
        search_id,
        provider_id,
        dummy.email,
        dummy.first_name,
        dummy.last_name,
        dummy.country_code_name,
        dummy.phone_number
    )
    reservation_id = api.poll_booking(search_id)
    api.cancellation(reservation_id)
