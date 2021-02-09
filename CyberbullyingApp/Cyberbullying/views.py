from django.shortcuts import render, redirect, HttpResponse
from .forms import Cyberbullying_Typed_Tweet_analyse_form
from .Cyberbullying_analysis_code import Cyberbullying_analysis_code
from .forms import Cyberbullying_Imported_Tweet_analyse_form
from .tweepy_Cyberbullying import Import_tweet_Cyberbullying

def Cyberbullying_analysis(request):
    return render(request, 'home/Cyberbullying.html')

def Cyberbullying_analysis_type(request):
    if request.method == 'POST':
        form = Cyberbullying_Typed_Tweet_analyse_form(request.POST)
        analyse = Cyberbullying_analysis_code()
        if form.is_valid():
            tweet = form.cleaned_data['Cyberbullying_typed_tweet']
            Cyberbullying = analyse.predict_Cyberbullying(tweet)
            args = {'tweet':tweet, 'Cyberbullying':Cyberbullying}
            return render(request, 'home/Cyberbullying_type_result.html', args)

    else:
        form = Cyberbullying_Typed_Tweet_analyse_form()
        return render(request, 'home/Cyberbullying_type.html')

def Cyberbullying_analysis_import(request):
    if request.method == 'POST':
        form = Cyberbullying_Imported_Tweet_analyse_form(request.POST)
        tweet_text = Import_tweet_Cyberbullying()
        analyse = Cyberbullying_analysis_code()

        if form.is_valid():
            handle = form.cleaned_data['Cyberbullying_imported_tweet']

            if handle[0]=='#':
                list_of_tweets = tweet_text.get_hashtag(handle)
                list_of_tweets_and_Cyberbullyings = []
                for i in list_of_tweets:
                    list_of_tweets_and_Cyberbullyings.append((i,analyse.predict_Cyberbullying(i)))
                args = {'list_of_tweets_and_Cyberbullyings':list_of_tweets_and_Cyberbullyings, 'handle':handle}
                return render(request, 'home/Cyberbullying_import_result_hashtag.html', args)

            list_of_tweets = tweet_text.get_tweets(handle)
            list_of_tweets_and_Cyberbullyings = []
            if handle[0] != '@':
                handle = str('@' + handle)
            for i in list_of_tweets:
                list_of_tweets_and_Cyberbullyings.append((i, analyse.predict_Cyberbullying(i)))
            args = {'list_of_tweets_and_Cyberbullyings': list_of_tweets_and_Cyberbullyings, 'handle': handle}
            return render(request, 'home/Cyberbullying_import_result.html', args)

    else:
        form = Cyberbullying_Imported_Tweet_analyse_form()
        return render(request, 'home/Cyberbullying_import.html')
