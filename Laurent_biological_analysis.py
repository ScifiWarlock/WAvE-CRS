import pandas as pd
import cmath
import math

#Use to convert the export.xml file to csv
#df = pd.read_xml('export.xml')
#print("xml read")
#df.to_csv('out.csv', index=False, encoding='utf8')
#print("csv saved")

#Analyzed through google sheets to find out important sample statistics
#This process will be dynamic in MVP implementation
#We can assume due to the vast data that it is reflective of the population normal distribution
avg_hr = 96.523
avg_hrv = 102.978
stdev_hrv = 12.283
stdev_hr = 22.246

#Laurent series centered at z=0
l_series_center = complex(0, 0)

#Defining standard deviation linear combination
stdev_combined = complex(stdev_hr, stdev_hrv)

#Ask user to enter biometrics (this will be automated later on)
print("Enter the heartrate in beats per minute")
hr = int(input())
print("Enter the hrv sdnn")
hrv = int(input())

p_complex = complex(hr-avg_hr, hrv - avg_hrv)

if p_complex == l_series_center:
    print("Fatigue not likely")

elif p_complex != l_series_center and abs(p_complex) < abs(stdev_combined)*math.sqrt(2):
    print("Fatigue not likely")

elif p_complex != l_series_center and abs(p_complex) > abs(stdev_combined)*math.sqrt(2):
    print("Fatigue is a possibility. Contacting servers and verifying with facial detection model...")
    #stdf = pd.read_excel("df.xlsx")
    #stdf.loc[cur_month, 'Logs'] += 1
    #stdf.to_excel("df.xlsx")
