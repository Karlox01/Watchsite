from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Category, Item


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'watches/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'watches/detail.html', {
        'item': item,
        'related_items': related_items
    })

def submit_offer(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        offer_amount = request.POST.get('offer_amount')

        admin_group = Group.objects.get(name='Admins')
        admin_users = admin_group.user_set.all()
        for admin_user in admin_users:
            message = f"New offer for '{item.name}' received: £{offer_amount}."
            messages.add_message(request, messages.INFO, message)

        return render(request, 'watches/thanks.html')

    return render(request, 'watches/submit_offer.html', {'item': item})
