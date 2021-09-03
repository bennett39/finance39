from django.db.utils import IntegrityError

from testing.test import UserTestCase
from credentials.models import Credential


class CredentialsTestCase(UserTestCase):
    def test_creation(self):
        credential = Credential(token='foo', name='bar', user=self.user,
                token_type=Credential.PLAID_CLIENT_ID)
        credential.save()

    def test_name_required(self):
        """ Ensure name is required on Categories """
        credential = Credential(user=self.user, token='abc', token_type=Credential.PLAID_CLIENT_ID)
        with self.assertRaises(IntegrityError):
            credential.save()

    def test_token_type_required(self):
        credential = Credential(user=self.user, token='abc', name='test')
        with self.assertRaises(IntegrityError):
            credential.save()

    def test_unique_together(self):
        tokens = (
            ('name_foo', 'secret_foo'),
            ('name_bar', 'secret_bar'),
        )

        for name, token in tokens:
            credential, created = Credential.objects.get_or_create(
                    name=name,
                    user=self.user,
                    defaults=dict(token=token, token_type=Credential.PLAID_CLIENT_ID)
                )
            self.assertIsNotNone(credential.uuid)
            self.assertTrue(created)

        for name, token in tokens:
            # Try to re-save existing names for this user
            credential = Credential(name=name, token='token_new_baz', token_type=Credential.PLAID_CLIENT_ID, user=self.user)
            self._assertRaisesAtomic(credential.save, IntegrityError)

