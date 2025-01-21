from django.shortcuts import render
from rest_framework.response import Response


class TodosViews:
    def handleTest(self, request):
        return Response("okman")
