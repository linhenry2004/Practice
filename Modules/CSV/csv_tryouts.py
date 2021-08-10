import csv

filename = '/Users/henrylin/Python/Modules/CSV/csvReport.csv'
filename2 = '/Users/henrylin/Python/Modules/CSV/csvReport2.csv'
filename3 = '/Users/henrylin/Python/Modules/CSV/csvReport3.csv'
filename4 = '/Users/henrylin/Python/Modules/CSV/csvReport4.csv'

#reader() method
with open(filename) as csvfile: 
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print()

#DictReader() method
with open (filename) as csvfile: 
    DictReader = csv.DictReader(csvfile)
    for row in DictReader: 
        print(row)

with open (filename) as csvfile: 
    DictReader = csv.DictReader(csvfile)
    for row in DictReader:
        print(row['Revenue'], row['Location'])

print()

#open() and close() method: Different way to open and close instead of with open() as filename
csvfile = open(filename2, 'w', newline='') #Using newline='' makes sure no extra spaces when changing to a newline
csvfile.close()

#writer() and writerow()
with open(filename2, 'w', newline = '') as csvfile: 
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])

print()

#delimiter 分隔符號
with open(filename3, 'w', newline = '') as csvfile: 
    csvWriter = csv.writer(csvfile, delimiter = '\t')
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])

print()

#DictWriter()
with open(filename4, 'w', newline = '') as csvfile: 
    fields = ['Name', 'Age', 'City']
    DictWriter = csv.DictWriter(csvfile, fieldnames=fields)
    DictWriter.writerow({'Name':'Hung', 'Age':'35', 'City':'Taipei'})
    DictWriter.writerow({'Name':'James', 'Age':'40', 'City':'Chicago'})

print()