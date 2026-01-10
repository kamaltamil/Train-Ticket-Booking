import csv

class TRAIN:
    train_count=0
    def __init__(self):
        pass

    def add_train(self):
        try:
            add_train=True
            while add_train:
                Train_Name = input(f"{'Train Name':<15}:")
                From_Location=input(f"{'From location':<15}:")
                To_location=input(f"{'To location':<15}:")
                Ticket_Price=int(input(f"{'Ticket Price':<15}:"))
                Seat_Count=int(input(f"{'Seat Count':<15}:"))
                new_train=[Train_Name,From_Location,To_location,str(Ticket_Price),str(Seat_Count)]
                
                added=TRAIN.add(True,new_train)
                if added=='Exist':
                    print('Train is already exist !')
                    return False
                elif added:
                    print('Train Added Successfully!')
                    add=input(f"\n{'Add another train (Y/N) : '}")
                    if add=='Y' or add=='Yes':
                        add_train=True
                    else:
                        add_train=False
            return True
        except ValueError:  return False

    def add(self,new_train):
        try:
            with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\train_list.csv','r') as data:                
                reader=csv.reader(data)
                for row in reader:
                    for j in range(len(row)):
                        if new_train[0]==row[0]:
                            data.close
                            return 'Exist'       
                data.close
            with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\train_list.csv','a+')as data:                
                writer=csv.writer(data)
                writer.writerow(new_train)
                data.close
            return True
        except (FileNotFoundError,PermissionError):   return False