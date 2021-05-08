from django.db.utils import IntegrityError

from testing.test import UserTestCase
from .models import Credential


class CredentialsTestCase(UserTestCase):
    def test_creation(self):
        credential = Credential(token='foo', name='bar', user=self.user)
        credential.save()

    def test_name_required(self):
        """ Ensure name is required on Categories """
        credential = Credential(user=self.user)
        with self.assertRaises(IntegrityError):
            credential.save()

    def test_unique_together(self):
        tokens = (
            ('name_foo', 'secret_foo'),
            ('name_bar', 'secret_bar'),
        )

        for name, token in tokens:
            credential, created = Credential.objects.get_or_create(name=name, user=self.user, defaults=dict(token=token))
            self.assertGreater(credential.id, 0)
            self.assertTrue(created)

        for name, token in tokens:
            # Try to re-save existing names for this user
            credential = Credential(name=name, token='token_new_baz', user=self.user)
            self._assertRaisesAtomic(credential.save, IntegrityError)

