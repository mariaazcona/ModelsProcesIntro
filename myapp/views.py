from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item, Purchase, Review
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ReviewForm


# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'myapp/signup.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})


def list_products(request):
    products = Item.objects.all()
    return render(request, "myapp/products_list.html", {"products": products})


@login_required(login_url='login')
def purchase_history(request):
    purchases = Purchase.objects.filter(user=request.user)
    return render(request, "myapp/purchase_history.html", {"purchases": purchases})


@login_required(login_url='login')
def buy_item(request, item_id):
    item = Item.objects.get(id=item_id)
    Purchase.objects.create(user=request.user, item=item)
    return redirect("purchase_history")


@login_required(login_url='login')
def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id, user=request.user)
    purchase.delete()
    return redirect('purchase_history')


@login_required(login_url='login')
def add_review(request, product_id):
    product = get_object_or_404(Item, id=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect("list_products")
    else:
        form = ReviewForm()

    return render(request, "myapp/add_review.html", {"form": form, "item": product})
