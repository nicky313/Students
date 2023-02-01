from django.shortcuts import render, HttpResponse, redirect
from .models import Student

# Create your views here.
def index(request, st_id=0):

    # print(st_id)

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        new_std = Student(first_name=first_name, last_name=last_name)
        new_std.save()
        return redirect('/');
    if st_id:
       try:
            student = Student.objects.get(id=st_id)
            context = {
                'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name
            }
       except:
           return HttpResponse('Please Enter a Valid Student Id.')
    else:
        students = Student.objects.all()
        context = {
            'students': students
        }

    return render(request, 'index.html', context)




def update(request, st_id=0):
    print(st_id)

    if request.method == 'POST':
        id = request.POST['stid']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        print(first_name)
        if id:
            try:
                Student.objects.filter(id=id).update(first_name=first_name, last_name=last_name)
                return redirect('/');
            except:
                return HttpResponse('Please Enter a Valid Student Id.')
    if st_id:
        try:
            student = Student.objects.get(id=st_id)
            context = {
                'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name
            }
        except:
            return HttpResponse('Please Enter a Valid Student Id..')
    else:
        return HttpResponse('Please Enter a Valid Student Id...')

    return render(request, 'update.html', context)






def remove_std(request, st_id=0):
    if st_id:
        try:
            std_to_be_removed = Student.objects.get(id=st_id)
            std_to_be_removed.delete()
            return redirect('/');
        except:
            return HttpResponse('Please Enter a Valid Employee Id')







def add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        new_std = Student(first_name=first_name, last_name=last_name)
        new_std.save()
        return redirect('/');
    elif request.method == 'GET':
        return render(request, 'add.html')
    else:
        return HttpResponse('AnException Occurred! Student has not been added')






















