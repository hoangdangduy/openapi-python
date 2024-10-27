from dataclasses import asdict

import requests
from dacite import Config, from_dict

from openapi.dto.derivative_dto import derivative_dto
from openapi.utils import Constant
from openapi.utils import RequestApi

# https://developers.tcbs.com.vn/#tag/total_cash_derivative/operation/total_cash_derivative
# 6.1.1. Money derivative
def get_total_cash_derivative(account_id, sub_account_id, get_type):
    url = f"{Constant.BASE_URL_PRODUCTION}/khronos/v1/account/status"
    headers = RequestApi.get_headers(Constant.token)
    params = {
        "accountId": account_id,
        "subAccountId": sub_account_id,
        "getType": get_type
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        response_data = response.json()
        config = Config(strict=False)
        return from_dict(data_class=derivative_dto.DerivativeResponse[derivative_dto.TotalCashDerivativeResponse], data=response_data, config=config)
    else:
        response.raise_for_status()

