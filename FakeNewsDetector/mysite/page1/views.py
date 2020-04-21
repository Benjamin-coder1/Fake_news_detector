from django.http import HttpResponse
from django.shortcuts import render
from django import forms

#On initialise la forme du formulaire

class Article(forms.Form):
    article = forms.CharField(label='',widget=forms.TextInput(attrs={'size': '40',
        'placeholder': "Entrez le titre ou l'URL de l'article"}))
# Create your views here.

def home(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    score=0
    form = Article(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        article = form.cleaned_data['article']

        score=len(article)%101
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'page1.html', locals())
