from django.shortcuts import render


def assistance_bot(request):
    return render(request, "assistance_bot/assistance_bot.html")
