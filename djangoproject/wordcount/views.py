from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']     #원문 글 전체를 text로 받음
    words = text.split()
    wordDictionary = {}

    for word in words:
        if word in wordDictionary:
            #increase
            wordDictionary[word] += 1
        else:
            #add to dictionary
            wordDictionary[word] = 1

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : wordDictionary.items})       #세번째 인자를 사용하는데 사전형 자료형을 사용
