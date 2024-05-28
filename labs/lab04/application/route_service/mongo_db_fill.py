from models.domain.route import CreateRoute


test_data = [
    CreateRoute.model_validate({
        "start_point": "Moscow",
        "destination_point": "Kazan",
        "driver_id": 1,
        "passenger_ids": [2, 3]
    }),
    CreateRoute.model_validate({
        "start_point": "Kazan",
        "destination_point": "Moscow",
        "driver_id": 1,
        "passenger_ids": [2, 3]
    }),
    CreateRoute.model_validate({
        "start_point": "Saint-Petersburg",
        "destination_point": "Moscow",
        "driver_id": 1,
        "passenger_ids": [4]
    })
]

