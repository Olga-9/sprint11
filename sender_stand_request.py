import requests
import configuration
import data

def post_new_orders(body):
    return requests.post(configuration.server_address + configuration.orders,
                         json=body,
                         headers=data.headers)


def get_new_orders_track(track):
    return requests.get(configuration.server_address + configuration.orders_track,
                        params={"t": track})