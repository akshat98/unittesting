import pytest_mock
import pytest
from math import isclose

from DeliveryFee.delivery_fee_service import *


@pytest.fixture
def order_instance():
    return Order(1,0,10)

@pytest.fixture
def location_instance():
    return Location(10)



def test_order(order_instance):
    assert order_instance.get_amount() == 0

def test_location(location_instance):
    assert location_instance.get_distance() == 10

    

def test_failing_delivery_fee(order_instance, location_instance):
    with pytest.raises(ValueError):
        deliveryService = DeliveryFeeService(order_instance, location_instance)


def test_delivery_fee_mocker(mocker):
    order_mock = mocker.Mock(spec=Order)
    location_mock = mocker.Mock(spec=Location)

    #setting return values 
    order_mock.get_amount.return_value = 10
    location_mock.get_distance.return_value = 20

    service: DeliveryFeeService = DeliveryFeeService(order_mock, location_mock)
    assert True == isclose(service.get_delivery_fee(),10*0.2+20*0.5)


