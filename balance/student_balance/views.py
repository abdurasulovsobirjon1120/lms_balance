from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import date
from .models import Student


def student_list(request):
    students = Student.objects.all()
    for student in students:
        update_student_balance(student)
    return render(request, 'student_balance/student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    update_student_balance(student)
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
            balance = -(days_passed * 10000)
        else:
            balance = 0
        status = 'qarzdor' if balance < 0 else 'to\'langan'

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


def update_student_balance(student):
    today = date.today()
    days_passed = (today - student.start_date).days
    if days_passed >= 0:
        student.balance = -(days_passed * 10000)
    else:
        student.balance = 0

    student.status = 'qarzdor' if student.balance < 0 else 'to\'langan'
    student.save()
