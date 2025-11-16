import os
import subprocess
import time
import re


while True:
    result = subprocess.run(["ping", "1.1.1.1"], stdout=subprocess.PIPE, text=True)

    match =  re.search(r'time[<=](\d+)ms', result.stdout)
    
    if match: 
        latency = int(match.group(1))
        if latency > 50:
            print(f"HIGH LATENCY: {latency}ms")
                  
    else:
            print("Ping failed or no latency info found.")     
            

    #print(result.stdout)
    time.sleep(1)


