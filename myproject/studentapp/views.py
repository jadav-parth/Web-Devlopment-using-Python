from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def student_api_list(request):
    # 1. GET Request: બધા જ વિદ્યાર્થીઓનો ડેટા JSON ફોર્મેટમાં મોકલવા માટે
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    # 2. POST Request: નવો ડેટા API દ્વારા ડેટાબેઝમાં સેવ કરવા માટે
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 1. Read (List View): બધા જ વિદ્યાર્થીઓની યાદી બતાવવા માટે
def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentapp/student_list.html', {'students': students})

# 2. Create (Add View): નવો રેકોર્ડ ઉમેરવા માટે
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list_url')
    else:
        form = StudentForm()
    return render(request, 'studentapp/student_form.html', {'form': form})

# 3. Update (Edit View): અગાઉના રેકોર્ડમાં સુધારો કરવા માટે
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list_url')
    else:
        form = StudentForm(instance=student)
    return render(request, 'studentapp/student_form.html', {'form': form})

# 4. Delete View: રેકોર્ડ કાઢી નાખવા માટે
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list_url')
    return render(request, 'studentapp/student_confirm_delete.html', {'student': student})