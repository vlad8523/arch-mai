from datetime import datetime, timedelta
from typing import Dict

from config import settings


FAIL_COUNT = 1
TIME_LIMIT = timedelta(seconds=5)
SUCCESS_LIMIT = 5

class CircuitState:
    def __init__(self) -> None:
        self.fail_count: int  = 0
        self.success_count: int = 0
        
        self.current_state: int = 2 # 0 - open, 1 - semi-open, 2 - closed
        self.state_time: float


class CircuitBreaker:
    services: Dict[str, CircuitState] = {}

    def check(self, service_name: str) -> bool:
        if service_name not in self.services:
            self.services[service_name] = CircuitState()

        service = self.services[service_name]

        print(f"CIRCUIT BRAKER: service: {service_name}, state {service.current_state}, fail {service.fail_count}, success {service.success_count}")

        if service.current_state == 2 or service.current_state == 1:
            return True
        
        # if service.current_state is open
        end = datetime.now()

        elapsed_time = end - service.state_time
        print(elapsed_time)
        if (elapsed_time >= TIME_LIMIT):
            print("CIRCUIT BRAKER: time limit reached")
            service.current_state = 1
            service.success_count = 0
            service.fail_count = 0

    
    def fail(self, service_name: str):
        print(f"CIRCUIT BREAKER: fail for service {service_name}")
        if service_name not in self.services:
            service = CircuitState()
            service.fail_count = 1
            self.services[service_name] = service
        else:
            service = self.services[service_name]

            if service.current_state == 2:
                service.state_time = datetime.now()

                service.fail_count += 1

                if service.fail_count > FAIL_COUNT:
                    print("CIRCUIT BREAKER: error limit is reached")
                    service.current_state = 0
            elif service.current_state == 1:
                service.current_state = 0
                service.state_time = datetime.now()
                service.success_count = 0

            # self.services[service_name] = service

    def success(self, service_name: str):
        if service_name in  self.services:
            service = self.services[service_name]

            if service.current_state == 1:
                service.success_count += 1

                if service.success_count > SUCCESS_LIMIT:
                    print(f"CIRCUIT BREAKER: success limit reached for service {service_name}")
                    service.current_state = 2

                    service.success_count = 0
                    service.fail_count = 0

            self.services[service_name] = service


circuit_breaker = CircuitBreaker()
