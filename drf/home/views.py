from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def list_book(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response({'payload':serializer.data, 'message':"Books are successfully displaying"})


class StudentAPI(APIView):

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response({'payload':serializer.data, 'message':'All students are listed'})
    
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'messges':"Sorry try again"})
        serializer.save()
        return Response({'payload':serializer.data, 'messages':'Student added successfully'})
    
    def put(self, request):
        try:
            student = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student, data=request.data)
            if not serializer.is_valid():
                return Response({'messages':'Sorry credentials didnot match'})
            serializer.save()
            return Response({'messages':'Student updated successfully','payload':serializer.data})
        except Exception as e:
            print(e)
            return Response({'messages' : "Sorry id didnot match"})
    
    def patch(self, request):
        try:
            student = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(instance=student, data=request.data, partial=True)
            # if not serializer.is_valid():
            #     return Response({'messages':'Sorry credentials didnot match'})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'messages':'Student updated successfully','payload':serializer.data})
        except Exception as e:
            print(e)
            return Response({'messages' : "Sorry id didnot match"})
    
    
    def delete(self, request):
        try:
            student = Student.objects.get(id=request.GET.get('id'))
            student.delete()
            return Response({'messages':'Student deleted successfully'})

        except Exception as e:
            print(e)
            return Response({'messages':'there is no data of id '})
    














# @api_view(['GET'])
# def home(request):
#     student_objs= Student.objects.all()
#     serializers = StudentSerializer(student_objs, many=True)


#     return Response({'status':200, 'payload': serializers.data })


# @api_view(['POST'])
# def createData(request):
#     data = request.data
#     serializer = StudentSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response({'status' : 403,'messges':serializer.errors})
#     serializer.save()

#     return Response({'status':201, 'payload':serializer.data, 'messages':'Submitted'})

# @api_view(['get'])
# def view_data(request, id):
#     try:
#         student = Student.objects.filter(id=id)
#         serializer = StudentSerializer(student, many=True)
#         return Response({'status': 200, 'payload':serializer.data})

#     except Exception as e:
#         return Response({'status':400})

# @api_view(['PUT'])
# def update_data(request, id):
#     try:
#         student = Student.objects.filter(id = id)    
#         serializer = StudentSerializer(student, data = request.data, partial = True)
#         if not serializer.is_valid():
#             return Response({'status': 403, 'errors': serializer.errors})
#         serializer.save()
#         return Response({'status':200, "payload":serializer.data, 'messages' : 'Successfully updated'})
#     except Exception as e:
#         return Response({'status':403})


# @api_view(['DELETE'])
# def delete_data(request, id):
#     student = Student.objects.filter(id=id)
#     student.delete()
#     return Response({'messages': 'Data deleted'})



# @api_view(['DELETE'])
# def delete_book(request, id):
#     book = Book.objects.get(id=id)
#     book.delete()
#     return Response({'messages': 'book deleted successfully'})

# @api_view(['POST'])
# def add_book(request):
#     data = request.data
#     serializer = BookSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response({'status': 400, 'messages': 'sorry try again'})
#     serializer.save()
#     return Response({'status':200, 'messages':'Book added succcessfully'})