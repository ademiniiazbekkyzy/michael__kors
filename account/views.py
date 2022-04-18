# Create your views here.


# class RegisterApiView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             message = 'You have successfully registered. An activation email has been sent to you.'
#             return Response(message, status=201)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

