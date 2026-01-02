from django.urls import path


from employee.views import info1, m1, save_employee, employee_data, update_name

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

    path( 'save/' ,m1),

     path('save1/',save_employee),

    path('manage/', employee_data),



    path('update1/',update_name),






]
