import requests
from dacite import from_dict, Config

from openapi.dto.account.AccountInformationResponse import AccountInformationResponse
from openapi.utils import Constant
from openapi.utils import RequestApi


# https://developers.tcbs.com.vn/#tag/account/operation/get_sub_account_information
def get_subaccount_info(custody_code, fields):
    url = f"{Constant.BASE_URL_PRODUCTION}/eros/v2/get-profile/by-username/{custody_code}"
    headers = RequestApi.get_headers(Constant.token)
    params = {
        "fields": fields
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        response_data = response.json()
        config = Config(strict=False)
        account_info_response = from_dict(data_class=AccountInformationResponse, data=response_data, config=config)
        return account_info_response
    else:
        response.raise_for_status()
