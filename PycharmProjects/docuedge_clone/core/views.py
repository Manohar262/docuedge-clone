# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Document
from .serializers import DocumentSerializer

# Create your views here.

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello from DocuEdge Clone API!"})

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_document(request):
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_documents(request):
    documents = Document.objects.all().order_by('-uploaded_at')
    serializer = DocumentSerializer(documents, many=True)
    return Response(serializer.data)

from django.shortcuts import render, redirect
from .models import Document

def document_portal(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        if title and file:
            Document.objects.create(title=title, file=file)
            return redirect('document_portal')
    documents = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'core/document_portal.html', {'documents': documents})