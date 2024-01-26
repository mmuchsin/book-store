from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTestCase(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='ucup',
            email='ucup@email.com',
            password='passucup',
        )

        self.assertEqual(user.username, 'ucup')
        self.assertEqual(user.email, 'ucup@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='adminucup',
            email='adminucup@email.com',
            password='passadminucup',
        )

        self.assertEqual(user.username,'adminucup')
        self.assertEqual(user.email, 'adminucup@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)