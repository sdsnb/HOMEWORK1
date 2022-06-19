import time
def main():
    t = 60
    print("**************进度条**************")
    start = time.perf_counter()
    for i in range(t + 1): 
        finshed = "*" * i 
        need_do = "-" * (t - i) 
        progress = (i / t) * 100 
        durtime = time.perf_counter() - start 
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finshed, need_do, durtime), end="") 
        time.sleep(0.1)