from django.http import HttpResponse
from django.shortcuts import render
from django import forms

#On initialise la forme du formulaire

class Article(forms.Form):
    article = forms.CharField(max_length=1000)

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

        score=int(article)%101

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'page1.html', locals())
