from rest_framework import viewsets,filters
from ..models import Post,PostPoint
from .serializers import PostSerializer,PostPointSerializer
from django_filters.rest_framework import \
    DjangoFilterBackend
from rest_framework import generics
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend]
    filterset_fields=['status',]
    search_fields=['title','short_description']

from  rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def PostList(request):
    posts=Post.objects.all()
    serializer=PostSerializer(posts,many=True)
    return Response({'post':serializer.data})

@api_view(['GET'])
def PostDetail(request,pk):
    post=Post.objects.get(id=pk)
    serializer=PostSerializer(post)
    post_points=PostPoint.objects.filter(post=post)
    p_p_serializer=PostPointSerializer(post_points
                                       ,many=True)
    return Response({'post':serializer.data,
                 'post_points':p_p_serializer.data})

