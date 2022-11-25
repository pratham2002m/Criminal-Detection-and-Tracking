from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login,authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic import CreateView
from django.contrib import messages
from .models import User as mu
from .models import *


# home Page❤️. .............................................................................  #


def index(request):
    return render(request, 'index.html')


# registration of police❤️...............................................................................  #

class PoliceView(CreateView):
    model = User
    form_class = policeReg
    template_name = 'register_police.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'police'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Police Station Data has been updated successfully!')
        login(self.request,user)
        return redirect("home")

# login of police❤️............................................................................... #

def sign_police(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_police == True:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, 'You are not authorized to access this page!')
        else:
            messages.error(request, 'Invalid Credentials!,plz try again')
            return redirect("sign_police")
    return render(request, 'sign_police.html')

# logout  of police❤️............................................................................... #

def letsout(request):
    logout(request)
    return render(request, 'index.html')



# page after signed in of police❤️............................................................................... #

def signpg_police(request):
    police_data = policeModel.objects.all()
    police = {
        "police_info": police_data
    }
    return render(request, 'signpg_police.html', police)

# update of police❤️ .............................................................................................#

def update_police_data(request):
    this_police = policeModel.objects.get(user=request.user)
    police_inf = mu.objects.get(email=request.user.email)
    if request.method == "POST":
        station_name = request.POST.get('station_name')
        station_incharge = request.POST.get('station_incharge')
        station_city = request.POST.get('station_city')
        mobile = request.POST.get('mobile')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        email3 = request.POST.get('email3')
        email4 = request.POST.get('email4')


        this_police.station_name = station_name
        this_police.station_incharge = station_incharge
        this_police.station_city = station_city
        this_police.mobile = mobile 
        this_police.email1 = email1
        this_police.email2 = email2
        this_police.email3 = email3
        this_police.email4 = email4
        this_police.save()

        police_inf.email = email1
        police_inf.save()
        form=policeReg()
        messages.success(request, '...your data has been updated Successfully!')

    police_dat = {
        "police_info": this_police,
        "my_police_inf": police_inf
    }

    return render(request, 'edit_police.html', police_dat)


# addition of criminal detected data❤️ .......................................................................#


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def add_criminal(request):
    if request.method=='POST':
        fm=criminalReg(request.POST,request.FILES)
        print('all not kkk............')
        if fm.is_valid():
           print('all kkk........')
           fm.save()
           print('data saved..........')
           fm=criminalReg()
           stud=criminalModel.objects.all()
           messages.success(request, '...criminal data has been updated Successfully!')
           return redirect('home')
        else:
           print('some error !!!!!!!!!!!!!')
           messages.success(request, '...criminal data not been uploaded !')
           return render(request,'add_criminal.html')   
    else:
        fm=criminalReg()
        stud=criminalModel.objects.all()
        return render(request,'add_criminal.html',{'formx':fm,'stu':stud })



# show profile page of police station❤️.................................................................#

@login_required
def profile_police(request):
    print("inside the profile page function...........!")
    pol_data = policeModel.objects.get(user=request.user)
    print(pol_data)
    sp = {
        "sg" : pol_data
    }
    return render(request, 'profile_police.html', sp)



# show criminal data❤️.......................................................................#

def show_criminal(request):
    crim_data = criminalModel.objects.all()
    sp = {
        "stu": crim_data
    }
    return render(request, 'show_criminal.html', sp)


# update the criminal data❤️.......................................................................#

def updatedata(request,id):
    if request.method=='POST':
        pi=criminalModel.objects.get(pk=id)
        fm=criminalReg(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, '...criminal data re-updated successfully !')
    else:
        pi=criminalModel.objects.get(pk=id)
        fm=criminalReg(instance=pi)
    return render(request,'update_criminal.html',{'formx':fm})



# delete the criminal data❤️.......................................................................#

def deletedata(request,id):
    if request.method=='POST':
        dlt=criminalModel.objects.get(pk=id)
        dlt.delete()
        messages.success(request, '...criminal data deleted successfully !')
        return render(request,'show_criminal.html')


# search the criminal by crim_id❤️.......................................................................#

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        ctr = criminalModel.objects.filter(__icontains=q).order_by("-id")
    return render(request, 'search.html', {'ct': ctr})


# .........................................................................................................#