import time
import random

from typing import Any


# streaming data injection Primary Streaming Data injection pipeline
def random_detection_streaming_data() -> Any:
    p_data: dict[str, int] = {}
    
    while True:
        time.sleep(1)
        p_data["person"] = random.randrange(1, 10)
        print(p_data)
        
random_detection_streaming_data()