from django.shortcuts import render, redirect
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel, AutoTokenizer
import requests
import unicodedata
from io import BytesIO
from PIL import Image


# Create your views here.


def index(request):
    get_prediction = request.session.get('prediction', None)
    if get_prediction is not None:
        prediction = get_prediction[0]['generated_text']
        request.session.delete('prediction')
    else:
        prediction = None
    return render(request, "main.html", {"prediction": prediction})


def predict(request):
    data = request.POST.get("sentence")

    model_name = "heegyu/ajoublue-gpt2-base"
    pipe = pipeline('text-generation', model=model_name)

    prediction = pipe(data, repetition_penalty=1.2, eos_token_id=1, early_stopping=False,
                      max_new_tokens=128, min_length=64)

    request.session['prediction'] = prediction

    return redirect("main:index")


def predict_image(request):
    data = request.FILES.get("image_file", None)

    if data:
        processor = TrOCRProcessor.from_pretrained("ddobokki/ko-trocr")
        model = VisionEncoderDecoderModel.from_pretrained("ddobokki/ko-trocr")
        tokenizer = AutoTokenizer.from_pretrained("ddobokki/ko-trocr")

        img = Image.open(BytesIO(data.read()))

        pixel_values = processor(img, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values, max_length=64)
        generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        generated_text = unicodedata.normalize("NFC", generated_text)
        request.session['image'] = generated_text

    else:

        return render(request, "image_result.html")

    return redirect("main:image_result")


def image_result(request):
    image = request.session.get('image', None)

    if image is not None:
        image_data = image
        request.session.delete('image')
    else:
        image_data = None

    return render(request, "image_result.html", {"image": image_data})
