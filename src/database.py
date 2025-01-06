import os

# Create / Read / Update / Delete

# file
def Create_file () :
    

    
def save (user_id, data) :

    file = "../info.csv"
    
    with open(file, mode = "r", encoding = "utf-8") as f :
        reader = csv.reader(f)
        rows = list(reader)

    rows.append(data)

    with open(file, mode = "w", encoding = "utf-8", newline = "") as f :

        writer = csv.writer(f)
        writer.writerows(rows)
