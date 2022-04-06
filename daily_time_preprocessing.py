import csv
with open("Metro_Interstate_Traffic_Volume.csv") as f_in, open("selected_hr.csv", 'w') as f_out:
    # Write header unchanged
    reader = csv.reader(f_in, delimiter=',')
    writer = csv.writer(f_out, delimiter=',')
    header = next(reader)
    writer.writerow(header)
    count  = 0
    for row in reader:
         
        date = row[7].split(" ")[0]
        time = row[7].split(" ")[1]
        print(time)
        if time in ["06:00:00", "09:00:00", "12:00:00", "15:00:00", "18:00:00", "23:00:00"]:

                
            
            writer.writerow(row)
            count += 1
        

        
    