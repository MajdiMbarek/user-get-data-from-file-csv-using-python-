import csv


title = input("title : ").upper()
with open("Favorite TV Shows - Form Responses 1.csv") as file:
    reader = csv.reader(file)
    next(reader)
    counter = 0
    for i in reader:
        if i[1].upper().strip( ) == title:
            counter += 1
    
print(counter)

# snow den