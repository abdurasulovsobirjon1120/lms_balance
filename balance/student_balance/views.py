from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.timezone import now
from datetime import date
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_balance/student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_balance/student_detail.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        start_date = request.POST.get('start_date')

        start_date = date.fromisoformat(start_date)
        today = date.today()
        days_passed = (today - start_date).days

        if days_passed >= 0:
            balance = -(days_passed // 30) * 500000
        else:
            balance = 0

        if balance < 0:
            status = 'qarzdor'
        else:
            status = 'to\'langan'

        student = Student(
            first_name=first_name,
            last_name=last_name,
            start_date=start_date,
            balance=balance,
            status=status
        )
        student.save()

        return redirect('student_list')

    return render(request, 'student_balance/add_student.html')


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')
