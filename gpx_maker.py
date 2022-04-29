#!/usr/bin/env python3

with open("out.csv", "r") as gps_data:
	file_content = gps_data.read()
	header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<gpx xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://www.topografix.com/GPX/1/1\" xsi:schemaLocation=\"http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.topografix.com/GPX/gpx_style/0/2 http://www.topografix.com/GPX/gpx_style/0/2/gpx_style.xsd\" xmlns:gpxtpx=\"http://www.garmin.com/xmlschemas/TrackPointExtension/v1\" xmlns:gpxx=\"http://www.garmin.com/xmlschemas/GpxExtensions/v3\" xmlns:gpx_style=\"http://www.topografix.com/GPX/gpx_style/0/2\" version=\"1.1\" creator=\"https://gpx.studio\">\n<metadata>\n<name>new</name>\n<author>\n<name>gpx.studio</name>\n<link href=\"https://gpx.studio\">\n</link>\n</author>\n</metadata>\n<trk>\n<name>new</name>\n<type>Test_gpx_maker</type>\n<trkseg>"
	footer = "</trkseg>\n</trk>\n</gpx>"

w = open("output.gpx", "a")
w.write(f"{header}\n")

# Parsing du fichier en input
Data_base = file_content.replace("\n", ",")
Data_base = Data_base.split(",")
lon = Data_base[1:len(Data_base):4]
lat = Data_base[2:len(Data_base):4]
ele = Data_base[3:len(Data_base):4]
for i in range (0, len(lon)):
	w.write(f"<trkpt lat=\"{lon[i]}\" lon=\"{lat[i]}\">\n<ele>{ele[i]}</ele>\n</trkpt>\n")

w.write(f"\n{footer}")
w.close()