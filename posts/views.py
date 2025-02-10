from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorizedOrReadOnly
# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorizedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#post detail
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorizedOrReadOnly,)
