from django.shortcuts import render, redirect
from transformers import pipeline


# Create your views here.


def index(request):
    get_prediction = request.session.get('prediction', None)
    prediction = get_prediction[0]['generated_text']

    return render(request, "main.html", {"prediction": prediction})


def predict(request):
    data = request.POST.get("sentence")

    model_name = "heegyu/ajoublue-gpt2-base"
    pipe = pipeline('text-generation', model=model_name)

    prediction = pipe(data, repetition_penalty=1.2, eos_token_id=1, early_stopping=False,
                      max_new_tokens=128, min_length=64)

    request.session['prediction'] = prediction

    return redirect("main:index")
