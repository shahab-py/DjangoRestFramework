from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from .models import Person, Question, Answer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status



class Home(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)
    


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True)
        return Response(srz_data, status=status.HTTP_200_OK)
