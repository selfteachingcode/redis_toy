from termios import VLNEXT
import redis_toy
from redis_toy import redis_conn
# check redis connection
print(redis_toy.redis_test_connection())

# set value and get value
redis_toy.redis_set(key="1a", value="1st Set")
print(redis_toy.redis_get(key="1a"))

# push and pop into a list
redis_toy.redis_queue_lpush(queue_name='tool_list', element="redis")
redis_toy.redis_queue_lpush(queue_name='tool_list', element="docker")
redis_toy.redis_queue_lpush(queue_name='tool_list', element="celery")
redis_toy.redis_queue_lpush(queue_name='tool_list', element="rabbitmq")
print(redis_conn.lrange(name='tool_list', start=0, end=4))

