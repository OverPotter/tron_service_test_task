import time


async def test_get_wallet_queries(test_client):
    start_time = time.time()
    response = test_client.get(
        "/api/v1/tron-service/wallets", params={"offset": 0, "limit": 10}
    )
    response_time = time.time() - start_time

    assert response.status_code == 200
    assert response.status_code != 401

    assert response_time < 1.0

    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "application/json"

    assert "error" not in response.json()

    assert isinstance(response.json(), dict)
