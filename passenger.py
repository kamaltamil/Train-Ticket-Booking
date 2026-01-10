import csv

class Passenger:
    def __init__(self):
        pass

    def option():
        try:
            option=int(input(f"--------------\n{' Option ':<10}: "))
            print('--------------')
        except ValueError:return
        return option

    def passenger():
        passenger=True
        while passenger:
            print('1.Signup \n2.Login \n3.Back')
            match Passenger.option():
                case 1:
                    new_pnr=Passenger.signup()
                    if new_pnr=='Exist':    print('User already signup!')
                    elif new_pnr:   print('Account created sucessfully')
                    else:   print('Account creation failed!')
                case 2:
                    login_success=Passenger.login()
                    if login_success:
                        print('-------------------\nLogin Successfull!\n-------------------')
                        booked=Passenger.booking(login_success)
                        if booked:  print('Booking Successfull')
                        else:   print('Booking Failed')
                    else:
                        print('Login failed....')
                case 3:return True

    def signup():
        try:
            name=input(f"{'Name ':<14}:")
            address=input(f"{'Address ':<14}:")
            phone_num=int(input(f"{'Phone Number ':<14}:"))
            pwd=input(f"{'Password ':<14}:")
            seat_booked=0
            new_user=[name,address,phone_num,pwd,seat_booked]
            try:
                with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\passenger_list.csv','r')as data:                
                    reader=csv.reader(data)
                    for row in reader:
                        for j in range(len(row)):
                            if str(new_user[2])==row[2]:
                                data.close()
                                return 'Exist'       
                data.close()
                with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\passenger_list.csv','a+')as data:                
                    writer=csv.writer(data)
                    writer.writerow(new_user)
                data.close()
                return True
            except (FileNotFoundError,PermissionError):
                return False
        except ValueError:  
            return False

    def login():
        try:
            phone_num=int(input(f"{'Phone Number ':<14}:"))
            password=input(f"{'Password ':<14}:")
            try:
                with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\passenger_list.csv','r')as data:                
                    reader=csv.reader(data)
                    for row in reader:
                        for j in range(len(row)):
                            if str(phone_num)==row[2] and str(password)==row[3]:
                                data.close()
                                return [phone_num,password]
                    else:       
                        data.close()
                        return False
            except (FileNotFoundError,PermissionError):   return False
        except ValueError: return False

    def booking(user):
        try:
            seat_require=0
            flag=False
            updated=[]
            from_location=input(f"{'From location ':<20}:")
            to_location=input(f"{'Destination location ':<20}:")
            try:
                with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\train_list.csv','r')as data:
                    reader=csv.reader(data)
                    for row in reader:
                        if len(row)!=0:
                            for j in range(len(row)):
                                if from_location==row[1] and to_location==row[2]:
                                    flag=True
                                    print(f"{'Train Name ':<14}:",row[0])    
                                    print(f"{'Ticket Price ':<14}:",row[-2])    
                                    print(f"{'Seats Available ':<14}:",row[-1])
                                    seat_require=int(input('How many seats booking : '))
                                    if seat_require<=int(row[-1]):
                                        row[-1]=int(row[-1])-seat_require
                                    else:   
                                        print('Invalid seat count')
                                        data.close()
                                        return False
                                    break
                            updated.append(row)
                data.close()
                with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\train_list.csv','w')as data:
                    writer=csv.writer(data)
                    writer.writerows(updated)
                data.close()
                updated=[]
                with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\passenger_list.csv','r')as data:
                    reader=csv.reader(data)
                    for row in reader:
                        if len(row)!=0:
                            for j in range(len(row)):
                                if str(user[0])==row[2] and str(user[1])==row[3]:
                                    row[-1]=int(row[-1])+seat_require
                                    break
                            updated.append(row)
                data.close()
                with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\passenger_list.csv','w')as data:
                    writer=csv.writer(data)
                    writer.writerows(updated)
                data.close()
                return flag
            except (FileNotFoundError,PermissionError):   
                return False
        except ValueError: return False

    def pnr_details():
        try:
            pnr_detail=[]    
            with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\IRTC\\passenger_list.csv','r')as data:                
                reader=csv.reader(data)
                for row in reader:
                    pnr_detail.append(row)
            return pnr_detail
        except(FileNotFoundError,PermissionError):  return False