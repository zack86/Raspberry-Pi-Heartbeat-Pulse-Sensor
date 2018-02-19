from pulsesensor import Pulsesensor
import time
import datetime
import csv

p = Pulsesensor()
p.startAsyncBPM()

with open('pulse.csv', 'w') as csvfile:
    fieldnames = ['datetime', 'BPM']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    try:
        while True:
            bpm = p.BPM
            if bpm > 0:
                print("BPM: %d" % bpm)
            else:
                print("No Heartbeat found")
            writer.writerow({'datetime': datetime.datetime.now(),
                             'BPM':bpm})
            time.sleep(1)
    except:
        p.stopAsyncBPM()
