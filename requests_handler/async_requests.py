import httpx


async def async_get(url: str, return_json: bool = True):
    async with httpx.AsyncClient() as client:
        raw_response = await client.get(url)

    if return_json:
        return raw_response.json()
    else:
        return raw_response
