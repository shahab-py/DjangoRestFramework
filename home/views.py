from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person


class Home(APIView):
    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)
