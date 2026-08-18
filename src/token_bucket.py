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

    def __init__(self, capacity, refill_rate, time_fn=time.time):
        if capacity <= 0:
            raise ValueError("capacity must be greater than 0")
        if refill_rate <= 0:
            raise ValueError("refill rate must be greater than 0")

        self.capacity = capacity
        self.refill_rate = refill_rate
        self.current_count = capacity
        self.last_refill_time = time_fn()
        self.time_fn = time_fn

    def allow_request(self):
        """
        Check if request is allowed

        Returns:
            bool: True if within limit, False if throttled
        """
        self.current_count = self.get_tokens_remaining()
        self.last_refill_time = self.time_fn()
        # check if alloweed, consume if yes, return
        if self.current_count >= 1:
            self.current_count -= 1
            return True
        return False

    def get_tokens_remaining(self):
        # calculate elapsed time
        elapsed_time = self.time_fn() - self.last_refill_time
        # calculate tokens to add
        new_tokens = elapsed_time * self.refill_rate
        return min(self.capacity, self.current_count + new_tokens)