import subprocess
import concurrent.futures
import time
from datetime import datetime
import csv


# waktu awal
T1 = time.perf_counter()

while(True):
    # waktu awal
    T1 = time.perf_counter()


    with open('/home/fiki/Documents/PSJ_Fiki-Alamsyah/host.cfg') as file:
        readFile = file.read().splitlines()

    # fungsi check host
    def check_host(ip):
        status, result = subprocess.getstatusoutput("ping -c1 " + ip)
        csvFile = open('output.csv', mode='a')
        fieldnames = ['datetime', 'ip', 'up']
        csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames, delimiter=';')
        if (status == 0):
            csvWriter.writerow({'datetime': datetime.now(), 'ip': ip, 'up':'UP'})
            return f"{datetime.now()} : Host {ip} is UP"
        else:
            csvWriter.writerow({'datetime': datetime.now(), 'ip': ip, 'up': 'DOWN'})
            return f'{datetime.now()} : Host {ip} is DOWN'


    # proses multithreading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        print("Mulai monitor......")
        results = executor.map(check_host, readFile)
        for result in results:
            print(result)

        time.sleep(5)

    # waktu akhir
    T2 = time.perf_counter()

    # cetak total waktu
    print(f"selesai dalam : {round(T2 - T1, 2)} detik \n")


