from dataclasses import dataclass
from model.order import Order

@dataclass
class Store:
    u: Order
    v: Order
    peso: int