from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import TestCase

from testing.test import UserTestCase
from .models import Category


class CategoryModelTestCase(UserTestCase):
    def test_creation(self):
        """ Successfully create a new Category """
        category = Category(name='Shopping', user=self.user)
        category.save()
        self.assertEqual(category.id, 1)

        queryset = Category.objects.filter(user=self.user)
        self.assertEqual(len(queryset), 1)

    def test_name_required(self):
        """ Ensure name is required on Categories """
        category = Category(user=self.user)
        with self.assertRaises(IntegrityError):
            category.save()

    def test_unique_together(self):
        """ Ensure name + user are unique together """
        names = ['Shopping', 'Groceries', 'Rent']
        for name in names:
            category, created = Category.objects.get_or_create(name=name, user=self.user)
            self.assertGreater(category.id, 0)
            self.assertTrue(created)

        for name in names:
            category = Category(name=name, user=self.user)
            self._assertRaisesAtomic(category.save, IntegrityError)
