from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SupportTicket
from .forms import SupportTicketForm

@login_required
def create_support_ticket(request, service_request_id):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            support_ticket = form.save(commit=False)
            support_ticket.service_request_id = service_request_id
            support_ticket.save()
            return redirect('request_tracking')
    else:
        form = SupportTicketForm()
    return render(request, 'support/create_support_ticket.html', {'form': form})

@login_required
def manage_tickets(request):
    assigned_tickets = SupportTicket.objects.filter(assigned_to=request.user)
    return render(request, 'support/manage_tickets.html', {'assigned_tickets': assigned_tickets})
