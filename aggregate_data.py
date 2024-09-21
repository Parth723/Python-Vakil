import time
import threading

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests = {}
        self.lock = threading.Lock()

    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()
            if user_id not in self.user_requests:
                self.user_requests[user_id] = []

            self.user_requests[user_id] = [
                timestamp for timestamp in self.user_requests[user_id]
                if current_time - timestamp < self.time_window
            ]

            if len(self.user_requests[user_id]) < self.max_requests:
                self.user_requests[user_id].append(current_time)
                return True
            else:
                return False

rate_limiter = RateLimiter()

user_id = "user_1"
for i in range(10):
    if rate_limiter.allow_request(user_id):
        print(f"Request {i + 1} allowed")
    else:
        print(f"Request {i + 1} denied")
    time.sleep(5)  
