import asyncio
import aioredis

# Redis connection
redis = aioredis.from_url("redis://localhost", decode_responses=True)

# Publisher - sending a message
async def publish_message(room_id, message):
    channel = f"room:{room_id}"
    await redis.publish(channel, message)
    print(f"Published to {channel}: {message}")

# Subscriber - receiving messages
async def subscribe_room(room_id):
    channel = f"room:{room_id}"
    pubsub = redis.pubsub()
    await pubsub.subscribe(channel)
    print(f"Subscribed to {channel}")

    async for msg in pubsub.listen():
        if msg['type'] == 'message':
            print(f"Received in {channel}: {msg['data']}")

# Example usage
async def main():
    # Run subscriber in background
    asyncio.create_task(subscribe_room("1234"))

    # Publish some messages
    await asyncio.sleep(1)
    await publish_message("1234", "Hello Everyone!")
    await asyncio.sleep(1)
    await publish_message("1234", "How are you all?")

asyncio.run(main())