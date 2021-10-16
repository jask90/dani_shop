from django.shortcuts import render


def register_bot(request):
    return render(request, "register_bot/register_bot.html")
