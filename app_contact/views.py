from rest_framework.viewsets import ModelViewSet

from .models import InfoForMainPage
from .serializers import InformationForMainPageSerializer


# Create your views here.
class InformationForMainPageVIewSet(ModelViewSet):
    queryset = InfoForMainPage.objects.all()
    serializer_class = InformationForMainPageSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class ContactCreateView(CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
