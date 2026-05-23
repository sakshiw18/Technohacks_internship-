import time
import threading


class TokenBucket:
    def __init__(self, capacity, refill_rate):
        """
        capacity: Maximum number of tokens in the bucket
        refill_rate: Tokens added per second
        """
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()
        self.lock = threading.Lock()

    def refill(self):
        """Refill tokens based on elapsed time"""
        current_time = time.time()
        elapsed_time = current_time - self.last_refill

        added_tokens = elapsed_time * self.refill_rate

        if added_tokens > 0:
            self.tokens = min(
                self.capacity,
                self.tokens + added_tokens
            )
            self.last_refill = current_time

    def allow_request(self, tokens_needed=1):
        """Check if request can be allowed"""
        with self.lock:
            self.refill()

            if self.tokens >= tokens_needed:
                self.tokens -= tokens_needed
                return True
            else:
                return False


# Demonstration
if __name__ == "__main__":

    # Bucket with capacity 5 and refill rate 1 token/sec
    bucket = TokenBucket(capacity=5, refill_rate=1)

    for i in range(10):

        if bucket.allow_request():
            print(f"Request {i+1}: Allowed ✅")
        else:
            print(f"Request {i+1}: Blocked ❌")

        time.sleep(0.5)