from django.contrib.auth.models import User
from django.db import transaction
from django.test import TestCase

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='secret'
        )

    def _assertRaisesAtomic(self, func, err):
        with self.assertRaises(err):
            with transaction.atomic():
                func()



