from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from .models import Person, Question, Answer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from permissions import IsOwnerOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle



class Home(APIView):
    permission_classes = [AllowAny,]
    serializer_class = QuestionSerializer
    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)
    


class QuestionListView(APIView):

    """
        LIST VIEW FOR QUESTIONS
    """

    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)
    

class QuestionCreateView(APIView):

    """
        CREATE QUESTIONS
    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = QuestionSerializer

    def post(self, request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class QuestionUpdateView(APIView):

    """
        UPDATE QUESTIONS 
    """

    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = QuestionSerializer
    
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial = True)
        if srz_data.is_valid():
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    


class QuestionDeleteView(APIView):

    """
        DELETE QUESTIONS
    """
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = QuestionSerializer

    def delete(self, request, pk):
        question = Question.objects.get(pk = pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response({'messages':'question deleted'}, status=status.HTTP_200_OK)
