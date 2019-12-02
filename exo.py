
####################################
#EXO1
# class Family:
#     def __init__(self,last_name):
#         self.last_name=last_name
#         self.allFamily=[]
#         self.children=[]
#         self.members = {'name': '', 'age': 0, 'sex': '', 'is_child': ''}
#
#     def add(self,name,age,sex,is_child):
#         newperson={'name':name,'age':age,'sex':sex, 'is_child':is_child}
#         self.allFamily.append(newperson)
#         if is_child:
#             self.children.append(newperson)
#
#     def born(self,name,sex):
#         newborn={'name':name,'age':0,'sex':sex,'is_child':True}
#         self.allFamily.append(newborn)
#         self.children.append(newborn)
#         print(f'Mazel Tov for {newborn["name"]}')
#
#     def is_18(self,child_name):
#         for child in self.children:
#             if child["name"]==child_name and child["age"]>=18:
#                 return True
#         else:
#             return False
#
#     def info(self):
#         for k in self.allFamily:
#             print(k)

#####################################
#EXO2
# class TheIncredibles(Family):
#
#
#     def updatekeys(self,incredible_name,power):
#         newincredible = {'incrediblename': incredible_name, 'age': age,'power'power, 'sex': sex, 'is_child': is_child}
#         self.members.update(newincredible)
#
#     pass

# Benhamou = Family('Benhamou')
# Benhamou.add('Papa',68,'Male',False)
# Benhamou.add('Maman',68,'Female',False)
# Benhamou.add('Ezra',35,'Male',True)
# Benhamou.add('Tamar',34,'Female',True)
# Benhamou.add('Yona',26,'Female',True)
# Benhamou.add('Hilel',25,'Male',True)
# Benhamou.add('Naomie',22,'Female',True)
# Benhamou.add('Matitiaou',15,'Male',True)
# Benhamou.info()
# Benhamou.born('Yohanan','Male')
# print(Benhamou.is_18('Yohanan'))
#
# Incredibles=TheIncredibles('Incredibles')
# Incredibles.add('Elastigirl',68,'Female',False)
# Incredibles.add('Mr.Incredible',69,'Male',False)
# Incredibles.add('Violet',15,'Female',True)
# Incredibles.add('Flash',11,'Male',True)
# Incredibles.info()
# Incredibles.born('Jack Jack','Male')
# Incredibles.info()

#######################################################
#######################################################
#EXO3
# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#
#     def deposit(self, amount):
#         if amount%20==0 or amount%100==0:
#             self.balance=self.balance+amount
#             return self.balance
#
#         elif amount%20 !=0 or amount%100 !=0:
#             print('We have only bills of 20$ and 100$')
#
#         else:
#             print('You cannot deposit a negative amount')
#
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             if amount%20==0 or amount%50==0:
#                 self.balance = self.balance - amount
#                 return self.balance
#             elif amount%20 !=0 or amount%50 !=0:
#                 print('We have only bills of 20$ and 50$')
#
#         else:
#             print("You don't have enought money on your bank account")

# class Owner(BankAccount):
#     def __init__(self,owner,balance,cardNumber,password):
#         super().__init__(owner, balance)
#         self.cardNumber=cardNumber
#         self.password=password
#
#     def check_owner_info(self):
#         for tries in range(2):
#             check_card = int(input('Put your Card Number '))
#             check_password = int(input('Put your password '))
#
#             if check_card==self.cardNumber and check_password==self.password:
#                 print('Code Valid')
#
#                 break
#
#             elif check_card!=self.cardNumber or check_password!=self.password:
#                 print('Code incorrect')
#                 print('Retry')
#
#         if check_card==self.cardNumber and check_password==self.password:
#             ask=input('Do you want to deposit or withdraw ?')
#
#             if ask=='deposit':
#                 amount=int(input('How much you want to depose ?'))
#                 super().deposit(amount)
#                 self.deposit_more()
#
#
#             elif ask=='withdraw':
#                 amount=int(input('How much you want to withdraw ?'))
#                 super().withdraw(amount)
#                 self.withdraw_more()
#
#             else:
#                 print('Error !!')
#
#         elif check_card != self.cardNumber or check_password != self.password:
#             print('Your Card has been eaten')
#             del(self.cardNumber)
#
#     def deposit_more(self):
#         ask = input('Do you want to deposit more ?')
#         if ask == 'yes':
#             amount = int(input('How much you want to depose ?'))
#             left = super().deposit(amount)
#             print(f'You have {left}$ left')
#             print('Have a nice Day')
#
#         elif ask == 'no':
#             left = self.balance
#             print(f'You have {left}$ left ')
#             print('Have a nice Day')
#
#     def withdraw_more(self):
#         ask = input('Do you want to withdraw more ?')
#         if ask == 'yes':
#             amount = int(input('How much you want to withdraw ?'))
#             left = super().withdraw(amount)
#             print(f'You have {left}$ left ')
#             print('Have a nice Day')
#
#         elif ask == 'no':
#             left=self.balance
#             print(f'You have {left}$ left ')
#             print('Have a nice Day')


# if __name__=="__main__":
#     hilelcard=Owner('Hilel',1000,1234,2704)
#     hilelcard.check_owner_info()

################################################################