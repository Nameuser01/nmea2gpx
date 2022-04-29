#!/usr/bin/env python3

from datetime import datetime
import math
import csv

with open(dbfile, 'r') as entree:
    with open(out.csv, 'wt') as sortie:
        reader = csv.reader(entree)
        writer = csv.writer(sortie, delimiter=',', lineterminator='\n')
        for row in reader:
            if not row[0].startswith('$GPRMC'):
                continue
            else:
                time = row[1]
                warning = row[2]
                lat = row[3]
                lat_direction = row[4]
                lon = row[5]
                lon_direction = row[6]
                speed = row[7]
                date = row[9]
                if warning == 'V':
                    continue

                date_and_time = datetime.strptime(date + ' ' + time, '%d%m%y %H%M%S.%f')
                date_and_time = date_and_time.strftime('%y-%m-%d %H:%M:%S.%f')[:-3]
                lat = round(math.floor(float(lat) / 100) + (float(lat) % 100) / 60, 6)
                if lat_direction == 'S':
                    lat = lat * -1
                lon = round(math.floor(float(lon) / 100) + (float(lon) % 100) / 60, 6)
                if lon_direction == 'W':
                    lon = lon * -1
                speed = int(round(float(speed) * 1.852, 0))
                writer.writerow([date_and_time, lat, lon, speed])
