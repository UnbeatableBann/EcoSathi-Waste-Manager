from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader,RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from Homepage.models import regsitration,CustomUser,complain,PickupBooking,Dustbin        #maunally added models
from django.db import IntegrityError
from django.contrib.auth import authenticate, login  as auth_login
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


#homepage.

def login(request): #Login for all characters.
    return render(request,'login_html.html')


def create_account(request):
    #print("shadab")
    if request.method == 'POST':
        account_type = request.POST['account-type']
        full_name = request.POST['fullname']
        username = request.POST['new-username']
        password = request.POST['new-password']
        phone = request.POST['phone_number']
        email = request.POST['email']
        business_type = request.POST['business-type-select']
        other_business_text = request.POST['other-business-text']
        hashed_password = make_password(password)
        try:
            user = CustomUser.objects.create(
                account_type=account_type,
                full_name=full_name,
                username=username,
                password=hashed_password,
                phone=phone,
                business_type=business_type,
                email=email,
                other_business_text=other_business_text
            )
           # print("aef")
            messages.success(request, 'Account created successfully!')
            return render(request, 'login_html.html')  # Redirect to login page
        except Exception as e:
            print(f"Exception: {e}")
            #messages.error(request, str(e))
        #except IntegrityError as e:
            # Handle duplicate username error
            message="Username is already taken. Please choose a different one."
            return render(request, 'create_account.html',{'message': message})

    else:
        return render(request, 'create_account.html')


def signup(request): #Login for all characters.
        return render(request,'create_account.html')

def home(request): #Home for a homepage.
    return render(request,'home_page.html')


def login_view(request):
    #print("qwerty")
    if request.method == 'POST':
            #print(request.POST)
            username = request.POST['username']
            password = request.POST['password']                 #no forgot password
            login_type = request.POST['login_type']
            #print(f"Username: {username}, Password: {password}, Login Type: {login_type}")
            user = authenticate(request,username=username, password=password,login_type=login_type)
            print(f"Authenticated User: {user}")

            if user is not None :
                auth_login(request, user)
                pickup_bookings = PickupBooking.objects.all()
                complaints = complain.objects.all()
                user_instance = CustomUser.objects.get(username=username)
                phone = user_instance.phone
                email = user_instance.email
                context = {
                    'username': username,
                    'complaints': complaints,
                    'pickup_bookings': pickup_bookings,
                    'phone':phone,
                    'email':email
                }
                messages.success(request, 'Login successful!')

                if login_type == 'user' :
                    #print('asdfgh')
                    #return redirect('enduser')                     # Replace 'user_home' with the user's home URL
                    return render(request,'enduser.html', context)              # issue with sending username to other app
                elif login_type == 'admin':
                    return render(request,'Admin page.html', context)
                elif login_type == 'business':
                    #return redirect('business_home')                # Replace 'business_home' with the business's home URL
                    messages.success(request, 'Login successful!')
                    return render(request,'business.html', context)
                else:
                    messages.error(request, 'Invalid account type.')
                    #print("popppp")
                    return render(request, 'login_html.html')           # add other url

            else:
                messages.error(request, 'Invalid username or password.')
                #return render(request,time_pass.html)
                return render(request, 'login_html.html', {'error_message': 'Invalid login credentials'})
    else:

        return render(request, 'time_pass.html')           # add other url



def custom_404(request, exception):
    return render(request,'error_page.html')


def learn_more(request):
    return render(request,'learn_more.html')

def complain_view(request):
    print("adasd")
    if request.user.is_authenticated:
        account_type = request.user.account_type
    else:
        # Set a default value or handle the case where the user is not authenticated
        account_type = "Guest"
    if request.method == 'POST':
        print("00000")
        try:
            print(request.POST)  # Add this line to inspect the POST data
            name = request.POST['name']
            address = request.POST['address']
            phone_number = request.POST['phone_number']        #error will come because in enduser template there is no phone number
            description = request.POST['description']
            image = request.FILES.get('image',None)

        except MultiValueDictKeyError as e:
            print(f"Error accessing form data: {e}")
            return render(request, 'error_page.html')

        # Process the form data, perform any necessary actions, and save to the database
        # Additional logic here
        complaint = complain(full_name=name, address=address, phone_number=phone_number, description=description, image=image, account_type=account_type)
        complaint.save()
        messages.success(request, 'Login successful!')
        return render(request,'enduser.html')         # Redirect to the home page after successful form submission

    else:
        return redirect('enduser.html')


def pickup_booking_view(request):
    print("pickup")
    if request.method == 'POST':
        # Handle form submission
        company_name = request.POST.get('companyName')
        user_name = request.POST.get('userName')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        pickup_date = request.POST.get('pickupDate')
        pickup_time = request.POST.get('pickupTime')

        # Create a PickupBooking object and save it to the database
        PickupBooking.objects.create(
            companyName=company_name,
            userName=user_name,
            address=address,
            phone_number=phone_number,
            pickupDate=pickup_date,
            pickupTime=pickup_time,
        )
        messages.success(request, 'Your success message goes here.')
        return render(request, 'business.html')                 # Redirect to a success page

    else:
        return render(request, 'pickup_booking_form.html')



def forgotpassword(request):                                                      #this is incomplete
    if request.method == 'GET':
        # Render the forgot password page template for GET requests
        return render(request, 'forgotpassword.html')
    elif request.method == 'POST':
        # Process the form submission for password reset for POST requests
        email = request.POST.get('email')
        username = request.POST.get('username')

        # Check if the email exists in the database
        if CustomUser.objects.filter(username=username).exists():
            # Generate a unique token for the password reset link (you might use a library for this)
            # Here, I'm using a simple example of concatenating email and username
            reset_token = f"{email}-{CustomUser.objects.get(username=username).username}"

            # Send an email with a link to reset the password
            reset_link = f"{settings.BASE_DIR}/resetpassword?token={reset_token}"
            send_mail(
                'Password Reset',
                f'Click the link to reset your password: {reset_link}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            # You may want to redirect the user to a success page
            return render(request, 'login_html.html')
        else:
            # Email does not exist in the database
            return render(request, 'error_page.html', {'error_message': 'Email does not exist'})
    else:
        # Handle other HTTP methods if needed
        return HttpResponse("Method not allowed", status=405)

'''
def pickup_booking_table(request):
    pickup_bookings = PickupBooking.objects.all()
    return render(request, 'pickup_booking table.html', {'pickup_bookings': pickup_bookings})


def complain_table(request):
    complaints = complain.objects.all()
    return render(request, 'complain_table.html', {'complaints': complaints})
'''



#this added today
def map_view(request):
    dustbins = Dustbin.objects.all()
    return render(request, 'map.html', {'dustbins': dustbins})


def get_nearby_dustbins(request):
    print("jfhbhf")
    user_latitude = float(request.GET.get('lat', 0))
    user_longitude = float(request.GET.get('lon', 0))

    # Assuming you have a method to calculate nearby dustbins based on user's location
    nearby_dustbins = calculate_nearby_dustbins(user_latitude, user_longitude)

    dustbin_data = [{'name': dustbin.name, 'latitude': dustbin.latitude, 'longitude': dustbin.longitude}
                    for dustbin in nearby_dustbins]

    return JsonResponse({'dustbins': dustbin_data})


def calculate_nearby_dustbins(user_latitude, user_longitude, max_distance_km=50):
    # Convert the max_distance_km to degrees
    max_distance_degrees = max_distance_km / 11.32  # Approximately 111.32 km per degree

    # Calculate the bounding box of the search area
    min_latitude = user_latitude - max_distance_degrees
    max_latitude = user_latitude + max_distance_degrees
    min_longitude = user_longitude - max_distance_degrees
    max_longitude = user_longitude + max_distance_degrees

    # Query the dustbins within the bounding box
    nearby_dustbins = Dustbin.objects.filter(
        latitude__gte=min_latitude,
        latitude__lte=max_latitude,
        longitude__gte=min_longitude,
        longitude__lte=max_longitude
    )

    # Filter out dustbins that are beyond the specified distance
    filtered_dustbins = []
    for dustbin in nearby_dustbins:
        distance_km = haversine(user_latitude, user_longitude, dustbin.latitude, dustbin.longitude)
        print(max_distance_km)
        if distance_km <= max_distance_km:
            #print(f'Dustbin Coordinates: {dustbin.latitude}, {dustbin.longitude}\n')
            print(filtered_dustbins)
            filtered_dustbins.append(dustbin)

    return filtered_dustbins


def haversine(lat1, lon1, lat2, lon2):
    # Calculate the great-circle distance between two points using the Haversine formula
    import math

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Earth radius in kilometers (use 6371 for kilometers, 3958.8 for miles)
    radius = 6371

    # Calculate the distance
    distance = radius * c

    return distance



def cancel_complaint_view(request, complaint_id):
    complaint = get_object_or_404(Complain, pk=complaint_id)
    complaint.delete()
    return JsonResponse({'success': True})