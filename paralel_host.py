import subprocess
import multiprocessing
import time

# waktu awal
T1 = time.perf_counter()

# index awal
i = 0

# list ip
hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '8.8.8.8', '8.8.4.4']

# fungsi cek host
def check_host():
    status, result = subprocess.getstatusoutput("ping -c1 " + hosts[i])
    if (status == 0):
        print(f'Host {hosts[i]} is UP')
    else:
        print(f'Host {hosts[i]} is DOWN')


Processes = []
# looping multiprocessing
for x in range(len(hosts)):
    P = multiprocessing.Process(target=check_host)
    P.start()
    Processes.append(P)
    # index bertambah
    i += 1

# looping join
for process in Processes:
    process.join()

# waktu akhir
T2 = time.perf_counter()

# cetak total waktu
print(f"selesai dalam : {round(T2 - T1, 2)} detik")
