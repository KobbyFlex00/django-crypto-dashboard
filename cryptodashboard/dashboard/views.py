import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import PortfolioItem
from .forms import PortfolioItemForm
from decimal import Decimal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def fetch_crypto_prices(coin_ids):
    """
    A helper function to fetch prices, taking a list of coin IDs.
    """
    if not coin_ids:
        return {}

    ids_string = ','.join(coin_ids)
    
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ids_string,
        'vs_currencies': 'usd'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def dashboard_view(request):
    """The main view for our dashboard."""
    
    portfolio_items = []
    total_portfolio_value = 0.0
    
    # --- Add/Update Logic ---
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PortfolioItemForm(request.POST)
            if form.is_valid():
                
                coin_id = form.cleaned_data['coin_id'].lower()
                amount_to_add = form.cleaned_data['amount']
                
                try:
                    # Check if this user *already* owns this coin
                    existing_item = PortfolioItem.objects.get(user=request.user, coin_id=coin_id)
                    
                    # If it exists, just add to the amount
                    existing_item.amount += amount_to_add
                    existing_item.save()
                    
                except PortfolioItem.DoesNotExist:
                    # If it doesn't exist, create a new one
                    item = form.save(commit=False)
                    item.user = request.user
                    item.coin_id = coin_id
                    item.save()
                    
                return redirect('home')
    
    # --- GET Logic (Display Dashboard) ---
    
    if request.user.is_authenticated:
        portfolio_items = PortfolioItem.objects.filter(user=request.user)
        coin_ids_to_fetch = [item.coin_id for item in portfolio_items]
        price_data = fetch_crypto_prices(coin_ids_to_fetch)
        
        if price_data:
            for item in portfolio_items:
                coin_id_lower = item.coin_id.lower() 
                if coin_id_lower in price_data:
                    current_price = price_data[coin_id_lower]['usd']
                    current_value = float(item.amount) * current_price
                    item.current_price = current_price
                    item.current_value = current_value
                    total_portfolio_value += current_value

    add_coin_form = PortfolioItemForm()
        
    context = {
        'items': portfolio_items,
        'total_value': total_portfolio_value,
        'add_coin_form': add_coin_form,
    }
    
    return render(request, 'dashboard/home.html', context)

def signup_view(request):
    """View for handling user signup."""
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'dashboard/signup.html', context)

@require_POST
@login_required
def delete_item_view(request, pk):
    """Deletes a portfolio item."""
    
    item = get_object_or_404(PortfolioItem, pk=pk)
    
    if item.user == request.user:
        item.delete()
    
    return redirect('home')