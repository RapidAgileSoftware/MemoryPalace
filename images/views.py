import base64
import io
import json
import torch
import os
from diffusers import StableDiffusionPipeline
from django.conf import settings
from django.shortcuts import render
from torchvision import models, transforms
from torchvision.models import DenseNet
from PIL import Image

from pprint import pprint as pp

commandline_args = os.environ.get('COMMANDLINE_ARGS', "--skip-torch-cuda-test --no-half")

# local imports
# load global variables to avoid expensive reloads with each request
from .forms import ImageUploadForm
from _auth_tokens import token_huggingface

# Label Prediction: load pretrained DenseNet model
'''
model4LabelPrediction: DenseNet = models.densenet121(pretrained=True)
model4LabelPrediction.eval()
# load mapping of ImageNet index to human-readable label
# run `python manage.py collectstatic` first!
json_path = os.path.join(settings.STATIC_ROOT, "imagenet_class_index.json")
imagenet_mapping = json.load(open(json_path))
'''

# Text2Image generation
# model4Diffusion = "runwayml/stable-diffusion-v1-5"

# pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16, use_auth_token=token_huggingface)
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32, use_safetensors=True).to("cpu")
#image = pipe("Bob Marley wearing a smoking going yoga").get_output()


def index(request):
    image = pipe("Bob Marley, wearing a smoking, doing yoga").images[0]
    pp(image)
    context = {
        'image': image,
        'pipeline': pipe
    }
    return render(request, 'images/index.html', context)


def label_prediction(request):
    image_uri = None
    predicted_label = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # passing the image as base64 string to avoid storing it to DB or filesystem
            image = form.cleaned_data['image']
            image_bytes = image.file.read()
            encoded_img = base64.b64encode(image_bytes).decode('ascii')
            image_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)

            try:
                predicted_label = get_prediction(image_bytes)
            except RuntimeError as re:
                print(re)

    else:
        form = ImageUploadForm()

    context = {
        'form': form,
        'image_uri': image_uri,
        'predicted_label': predicted_label,
    }
    return render(request, 'images/label_prediction.html', context)


def transform_image(image_bytes):
    # Transform image into required DenseNet format: 224x224 with 3 RGB channels and normalized.
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    # For given image bytes, predict the label using the pretrained DenseNet
    tensor = transform_image(image_bytes)
    outputs = model4LabelPrediction.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    class_name, human_label = imagenet_mapping[predicted_idx]
    return human_label


def image_generator(request):
    image = pipe("Bob Marley wearing a smoking going yoga").get_output()
    context = {
        'output': image,
    }
    return render(request, 'images/image_generation.html', context)
