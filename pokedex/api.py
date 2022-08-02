from aiohttp import ClientSession, TCPConnector

API_URL = "https://api.poketox.me"

async def predict(url, moveset=False):
  if url is None:
    return "Valid url not provided."
  
  async with ClientSession(connector=TCPConnector(verify_ssl=False)) as session:
        response = f'{API_URL}/identify/{url}'
        async with session.get(response) as resp:
            return await resp.text()
