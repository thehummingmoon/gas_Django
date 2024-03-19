from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/submit_service_request.html', {'form': form})

@login_required
def track_requests(request):
    customer = request.user.customer
    requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'customers/track_requests.html', {'requests': requests})
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, ServiceRequest
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm  # Assuming you create a form for service requests
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import datetime
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HomeView(View):
    def get(self, request):
        return render(request, 'customers/home.html')

# class SubmitRequestView(View):
#     @login_required
#     def get(self, request):
#         form = ServiceRequestForm()
#         return render(request, 'customers/submit_request.html', {'form': form})
#     @login_required
#     def post(self, request):
#         form = ServiceRequestForm(request.POST)
#         if form.is_valid():
#             customer = Customer.objects.get(user=request.user)  # Assuming user is authenticated
#             service_request = form.save(commit=False)
#             service_request.customer = customer
#             service_request.save()
#             return redirect('customers:track_requests')
#         return render(request, 'customers/submit_request.html', {'form': form})


# class SubmitRequestView(View):
#     @method_decorator(login_required)
#     def get(self, request):
#         form = ServiceRequestForm()
#         return render(request, 'customers/submit_request.html', {'form': form})

#     @method_decorator(login_required)
#     def post(self, request):
#         form = ServiceRequestForm(request.POST, request.FILES)  # Include request.FILES for file uploads
#         if form.is_valid():
#             service_request = form.save(commit=False)
#             service_request.customer = request.user.customer  # Use request.user to get the logged-in user
#             service_request.save()
#             return redirect('customers:track_requests')
#         return render(request, 'customers/submit_request.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class SubmitRequestView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = ServiceRequestForm()
        return render(request, 'customers/submit_request.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = ServiceRequestForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            try:
                customer = Customer.objects.get(user=request.user)
            except Customer.DoesNotExist:
                # Create a customer profile if it doesn't exist
                customer = Customer.objects.create(
                    user=request.user,
                    name=request.user.username,  # Example: You might use a different field for the customer's name
                    email=request.user.email,    # Example: You might use a different field for the customer's email
                    account_number='123456',     # Example: Set an appropriate account number
                )

            service_request = form.save(commit=False)
            service_request.customer = customer
            service_request.request_date = datetime.datetime.now()
            service_request.status = "Pending"
            service_request.save()
            return redirect('customers:track_requests')
        return render(request, 'customers/submit_request.html', {'form': form})


# @method_decorator(login_required, name='dispatch')
# class TrackRequestsView(View):
#     def get(self, request):
#         customer = Customer.objects.get(user=request.user)  # Assuming user is authenticated
#         service_requests = ServiceRequest.objects.filter(customer=customer)
#         return render(request, 'customers/track_requests.html', {'service_requests': service_requests})



class TrackRequestsView(View):
    @method_decorator(login_required)
    def get(self, request):
        customer = request.user.customer  # Access the customer associated with the logged-in user
        service_requests = ServiceRequest.objects.filter(customer=customer)
        return render(request, 'customers/track_requests.html', {'service_requests': service_requests})

class AccountInfoView(View):
    def get(self, request):
        customer = Customer.objects.get(user=request.user)  # Assuming user is authenticated
        return render(request, 'customers/account_info.html', {'customer': customer})