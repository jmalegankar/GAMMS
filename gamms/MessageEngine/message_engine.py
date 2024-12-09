from typing.message_engine import IMessageEngine, IMessage
import redis
import threading

class MessageEngine(IMessageEngine):

    def __init__(self, host: str = "127.0.0.1", port: int = 6379):
        self.host = host
        self.port = port
        self.redis_client = None
        self.pubsub = None
        self.subscriber_thread = None

    def connect_redis(self):
        if not self.redis_client:
            #initialize redis client
            self.redis_client = redis.StrictRedis(
                host=self.host, port=self.port, db=self.db, decode_responses=True
            )
            #initialize pubsub
            self.pubsub = self.redis_client.pubsub()
            print(f"Connected to Redis at {self.host}:{self.port}")
    
    def disconnect_redis(self):
        #close redis connection

        if self.pubsub:
            self.pubsub.close()
        self.redis_client = None
        self.pubsub = None
        print("Disconnected from Redis.")

    def publish(self, channel: str, message: IMessage):
        if not self.redis_client:
            raise ConnectionError("Redis is not connected. Call `connect` first.")
        self.redis_client.publish(channel, message)   

    def subscribe(self, channel: str, callback: callable):
        if not self.pubsub:
            raise ConnectionError("Redis is not connected. Call `connect` first.")
        
        def listen():
            self.pubsub.subscribe(channel)
            for message in self.pubsub.listen():
                if message["type"] == "message":
                    callback(message["data"])

        if not self.subscriber_thread or not self.subscriber_thread.is_alive():
            self.subscriber_thread = threading.Thread(target=listen)
            self.subscriber_thread.start()
            print(f"Subscribed to {channel}.")
    
    def unsubscribe(self, channel: str):
        if not self.pubsub:
            raise ConnectionError("Redis is not connected. Call `connect` first.")
        self.pubsub.unsubscribe(channel)
    
    def generate_channel_name(self):
        pass
    def list_active_channels(self):
        if not self.redis_client:
            raise ConnectionError("Redis is not connected. Call `connect` first.")
        return self.redis_client.pubsub_channels()