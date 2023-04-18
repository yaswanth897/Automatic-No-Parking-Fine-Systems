import pyrebase

S_mail="yasurv05@gmail.com"
S_password="Avengers@9440"
firebaseConfig = {"apiKey": "AIzaSyAho6zWZZOuAuzxh2t_SHT2Ip6MrtZx6Rk",
                  "authDomain": "automatic-no-parking-fine-sys.firebaseapp.com",
                  "databaseURL": "https://automatic-no-parking-fine-sys-default-rtdb.firebaseio.com",
                  "projectId": "automatic-no-parking-fine-sys",
                  "storageBucket": "automatic-no-parking-fine-sys.appspot.com",
                  "messagingSenderId": "206227731173",
                  "appId": "1:206227731173:web:5ee8496a158ab0b369da0c",
                  "measurementId": "G-1VSFMCX8GQ"
                 }

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

number=input("Enter Vehicle Number:")
mail=input("Enter E-Mail id:")
vtype=input("Enter Vehicle Type:")
name=input("Enter Owner Name:")
data={"Vehicle Owner":name, "email":mail, "type":vtype, "Fine":0, "Vehicle Number": number}
db.child("data").child(number).set(data)
print("Sucess")
