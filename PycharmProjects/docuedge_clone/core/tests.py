#from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Document
from django.core.files.uploadedfile import SimpleUploadedFile

class DocumentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_document(self):
        file = SimpleUploadedFile("testfile.txt", b"Dummy content")
        data = {'title': 'Test File', 'file': file}
        response = self.client.post('/api/upload/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(Document.objects.first().title, 'Test File')

    def test_list_documents(self):
        Document.objects.create(title='Doc 1', file=SimpleUploadedFile("doc1.txt", b"123"))
        Document.objects.create(title='Doc 2', file=SimpleUploadedFile("doc2.txt", b"456"))
        response = self.client.get('/api/documents/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_portal_view_status(self):
        response = self.client.get('/api/portal/')
        self.assertEqual(response.status_code, 200)