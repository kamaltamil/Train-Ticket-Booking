from passenger import Passenger as PNR
from train import TRAIN

class IRTC:
    def __init__(self):
        pass
    # Home page for IRTC
    def home(visit):
        while visit:
            print('1.Admin \n2.Passenger \n3.Exit')
            match PNR.option():
                case 1: visit=run.admin(admin=True)
                case 2: PNR.passenger()
                case 3: 
                    print('Thank Your for visit')
                    visit=False
                case _: 
                    print('Invalid')
    # Admin page
    def admin(admin):
        while admin:
            print('1.Login \n2.Back')
            match PNR.option():
                case 1: admin=run.admin_login(True)
                case 2: 
                    print('Back')
                    return True
                case _: print('Invalid')
    # Admin login page
    def admin_login(self):
        try:
            admin_id=input('Enter Admin Id : ')
            admin_pwd=int(input('Password : '))
            if admin_id=='kamaltamil' and admin_pwd==int(1101):
                admin=True
                while admin:
                    print('1.Add Train \n2.Check Passenger \n3.Back')
                    match PNR.option():
                        case 1: 
                            add=TRAIN.add_train(self)
                            if add:   
                                admin=True
                            else:
                                print('Operation Failed!')
                                admin=False
                        case 2: 
                            passenger_det=PNR.pnr_details()
                            for row in passenger_det:
                                if len(row)>=4:
                                    print(f"{row[0]:<8}|{row[1]:<8}|{row[2]:<13}|{row[4]:<8}")
                        case 3: admin=False
                        case _: print('Invalid ')
            elif admin_id!='kamaltamil':
                print('Invalid Username')        
            else:
                print('Enter correct password')        
            return True
        except ValueError: print('Enter Valid Input')

run=IRTC
run.home(True)