from httpx import AsyncClient


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/operations/", json={
        "id": 1,
        "quantity": "25.5",
        "figi": "code",
        "instrument_type": "bond",
        "date": "2023-04-10T17:17:25.29",
        "type": "Выплата",
    })
    assert response.status_code == 200, "Add operation test failed"


async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get("/operations/", params={
        "operation_type": "Выплата",
    })
    assert response.status_code == 200