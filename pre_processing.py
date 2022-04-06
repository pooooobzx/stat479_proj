import csv
with open("Metro_Interstate_Traffic_Volume.csv") as f_in, open("daily_a_month.csv", 'w') as f_out:
    # Write header unchanged
    reader = csv.reader(f_in, delimiter=',')
    writer = csv.writer(f_out, delimiter=',')
    header = next(reader)
    writer.writerow(header)
    previous_date = "2012-10-02"
    temp = []
    rain = []
    snow = []
    clouds_all = []
    traffic_volume = []
    holiday = 0
    count = 1 
    for row in reader:
        if count == 365:
            break
         
        date = row[7].split(" ")[0]
        print(date)
        time = row[7].split(" ")[1]
        print(time)
        if date == previous_date:
            temp.append(float(row[1]))
            rain.append(float(row[2]))
            snow.append(float(row[3]))
            clouds_all.append(float(row[4]))
            traffic_volume.append(float(row[8]))
        else:
            try:
                colValues = [holiday, round(sum(temp)/len(temp), 2), round(sum(rain)/len(rain), 2), round(sum(snow)/len(snow), 2), round(sum(clouds_all)/len(clouds_all), 2), 0, 0, previous_date,round(sum(traffic_volume)/len(traffic_volume), 2)]
            except:
                previous_date = date
                temp = []
                rain = []
                snow = []
                clouds_all = []
                traffic_volume = []
                holiday = 0 if row[0] == "None" else 1
                continue 
                
            previous_date = date
            temp = []
            rain = []
            snow = []
            clouds_all = []
            traffic_volume = []
            holiday = 0 if row[0] == "None" else 1
            writer.writerow(colValues)
            count += 1 
        

        
    