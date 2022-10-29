from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import UserProfile
from .serializer import ProfileSerializor
from rest_api_project.permission import isOwnerOrReadOnly


class DisplayList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        post = UserProfile.objects.all()
        serializer = ProfileSerializor(
            post, many=True, context={'request': request})
        return Response(serializer.data)


class DetailList(APIView):
    permission_classes = [isOwnerOrReadOnly]
    serializer_class = ProfileSerializor

    def get_object(self, pk):
        try:
            profile = UserProfile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile

        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = ProfileSerializor(post, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = ProfileSerializor(
            post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
