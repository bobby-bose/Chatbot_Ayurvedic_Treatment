from django.shortcuts import render
from . import disease
def home(request):
    if request.method == 'POST':
        # get the text submitted through the post method
        text = request.POST['text']
        # print the text
        print(text)
        # then try to tokenize using the NLP methods
        # and then try to predict the sentiment
        # and then try to return the result

        tokized_text = text.split().lower()
        print(tokized_text)

        sentiments = []
        for word in tokized_text:
            positive_words = [
                'happy', 'good', 'joy', 'excited', 'fun', 'awesome', 'amazing', 'fantastic',
                'excellent', 'wonderful', 'terrific', 'delightful', 'blissful', 'content', 'vibrant',
                'enthusiastic', 'glorious', 'thrilled', 'ecstatic', 'jovial', 'lively', 'upbeat',
                'exhilarating', 'radiant', 'cheerful', 'magnificent', 'splendid', 'brilliant', 'gleeful',
                'buoyant', 'exuberant', 'charming', 'enchanting', 'grateful', 'optimistic', 'sunny',
                'joyful', 'elated', 'euphoric', 'bliss', 'merry', 'festive', 'peppy', 'spirited',
                'refreshed', 'jubilant', 'vivacious', 'zestful', 'heartwarming', 'thriving', 'buoyed',
                'blessed', 'cheery', 'lighthearted', 'sparkling', 'dynamic', 'sparkly', 'rapturous',
                'ecstasy', 'glad', 'exciting', 'exhilarated', 'animated', 'festivity', 'glee', 'heartening',
                'hilarious', 'jolly', 'overjoyed', 'pleasurable', 'blithe', 'giddy', 'peachy', 'radiating',
                'satisfying', 'smiling', 'jocund', 'elevated', 'enlivened', 'sunny', 'exultant', 'festal',
                'joking', 'positive', 'rejoicing', 'bright', 'hopeful', 'chipper', 'hurray', 'light-hearted',
                'thrill', 'uplifting', 'zippy', 'effervescent', 'genial', 'gleaming', 'rejoice', 'revived',
                'romantic', 'sunshine', 'vitality', 'youthful', 'optimism', 'joyous', 'optimistic'
            ]
            negative_words = [
                'sad', 'bad', 'unhappy', 'angry', 'depressed', 'disappointed', 'frustrated', 'miserable',
                'upset', 'distressed', 'gloomy', 'grief', 'grim', 'melancholy', 'sorrowful', 'woeful',
                'wretched', 'despair', 'desperate', 'heartbroken', 'anguished', 'bitter', 'dismal', 'forlorn',
                'mournful', 'painful', 'regretful', 'suffering', 'tearful', 'troubled', 'unfortunate', 'bleak',
                'dejected', 'downhearted', 'glum', 'hurt', 'lonely', 'sorry', 'somber', 'unpleasant', 'furious',
                'hostile', 'irate', 'mad', 'outraged', 'resentful', 'sulky', 'sullen', 'tense', 'uncomfortable',
                'annoyed', 'cross', 'enraged', 'exasperated', 'indignant', 'irritated', 'offended', 'aggravated',
                'disgusted', 'disturbed', 'irksome', 'offensive', 'repulsive', 'troublesome', 'vexed', 'bitterness',
                'displeased', 'fed up', 'fuming', 'livid', 'miffed', 'peeved', 'riled up', 'seething', 'upset',
                'weary', 'discontent', 'dissatisfied', 'frustrating', 'grouchy', 'grumpy', 'maddening', 'peeved',
                'petulant', 'testy', 'ticked off', 'unhappy', 'unpleasant', 'upset'
            ]
            if word in positive_words:
                sentiments.append('positive')
            elif word in negative_words:
                sentiments.append('negative')
            else:
                sentiments.append('neutral')

        # then return the result
        return render(request, 'research.html', {'text': text})
    return render(request, 'home.html')


def research(request):
    if request.method == 'POST':
        text = request.POST['text']
        text_lower = text.lower()
        return render(request, 'disease_detection.html', {'text': text_lower})
    return render(request, 'research.html')


def home(request):


    return render(request, 'home.html')


def disease_detection(request):
    if request.method == 'POST':
        text = request.POST['text']
        text_lower = text.lower()

        # Add disease detection logic here using Python
        diseases_detected = disease.diseases_detected  # Example diseases detected

        return render(request, 'disease_detection.html', {'text': text_lower, 'diseases': diseases_detected})

    return render(request, 'disease_detection.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def recommendation(request):
    return render(request, 'recommendation.html')

def checkout(request):
    return render(request, 'checkout.html')

def payments(request):
    return render(request, 'payments.html')
