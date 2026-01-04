from django.urls import path


from employee.views import info1, save_employee, update_name, delete_employee, get_employee_details

#from .views import hello_world, save_world, update_world, addition, subtraction, multiplication

urlpatterns = [
    # path('hello/', hello_world, name='hello'),
    # path('save/', save_world, ),
    # path('update/', update_world, ),
    #
    # path('addition/', addition, ),
    #
    # path('subtraction/', subtraction, ),
    #
    # path('multiplication/', multiplication, ),
    # path('details/', get_details, ),

     path('save1/',save_employee),

    path('delete/',delete_employee),

    path('update1/',update_name),

    path('get-details/',get_employee_details )






]
