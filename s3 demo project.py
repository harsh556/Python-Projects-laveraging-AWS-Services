print('welcome to bank of india ATM')
restart=('y')
chances=5
import boto3
import pandas as pd
s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='AKIATNWCXI5YKH4OHSIE',
    aws_secret_access_key='pneMYCH3HZQ4IbRuFhLipyH0jS02JKwynsJQG2sa'
)
# for avoiding regular use of access keys and secret keys and setting it with respect to your environment 
import os
os.environ["AWS_DEFAULT_REGION"] = 'ap-south-1'
os.environ["AWS_ACCESS_KEY_ID"] = 'AKIATNWCXI5YKH4OHSIE'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'pneMYCH3HZQ4IbRuFhLipyH0jS02JKwynsJQG2sa'
# for avoiding regular use of access keys and secret keys and setting it with respect to your environment 
import os
os.environ["AWS_DEFAULT_REGION"] = 'ap-south-1'
os.environ["AWS_ACCESS_KEY_ID"] = 'AKIATNWCXI5YKH4OHSIE'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'pneMYCH3HZQ4IbRuFhLipyH0jS02JKwynsJQG2sa'
import pandas as pd
# user details 
import pandas as pd
user_details={'users': {'harsh':{'amount':'5000','pin':'2233'},'satyam':{'amount':'6000','pin':'5566'},'zaid':{'amount':'5000','pin':'3344'},'prakhar':{'amount':'4000','pin':'8877'},'suraj':{'amount':'10000','pin':'6666'}}}
df = pd.DataFrame(user_details['users'])


# save to csv
df.to_csv('df.csv')
#upload files to s3 bucket
s3.Bucket('harshbucket-1').upload_file(Filename='df.csv', Key='df.csv')
#load csv file directly into python
obj = s3.Bucket('harshbucket-1').Object('df.csv').get()
df = pd.read_csv(obj['Body'],index_col=0)
while chances:
      user = input('Please Enter your name:')
      if user.lower() in df.columns:
            pin = int(input('Enter your PIN:'))
            if df.loc['pin',user] == pin:
                  print('Sign in successful')
                  option = ''
                  while option.lower() not in ['no','N']:
                        print('1. To check your balance')
                        print('2. To check make a withdrawl')
                        print('3. To pay in.')
                        print('4. To return your card')
                        option = input('Choose an option:')
                        if option=='1':
                              print('Your account balance is %.4f'%df.loc['amount',user])
                              print('Would you like to restart?')
                              option = input('Choose Y[es] or N[o]:')
                              continue
                        elif option == '2':
                              amount = float(input('Enter the amount you want to withdraw:'))
                              if amount > df.loc['amount',user]:
                                    print('Invalid amount entered. Aborting the transaction.')
                                    continue
                              else:
                                    print('You want to withdraw $%.4f ?')
                                    yORn = input('Choose Y[es] or N[o]:')
                                    if yORn == 'Y':
                                          df.loc['amount',user] = str(float(df.loc['amount',user])-amount)
                                          print('Transaction Successful')
                                          df.loc('Thank you!')
                                          print('Would you like to restart?')
                                          option = input('Choose Y[es] or N[o]:')
                                          continue
                                    elif yORn:
                                          print('Thank you! Aborting the transaction as per your request')
                                          print('Would you like to restart?')
                                          option = input('Choose Y[es] or N[o]:')
                                          continue
                        elif option == '3':
                              pay_in = float(input('How much would you like to payin?'))
                              df.loc['amount',user] = str( float(df.loc['amount',user]) + pay_in )
                              print('Amount successfully payed in. \nThank you')
                              print('Would you like to restart?')
                              option = input('Choose Y[es] or N[o]:')
                              continue

                        elif option == '4':
                              print('please wait while your card is returned...\n')
                              print('thankyou for your service')
                              print('Would you like to restart?')
                              option = input('Choose Y[es] or N[o]:')
                              continue
                        else:
                              print('Enter a correct a option.')
                              continue
            else:
                  print('Incorrect Username.')
                  chances-=1
            if chances==0:
                  print('Your have exhausted all you chances please retry after sometime')
      else:
            print("Invalid Username")
            chances-=1
            if chances ==0:
                  print('Your have exhausted all you chances please retry after sometime')
