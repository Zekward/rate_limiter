from src.token_bucket import TokenBucket

def test_basic():
    limiter = TokenBucket(capacity=10, refill_rate=1)

    # Should allow first request
    assert limiter.allow_request() == True

    # Should allow up to 10 requests
    for i in range(9):
        assert limiter.allow_request() == True

    # 11th test should fail
    assert limiter.allow_request() == False

    print("Test passed")

if __name__ == "__main__":
    test_basic()
