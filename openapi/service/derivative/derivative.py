import json

from openapi.dto.derivative_dto import derivative_dto
from openapi.utils import Constant
from openapi.utils import RequestApi
import requests
from typing import Optional

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
        return derivative_dto.DerivativeResponse[derivative_dto.TotalCashDerivativeResponse].from_json(json.dumps(response_data))
    else:
        response.raise_for_status()

# https://developers.tcbs.com.vn/#tag/asset_derivative/operation/asset_position_close_derivative
# 6.2.1. Asset, position close
def get_asset_position_close(account_id: str, sub_account_id: str, symbol: Optional[str], page_no: int, page_size: int):
    url = f"{Constant.BASE_URL_PRODUCTION}/khronos/v1/account/portfolio/position/close"
    headers = RequestApi.get_headers(Constant.token)
    params = {
        "accountId": account_id,
        "subAccountId": sub_account_id,
        "symbol": symbol,
        "pageNo": page_no,
        "pageSize": page_size
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        response_data = response.json()
        return derivative_dto.DerivativeResponse[derivative_dto.AssetPositionCloseDerivativeResponse].from_json(json.dumps(response_data))
    else:
        response.raise_for_status()

# https://developers.tcbs.com.vn/#tag/asset_derivative/operation/asset_position_open_derivative
# 6.2.2. Asset, position open
def get_asset_position_open(account_id: str, sub_account_id: str):
    url = f"{Constant.BASE_URL_PRODUCTION}/khronos/v1/account/portfolio/status"
    headers = RequestApi.get_headers(Constant.token)
    params = {
        "accountId": account_id,
        "subAccountId": sub_account_id
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        response_data = response.json()
        return derivative_dto.DerivativeResponse[derivative_dto.AssetPositionOpenDerivativeResponse].from_json(json.dumps(response_data))
    else:
        response.raise_for_status()

# https://developers.tcbs.com.vn/#tag/get_order_derivative/operation/list_order_normal_derivative
# 6.3.1. Get list of orders
def get_list_order_normal(page_no: int, page_size: int, account_id: str, symbol: str, order_type: str, status: str):
    url = f"{Constant.BASE_URL_PRODUCTION}/khronos/v1/order/in-day"
    headers = RequestApi.get_headers(Constant.token)
    params = {
        "pageNo": page_no,
        "pageSize": page_size,
        "accountId": account_id,
        "symbol": symbol,
        "orderType": order_type,
        "status": status
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        response_data = response.json()
        return derivative_dto.DerivativeResponse[derivative_dto.ListOrderNormalDerivativeResponse].from_json(json.dumps(response_data))
    else:
        response.raise_for_status()

# https://developers.tcbs.com.vn/#tag/get_order_derivative/operation/list_order_condition_derivative
# 6.3.2. Get list of conditional orders
def get_list_order_condition(page_no: int, page_size: int, account_id: str, sub_account_id: str, order_status: str, order_type: str, symbol: str):
    url = f"{Constant.BASE_URL_PRODUCTION}/khronos/v1/order/condition/detail"
    headers = RequestApi.get_headers(Constant.token)
    params = {
        "pageNo": page_no,
        "PageSize": page_size,
        "accountId": account_id,
        "subAccountID": sub_account_id,
        "orderStatus": order_status,
        "orderType": order_type,
        "Symbol": symbol
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        response_data = response.json()
        return derivative_dto.DerivativeResponse[derivative_dto.ListOrderConditionDerivativeResponse].from_json(json.dumps(response_data))
    else:
        response.raise_for_status()
