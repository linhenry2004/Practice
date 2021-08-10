import csv

filename = '/Users/henrylin/Python/Practice/Class Practice and CSV Module/class_practice.csv'

class Student (): 
    subjects = ['Science', 'Math', 'English']
    def __init__ (self, ID, first, last, score1, score2, score3): 
        self.first = first
        self.last = last
        self.ID = ID
        self.scores = [score1, score2, score3]
        with open (filename, 'r') as file1:
            csv_reader = csv.reader(file1) 
            temp = False
            for row in csv_reader: 
                if row[0] == ID:
                    temp = True
                    break
            if temp == False: 
                with open (filename, 'a') as file2: 
                        file2.write(ID + ',' + first + ',' + last + ',' + str(score1) + ',' + str(score2) + ',' + str(score3) + '\n')

    def changeScore (self, subject, score): 
        for i in range(3): 
            if self.subjects[i] == subject: 
                self.scores[i] = score
                temp_list = readfile(filename)
                for j in temp_list: 
                    if j[0] == self.ID: 
                        j[i+3] = str(score)
                writefile(temp_list)

    def getScore (self, subject): 
        for i in range(3):
            if self.subjects[i] == subject: 
                return self.scores[i]
    def getName (self):
        return self.first + ' ' +  self.last
    def getAvg (self): 
        average = 0
        for score in self.scores: 
            average += score
        return average / len(self.scores)

def readfile (filename):
    temp_list = []
    with open (filename, 'r') as csvfile: 
                    csv_reader = csv.reader(csvfile)
                    for row in csv_reader: 
                        sub_list = []
                        for i in row: 
                            sub_list.append(i)
                        temp_list.append(sub_list)
    return temp_list  

def writefile (whole_list): 
    with open (filename, 'w') as file: 
        for i in whole_list: 
            for j in range(len(i) - 1):
                file.write(i[j] + ',')
            file.write(i[-1] + '\n') 

def stuAvg (subject, *args): 
    average = 0
    length = 0
    for arg in args: 
        temp = arg.getScore(subject)
        average += temp
        length += 1
    return average/length

my_list = []

with open ('/Users/henrylin/Python/Practice/Class Practice and CSV Module/class_practice.csv', 'r') as file: 
    reader = csv.reader(file)
    for row in reader: 
        my_list.append(Student(row[0], row[1], row[2], int(row[3]), int(row[4]), int(row[5])))

my_list[2].changeScore('English', 90)
print('%s\'s average is' % my_list[0].getName(), my_list[0].getAvg())
print('%s\'s Math score is' % my_list[1].getName(), my_list[1].getScore('Math'))
print('The average score of Science is:', stuAvg('Science', *my_list))
print('The average score of Math is:', stuAvg('Math', *my_list))
print('The average score of English is:', stuAvg('English', *my_list))