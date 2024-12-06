from .models import Event, Transaction
from django.db.models import Sum
from .forms import ExpenseForm, MembersForm

def get_event_context(event_id, expense_form=None, members_form=None):
    event = Event.objects.get(id = event_id)
    members = event.members.all()
    transactions = Transaction.objects.filter(member__event=event)
    total_budget = members.aggregate(Sum('amount_pledged'))['amount_pledged__sum']
    total_balance = members.aggregate(Sum('balance_amount'))['balance_amount__sum']
    context = {
        'event' : event,
        'transactions' : transactions,
        'members' : members,
        'total_budget' : total_budget,
        'total_balance' : total_balance,
        'expense_form' : expense_form if expense_form else ExpenseForm(),
        'members_form' : members_form if members_form else MembersForm()
    }
    return context