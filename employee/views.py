from http import HTTPStatus

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from employee.models import Employee


# def hello_world(request):
#     return HttpResponse("Hello World from Employee App")
#
#
# def save_world(request):
#     return HttpResponse("I am saving the employee file")
#
#
# def update_world(request):
#     return HttpResponse("I am updating the employee file")
#
# def employee_details(request):
#     details={
#         "name":"Shub",
#         "address": "sahur",
#         "city": "wardha",
#         "state": "mh",
#         "zipcode": "12",
#         "phone": "7689",
#         "email": "sh@gmail",
#     }
#
#     return JsonResponse(details)
#
#
# def addition(request):
#     a=10
#     b=20
#     return JsonResponse({"sum":a + b})
#     #return HttpResponse(f"Addition of 2 no is= {a+b}")
#
# def subtraction(request):
#     a=45
#     b=10
#     return JsonResponse({"subtraction":a-b})

# def multiplication(request):
#     a=20
#     b=35
#     return HttpResponse({"multiplication":a*b})

# @api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
# def get_details(request):
#
#     print(f"*****{request.method}******")
#     if request.method == "GET":
#         details={
#             "api response":"ITS GET METHOD",
#         }
#
#     elif request.method == "POST":
#         details={
#             "api response":"ITS POST METHOD",
#         }
#
#     else:
#         details={
#             "api response":"ITS METHOD",
#         }
#     return JsonResponse(details)

@api_view(['GET', 'POST'])
def info1(request):
    method = request.method
    print("shubham")

    if method == 'GET':
        name = request.query_params.get('name')
        age = request.query_params.get('age')
        res = {
            "name": f"My Name is {name} and I'm {age} years old"
        }
        return JsonResponse(res)

    elif method == 'POST':
        data = request.data
        print(data)
        return JsonResponse(data)

    else:
        return JsonResponse()


@api_view(['GET', 'POST'])
def m1(request):
    method = request.method

    if method == 'GET':
        name = request.query_params.get('name')
        age = request.query_params.get('age')
        res = {
            "res": f"My Name is {name} and I'm {age} years old"
        }
        return JsonResponse(res)

    elif method == 'POST':
        # Read all request data
        data = request.data

        # create employee instance
        emp = Employee()

        # set all values
        emp.name = data.get("name")
        emp.age = data.get("age")
        emp.salary = data.get("salary")
        emp.address = data.get("address")
        emp.email = data.get("email")

        emp.save()
        res = {
            "mesg": "your data successfully saved"
        }

        return JsonResponse(res)


@api_view(['POST'])
def save_employee(request):
    method = request.method
    if method == 'POST':
        print(request.data)
        name = request.data.get("name")
        age = request.data.get("age")
        salary = request.data.get("salary")
        address = request.data.get("address")
        email = request.data.get("email")
        mobile = request.data.get("mobile")
        dob = request.data.get("dob")
        gender = request.data.get("gender")

        emp = Employee()
        emp.name = name
        emp.age = age
        emp.salary = salary
        emp.address = address
        emp.email = email
        emp.mobile = mobile
        emp.dob = dob
        emp.gender = gender

        emp.save()

        res = {
            " mesg": "your data is successfully saved "
        }

        return JsonResponse(res)


@api_view(['GET', 'POST'])
def employee_data(request):
    method = request.method
    if method == 'POST':
        mobile = request.data.get("mobile")
        name = request.data.get("name")
        email = request.data.get("email")
        age = request.data.get("age")
        emp = Employee()
        emp.email = email
        emp.name = name
        emp.mobile = mobile
        emp.age = age

        emp.save()
        res = {
            "mesg": "your data fill successfully"

        }
        return JsonResponse(res)


@api_view(['PATCH'])
def update_employee(request):
    method = request.method
    if method == 'PATCH':
        data = request.data
        employee_id = data.get("id")
        emp = Employee.objects.get(id=employee_id)
        print(emp)
        emp.age = data.get("age")
        emp.address = data.get("address")
        emp.save()
        res = {
            "mesg": "your data update successfully"

        }
        return JsonResponse(res)


@api_view(['PATCH'])
def update_name(request):
    method = request.method
    if method == 'PATCH':
        data = request.data
        employee_id = data.get("id")
        emp = Employee.objects.get(id=employee_id)
        print(emp)
        emp.age = data.get("age")
        emp.address = data.get("address")
        emp.mobile = data.get("mobile")
        emp.salary = data.get("salary")
        emp.name = data.get("name")
        emp.email = data.get("email")
        emp.mobile = data.get("mobile")
        emp.dob = data.get("dob")
        emp.gender = data.get("gender")

        emp.save()
        res = {
            "mesg": "successfully update name"

        }
        return JsonResponse(res)

@api_view(['DELETE'])
def delete_employee(request,pk):
    method = request.method
    if method == 'DELETE':
        emp = Employee.objects.get(id=pk)
        emp.delete()
        res = {
            "mesg": "successfully record  deleted"

        }
        return JsonResponse(res)

