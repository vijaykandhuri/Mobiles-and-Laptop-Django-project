from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from sep02app.models import Useradd,Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"base.html")

def products(request):
    return render(request,"products.html")



#1
#HONOR
response=requests.get("https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&otracker=categorytree&otracker=nmenu_sub_Women_0_Topwear&otracker=nmenu_sub_Women_0_Topwear&p%5B%5D=facets.brand%255B%255D%3DADIDAS")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('span',class_='B_NuCI')
prices=soup.find_all('div',class_='_30jeq3 _16Jk6d')
ratings=soup.find_all('div',class_='_3LWZlK _3uSWvT')
images=soup.find_all('img',class_='_2r_T1I _396QI4')
links=soup.find_all('a',class_='_2UzuFa')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist1=zip(name,
price,
rate,
image,
link
)



def honor(request):
    return render(request,"honor.html",{'mylist1':mylist1})

#2
#REDMI
response=requests.get("https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&otracker=categorytree&otracker=nmenu_sub_Women_0_Topwear&otracker=nmenu_sub_Women_0_Topwear&p%5B%5D=facets.brand%255B%255D%3DADIDAS")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='B_NuCI')
prices=soup.find_all('div',class_='_30jeq3 _16Jk6d')
ratings=soup.find_all('div',class_='_3LWZlK _3uSWvT')
images=soup.find_all('img',class_='_2r_T1I _396QI4')
links=soup.find_all('a',class_='_2UzuFa')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist2=zip(name,
price,
rate,
image,
link
)

def redmi(request):
    return render(request,"redmi.html",{'mylist2':mylist2})

# mobiles_rating=pandas.DataFrame()
# mobiles_rating['Ratings']=Rating
# print(mobiles_rating)
# mobiles_rating.to_csv('moblies_rating.csv')


#3
#OPPO
response=requests.get("https://www.flipkart.com/search?q=realme%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist3=zip(name,
price,
rate,
image,
link
)

def oppo(request):
    return render(request,"oppo.html",{"mylist3":mylist3})


#4
#SAMSUNG
response=requests.get("https://www.flipkart.com/search?q=samsung%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist4=zip(name,
price,
rate,
image,
link
)


def samsung(request):
    return render(request,"samsung.html",{'mylist4':mylist4})

#5
# VIVO
response=requests.get("https://www.flipkart.com/search?q=vivo%20mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist5=zip(name,
price,
rate,
image,
link
)

def vivo(request):
    return render(request,"vivo.html",{'mylist5':mylist5})

#6
#HP Laptops

response=requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DHP")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/search?q=HP%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off/"#+i['href']
    link.append(d)

mylist6=zip(name,
rate,
price,
image,
link
)

def hp(request):
    return render(request,"hp.html",{'mylist6':mylist6})


#7
#MSI LAPTOP

response=requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DMSI")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/search?q=msi%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off/"#+i['href']
    link.append(d)

mylist7=zip(name,
rate,
price,
image,
link
)

def msi(request):
    return render(request,"msi.html",{'mylist7':mylist7})

#8
#DELL LAPTOP

response=requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DDELL")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/search?q=dell%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off/"#+i['href']
    link.append(d)

mylist8=zip(name,
rate,
price,
image,
link
)

def dell(request):
    return render(request,"dell.html",{'mylist8':mylist8})

#9
#ASUS LAPTOP

response=requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DASUS")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/search?q=asus%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off/"#+i['href']
    link.append(d)

mylist9=zip(name,
rate,
price,
image,
link
)

def asus(request):
    return render(request,"asus.html",{'mylist9':mylist9})

#10
#LENOVO LAPTOP

response=requests.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DLenovo")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/search?q=lenovo%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off/"#+i['href']
    link.append(d)

mylist10=zip(name,
rate,
price,
image,
link
)

def lenovo(request):
    return render(request,"lenovo.html",{'mylist10':mylist10})

#11
#INFINIX

response=requests.get("https://www.flipkart.com/search?q=+laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DInfinix")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/search?q=lenovo%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off/" #+i['href']
    link.append(d)

mylist11=zip(name,
rate,
price,
image,
link
)

def infinix(request):
    return render(request,"infinix.html",{'mylist11':mylist11})


#12
#ACER LAPTOP

response=requests.get("https://www.flipkart.com/search?q=+laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DAcer")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/search?q=acer%20laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off/" #+i['href']
    link.append(d)

mylist12=zip(name,
rate,
price,
image,
link
)

def acer(request):
    return render(request,"acer.html",{'mylist12':mylist12})


def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")# read 
        password=request.POST.get("password")# read
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
        return redirect("home")
    return render(request,"login.html")




def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        c = User.objects.create_user(username=username,email=email,password=password)
        c.save()
        return redirect("login")
    
    return render(request,"register.html")



def logout_user(request):
    logout(request)
    return redirect("login")




def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        


        c=Contact(name=name,email=email,message=message)
        c.save()
        return redirect("home")

    return render(request,"contact.html")

       














"""def demo(request):
    #return(HttpResponse("This is my Django Project"))
def demo(request):
    c=" "
    if request.method=="POST":
        n1=eval(request.POST.get("A"))
        n2=eval(request.POST.get("B"))
        opr=request.POST.get("opr")
        if opr=="+":
            c=n1+n2
        elif opr=="-":
            c=n1-n2
        elif opr=="*":
            c=n1*n2
        elif opr=="/":
            c=n1/n2
        elif opr=="**":
            c=n1**n2
    return render(request,"calculator.html",{'c':c})"""