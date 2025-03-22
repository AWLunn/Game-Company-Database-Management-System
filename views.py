from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            account_balance = form.cleaned_data['account_balance']
            purchase_history = form.cleaned_data['purchase_history']
            subscription_status = form.cleaned_data['subscription_status']

            # Check if the player already exists
            existing_player = Player.objects.filter(username=username).first()

            if existing_player:
                # Player found, update its details
                existing_player.password = password
                existing_player.email = email
                existing_player.account_balance = account_balance
                existing_player.purchase_history = purchase_history
                existing_player.subscription_status = subscription_status
                existing_player.save()
                return HttpResponse("Player updated successfully")
            else:
                # Player not found, create a new player
                new_player = Player(
                    username=username,
                    password=password,
                    email=email,
                    account_balance=account_balance,
                    purchase_history=purchase_history,
                    subscription_status=subscription_status
                )
                new_player.save()
                return HttpResponse("Player created successfully")
    else:
        form = PlayerForm()
    return render(request, 'home.html', {'form': form})

def gameModify(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            GameID = form.cleaned_data['GameID']
            Title = form.cleaned_data['Title']
            Genre = form.cleaned_data['Genre']
            Price = form.cleaned_data['Price']
            Platform = form.cleaned_data['Platform']

            # Check if the game already exists
            existing_game = Game.objects.filter(GameID=GameID).first()

            if existing_game is not None:
                # Game found, update its details
                existing_game.Title = Title
                existing_game.Genre = Genre
                existing_game.Price = Price
                existing_game.Platform = Platform
                existing_game.save()
                return redirect('home')
            else:
                # Game not found, create a new game
                newGame = Game(
                    GameID=GameID,
                    Title=Title,
                    Genre=Genre,
                    Price=Price,
                    Platform=Platform,
                )
                newGame.save()
                return redirect('home')
    else:
        form = GameForm()
    return render(request, 'GameModify.html', {'form': form})
