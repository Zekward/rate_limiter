import time

class TokenBucket:
    """
    Token bucket rate limiter per user

    Args: 
        capacity: Max tokens in bucket
        refill_rate: Tokens per second
        current_count: Number of tokens available
        last_refill_time: Time at the last request
    """

    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.current_count = capacity
        self.last_refill_time = time.time()

    def allow_request(self):
        """
        Check if request is allowed

        Returns:
            bool: True if within limit, False if throttled
        """
        pass

    def get_tokens_remaining(self):
        pass