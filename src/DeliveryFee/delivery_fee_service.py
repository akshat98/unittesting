
from dataclasses import dataclass


@dataclass
class Order():
    id: int
    amount: int
    deliveryfee : int

    def get_amount(self)->int:
        return self.amount

@dataclass
class Location:
    distance: int

    def get_distance(self):
        return self.distance

class DeliveryFeeService:
    order: Order
    location: Location

    def __init__(self, order: Order, location: Location):
        if order.get_amount() < 0:
            raise ValueError("Order amount cannot be negative.")
        if location.get_distance() <= 0:
            raise ValueError("Distance cannot be negative.")

        self.order = order
        self.location = location

    def get_delivery_fee(self) -> float:
        return self.order.get_amount()*0.2 + self.location.get_distance()*0.5
    