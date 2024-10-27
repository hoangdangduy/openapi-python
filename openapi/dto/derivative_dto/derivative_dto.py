from dataclasses import dataclass
from typing import List, Optional, Generic, TypeVar

T = TypeVar('T')
@dataclass
class DerivativeResponse(Generic[T]):
    cmd: str
    rc: str
    rs: str
    oID: str
    data: T

@dataclass
class TotalCashDerivativeResponse:
    cash: Optional[float]
    stock: Optional[float]
    collateral: Optional[float]
    type: Optional[str]
    net: Optional[float]
    tyle: Optional[float]
    im: Optional[float]
    vm: Optional[float]
    dm: Optional[float]
    mr: Optional[float]
    avaiCash: Optional[float]
    avaiColla: Optional[float]
    vmunpay: Optional[float]
    info: Optional[str]
    color: Optional[str]
    vm_eod: Optional[float]
    others: Optional[float]
    tax: Optional[float]
    feeCTCK: Optional[float]
    feeHNX: Optional[float]
    cashWithdraw: Optional[float]
    tienbosung: Optional[float]
    cashavaiwithdraw: Optional[float]
    assets: Optional[float]
    nav: Optional[float]
    cashOut: Optional[float]
    unrelizeVM: Optional[float]
    feePos: Optional[float]
    feeMan: Optional[float]
    product: Optional[str]
    status: Optional[str]
    debt: Optional[float]
    w1: Optional[float]
    w2: Optional[float]
    limit: Optional[float]
    package: Optional[str]

