from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Member, Transaction
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm, MembersForm
from .helper import get_event_context
from django.contrib.auth.models import User

@transaction.atomic
@login_required
def events(request):
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        event_description = request.POST.get('event_description')
        pledged_amount = request.POST.get('contribution')

        event = Event.objects.create(
            name=event_name,
            description=event_description
        )

        Member.objects.create(
            user=request.user,
            event=event,
            amount_pledged=pledged_amount,
            balance_amount=pledged_amount
        )
        return redirect('/events/')
    else:
        events = Event.objects.filter(members__user=request.user)
        context = {
            'events': events
        }
        return render(request, 'events.html', context)

@transaction.atomic
@login_required
def event_details(request, event_id):
    user = request.user
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'expense_form':
            expense_form = ExpenseForm(request.POST, balance_amount = Member.objects.get(user = user).balance_amount)
            if expense_form.is_valid():
                heading  = expense_form.cleaned_data.get('heading')
                expense = expense_form.cleaned_data.get('amount')
                Transaction.objects.create(
                    heading = heading,
                    expense = expense,
                    user = user,
                    event = Event.objects.get(id=event_id)
                )
                member = Member.objects.get(user = user)
                member.balance_amount -= expense
                member.save()
                return redirect(request.path_info)
            else:
                context = get_event_context(event_id, expense_form)
                print(expense_form.errors.get('amount', []))
                return render(request, 'event_details.html', context)
        else:
            members_form = MembersForm(request.POST, event_id)
            if members_form.is_valid():
                Member.objects.create(
                    user = User.objects.get(email=members_form.cleaned_data.get('email_id')),
                    event = Event.objects.get(id=event_id),
                    amount_pledged = members_form.cleaned_data.get('contribution'),
                    balance_amount = members_form.cleaned_data.get('contribution')
                )
                return redirect(request.path_info)
            else:
                print(members_form.errors.get('email_id', []))
                context = get_event_context(event_id, members_form=members_form)
                return render(request, 'event_details.html', context)

    else:
        context = get_event_context(event_id)
        return render(request, 'event_details.html', context)

@transaction.atomic
@login_required
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    member = Member.objects.get(user=transaction.user)
    event_id = transaction.event.id
    if request.method == 'POST':
        transaction.delete()
    member.balance_amount += transaction.expense
    member.save()
    return redirect('event_details', event_id=event_id)

@transaction.atomic
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('events')
 




