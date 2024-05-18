from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import ToDO

from .serializers import (
    ToDoCreateSerializer,
    ToDoDetailSerializer,
    ToDoListSerializer
)

class TodoCreateView(CreateAPIView):
    queryset = ToDO.objects.all()
    serializer_class = ToDoCreateSerializer

class TodoListView(ListAPIView):
    queryset = ToDO.objects.all()
    serializer_class = ToDoListSerializer

class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ToDO.objects.all()
    serializer_class = ToDoDetailSerializer