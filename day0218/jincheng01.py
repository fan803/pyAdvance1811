from multiprocessing import Pool
import os
def processmain(index):
    print("进程",os.getpid(),"当前循环",index )

if __name__ == "__main__":
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func = processmain, args=(i,))
    pool.close()
    pool.join()