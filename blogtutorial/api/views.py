from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import openai
from .models import Prompt
from .serializer import PromptSerializer


openai.organization = "org-4syK5rpvVR7nABjSceLGim9e"
# Alpha school's dedicated API key issued on Benjamin's account
openai.api_key = "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"

# Create your views here.
@api_view(['GET'])
def get_prompts(request):
    prompts = Prompt.objects.all()
    serializer = PromptSerializer(prompts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def test_get(request):
    return Response("you reached the test api endpoint!")

@api_view(['POST'])
def post_message(request):
    format, style, subject = map(request.POST.get, ['format', 'style', 'subject'])
    prompt = f"Write a {format} about {subject} in the style of {style}"
    message = make_message(prompt)
    response = get_completion(message)
    return Response(response['choices'][0]['message']['content'])

# Helper functions here
def make_message(prompt):
    return [{"role": "user", "content": prompt}]

def get_completion(
    messages,
    model="gpt-4",
    temperature=1.0,
    top_p=1,
    freq_penalty=0,
    pres_penalty=0,
):
    return openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=freq_penalty,
        presence_penalty=pres_penalty,
        stream=False,
    )