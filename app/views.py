from django.shortcuts import render , HttpResponse
import requests
import nltk

# Create your views here.

def index(request):
    return render(request, 'app/base.html')

def test(request):
#from nltk import FreqDist
#from nltk.book import *
	readFile = open("C:\\Users\\lucifer\\pythonWebApp\\app\\test.txt","r")
	#outputFile = open("output.txt","w+")
	conatant = readFile.read()
	text = nltk.word_tokenize(conatant)
	text1 = nltk.Text(text)
	a  = nltk.pos_tag(text)
	#return HttpResponse(a)
	#cbc ="abc"
	return render(request, 'app/words.html',{ 'words' : a})
    
def base(request):
	return HttpResponse(" hsgdhsdg ")