from django.shortcuts import render, HttpResponse
from .models import TodoItem, Part

# Create your views here.

# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Part
# from .models import User

# def list_parts(request):
#     parts = Part.objects.all()
#     output = ''
#     for part in parts:
#         output += f"{part.description}, {part.price}\n"
#
#     return HttpResponse(output)
#
# from django.http import JsonResponse
# from .models import Part
#
# def parts_list(request):
#     # Filter parts where number is 33
#     parts = Part.objects.filter(number=33)
#     data = list(parts.values('number', 'description', 'price', 'weight', 'picture_url'))  # adjust field names as necessary
#     return JsonResponse(data, safe=False)  # `safe=False` is required to allow serializing lists

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Part
from .serializers import PartSerializer

# class PartDetailView(APIView):
#     def get(self, request, number, format=None):
#         part = Part.objects.filter(number=number).first()
#         if part:
#             serializer = PartSerializer(part)
#             return Response(serializer.data)
#         else:
#             return Response({'error': 'Part not found'}, status=status.HTTP_404_NOT_FOUND)
#

from django.http import JsonResponse
from .models import Part

def part_detail(request):
    number = 33  # Hard-code the number here
    try:
        part = Part.objects.get(number=number)
        data = {
            'number': part.number,
            'description': part.description,
            'price': float(part.price),  # Convert Decimal to float for JSON serialization
            'weight': float(part.weight),
            'picture_url': part.picture_url
        }
        return JsonResponse(data)
    except Part.DoesNotExist:
        return JsonResponse({'error': 'Part not found'}, status=404)


# def part_detail(request, number):
#     try:
#         part = Part.objects.get(number=number)
#         data = {
#             'number': part.number,
#             'description': part.description,
#             'price': float(part.price),  # Convert Decimal to float for JSON serialization
#             'weight': float(part.weight),
#             'picture_url': part.picture_url
#         }
#         return JsonResponse(data)
#     except Part.DoesNotExist:
#         return JsonResponse({'error': 'Part not found'}, status=404)


# def user_profile(request, user_id):
#     user = User.objects.get(id=user_id)
#     return render(request, 'user_profile.html', {'user': user})
#
def home(request):
    return render(request, "home.html")
    #return HttpResponse("hello world!")

# def todos(request):
#     items = TodoItem.objects.all()
#     return render(request, "todos.html", {"todos":items})