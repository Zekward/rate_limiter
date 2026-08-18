from src.token_bucket import TokenBucket

import time

class testTime:
    def __init__(self):
        self.current_time = time.time()

    def __call__(self):
        return self.current_time



def test_initial_capacity():
    """Initially, bucket should be full"""
    limiter = TokenBucket(capacity=10, refill_rate=2)
    assert limiter.get_tokens_remaining() == 10

def test_consume_tokens():
    """Tokens should be consumed one per request"""
    test_time = testTime()
    limiter = TokenBucket(capacity=10, refill_rate=2, time_fn=test_time)

    for i in range(10):
        assert limiter.allow_request() == True

    assert limiter.allow_request() == False

def test_refill_over_time():
    """After time passes, tokens should refill"""
    test_time = testTime()

    limiter = TokenBucket(capacity=10, refill_rate=2, time_fn=test_time)

    for i in range(10):
        limiter.allow_request()

    assert limiter.get_tokens_remaining() == 0

    test_time.current_time += 4.0

    assert limiter.get_tokens_remaining() == 8

def test_capacity_never_exceeds_max():
    test_time = testTime()

    limiter = TokenBucket(capacity=10, refill_rate=2, time_fn=test_time)
    test_time.current_time += 100.0
    assert limiter.get_tokens_remaining() == 10

def test_invalid_capacity():
    try:
        limiter = TokenBucket(capacity=-5, refill_rate=1)
        assert False, "should have raised error"
    except ValueError:
        pass

  


