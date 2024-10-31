from dataclasses import dataclass
from typing import Optional, Generic, TypeVar
from dataclasses_json import dataclass_json

T = TypeVar('T')

@dataclass_json
@dataclass
class DerivativeResponse(Generic[T]):
    cmd: str
    rc: str
    rs: str
    oID: str
    data: T

@dataclass_json
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

@dataclass_json
@dataclass
class AssetPositionCloseDerivativeResponse:
    symbol: str
    side: str
    openPrice: float
    closePrice: float
    closePosition: str
    fee: float
    tax: float
    closeVM: float
    unrealize: float
    closePC: float
    time: str

@dataclass_json
@dataclass
class AssetPositionOpenDerivativeResponse:
    symbol: str
    im: str
    deliver: str
    receive: str
    net: int
    side: str
    account: str
    wasp: float
    wapb: float
    lastPrice: float
    imValue: float
    vmValue: float
    mrValue: float
    duedate: str
    netoffvol: int
    avg_remain: float
    vm_remain: float
    pc_remain: str
    stoploss: Optional[str]
    takeprofit: Optional[str]

@dataclass_json
@dataclass
class ListOrderNormalDerivativeResponse:
    orderNo: str
    pk_orderNo: str
    orderTime: str
    accountCode: str
    side: str
    symbol: str
    volume: int
    showPrice: float
    matchVolume: int
    matchPriceBQ: float
    status: str
    orderStatus: str
    channel: str
    group: str
    cancelTime: Optional[str]
    isCancel: bool
    isAmend: bool
    info: Optional[str]
    maxPrice: Optional[float]
    matchValue: Optional[float]
    quote: Optional[str]
    autoType: Optional[str]
    product: Optional[str]
    orderType: Optional[str]
    source: Optional[str]

@dataclass_json
@dataclass
class ListOrderConditionDerivativeResponse:
    orderNo: str
    groupOrder: str
    pk_orderNo: str
    accountCode: str
    side: str
    symbol: str
    showPrice: float
    volume: int
    condition: str
    result: str
    active_time: str
    send_time: str
    cancel_time: Optional[str]
    group: str
    channel: str
    maxPrice: Optional[float]
    soPrice: float
    orderType: str
    from_time: str
    exp_time: str
    status: str
    details: str
    notes: str

