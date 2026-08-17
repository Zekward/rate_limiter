from src.token_bucket import TokenBucket

def test_basic():
    fake_time = 0.0

    def mock_time():
        return fake_time

    limiter = TokenBucket(capacity=10, refill_rate=2, time_fn=mock_time)

    # Should allow first request at time 0, 10 tokens
    print(f"inital count: {limiter.get_tokens_remaining()}")

    # Should allow up to 10 requests
    for i in range(10):
        assert limiter.allow_request() == True
        print(f"current count now: {limiter.get_tokens_remaining()}")

    # 11th test should fail
    assert limiter.allow_request() == False

    assert limiter.current_count == 0

    fake_time = 4.0
    print(f"after 4 seconds: {limiter.get_tokens_remaining()}")

    for i in range(3):
        limiter.allow_request()

    print(f"after another three requests: {limiter.get_tokens_remaining()}")

    print("Tests passed")

if __name__ == "__main__":
    test_basic()
