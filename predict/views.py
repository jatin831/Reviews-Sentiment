from django.shortcuts import render,HttpResponse
from joblib import load
# Create your views here.
def index(request):
    d = {'prediction' : False}
    return render(request,'review.html',d)
def lemmatize(doc):
        return [i.lemma_ for i in nlp(doc)]
def predict(request):
    text = request.POST.get('review','None')
    model = load('movie_review_model.joblib')
    pred = model.predict([text])[0]
    prob = model.predict_proba([text])[0]
    if pred==1:
        rev = 'prediction : Positive'
        prob = 'Probailty : '+str('%.2f'%(prob[1]*100))+'%'
    else:
        rev = 'Predictdion : Negative'
        prob = 'Probabilty : '+str('%.2f'%(prob[0]*100))+'%'
    d = {'prediction':True,'text':text,'pred':rev,'prob':prob}
    print(d)
    return render(request,'review.html',d)


