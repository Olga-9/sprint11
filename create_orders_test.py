import sender_stand_request
import data

def get_order_track():
    response = sender_stand_request.post_new_orders(data.order_body)

    return response.json()['track']


def test_order_data_by_order_track():
    track = get_order_track()
    response = sender_stand_request.get_new_orders_track(track)
    assert response.status_code == 200

# Ольга Белова, 17-я когорта — Финальный проект. Инженер по тестированию плюс