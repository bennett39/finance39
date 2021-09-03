from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from transactions.views import TransactionViewSet
from django.contrib.auth.models import User


class UnauthenticatedTransactionTestCase(TestCase):
    def test_unauthenticated(self):
        factory = APIRequestFactory()
        view = TransactionViewSet.as_view({'get': 'list'})
        request = factory.get('api/transactions/')

        # Don't authenticate a user - should be forbidden
        response = view(request)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.status_text, 'Forbidden')


class AuthenticatedTransactionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', email=f'test@test.com')

    def test_authenticated(self):
        factory = APIRequestFactory()
        view = TransactionViewSet.as_view({'get': 'list'})
        request = factory.get('api/transactions/')

        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.render().content, b'[]')
