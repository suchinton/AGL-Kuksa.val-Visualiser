import asyncio

from kuksa_client.grpc.aio import VSSClient

async def main():
    async with VSSClient('127.0.0.1', 55555) as client:
        current_values = await client.get_current_values([
            'Vehicle.Speed',
        ])
        print(current_values['Vehicle.Speed'].value)

asyncio.run(main())