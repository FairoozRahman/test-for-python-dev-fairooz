from django.shortcuts import redirect, render
from .models import Analysis
from .forms import AnalysisForm
from .utils import AnalyzeText
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import AnalysisSerializer
from rest_framework.response import Response


# Returns the form for text input, once an input is submitted it analyses the text and redirects to results page
def text_analysis(request):
    form = AnalysisForm()

    # If the form is submitted with text data, we use the data to predict the sentiment
    if request.method == 'POST':
        form = AnalysisForm(request.POST) # The submitted data is put in the form
        if form.is_valid(): # Check if the form is valid
            text_data = form.save(commit=False) # save the data in a variable before saving in database
            text_data.result =  AnalyzeText(text_data.text) # Analyzing the text with the Hugging Face pretrained model
            text_data.save() # Saving the text data and analysis result in the database
            messages.success(request, 'Text data is analyzed!')
            return redirect('analysis', pk=text_data.id) # redirect to another page to show the result
        else:
            messages.error(request, 'Text data is invalid!')

    context = {'form': form}
    return render(request, 'analyze/text-analysis.html', context)


# Shows the sentiment prediction of the input text
def result(request, pk):
    sentiment = Analysis.objects.get(id=pk) # Query to get the data of the requested object
    context = {'text': sentiment.text, 'result': sentiment.result}
    return render(request, 'analyze/result.html', context)


# API to submit the text for sentiment prediction
@api_view(['POST'])
def postAnalyze(request):
    # Try to get the POST request, make sure there is no error that is not handled 
    try:
        serializer = AnalysisSerializer(data=request.data) # The submitted data is put in the serializer
        text = serializer.initial_data['text'] 
        sentiment = AnalyzeText(text) # Analyzing the text with the Hugging Face pretrained model
        serializer.initial_data['result'] = sentiment
        if serializer.is_valid(): # Check if the serializer is valid
            serializer.save() # Saving the serializer in the database
            return Response({"sentiment": serializer.data['result']})
        else:
            return Response({"error": serializer.errors})
    except:
        return Response({"error": "Form cannot be empty!"})


