
import redis

redis_conn = redis.Redis(
    host='localhost',
    port=6379, 
    password='redis_pass')

def redis_test_connection():
    return redis_conn.ping()

def redis_get(key):
    value = redis_conn.get(key)
    return value

def redis_set(key,value):
    response = redis_conn.set(key,value)
    if response =="OK":
        return True
    else:
        return False

def redis_queue_lpush(queue_name,element):
    try:
        redis_conn.lpush(queue_name,element)
    except:
        return False
    return True

def redis_dequeue_rpop(queue_name):
    element = redis_conn.rpop(queue_name)
    return element.decode("utf-8").strip()
    
def redis_dequeue_lpop(queue_name):
    element = redis_conn.rpop(queue_name)
    return element.decode("utf-8").strip()

def  redis_queue_key_exists(queue_name, element):
    return redis_conn.lpos(queue_name,element)

def  redis_delete_key(key):
    return redis_conn.delete(key)