from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .views import SignUpView
from .forms import CustomUserCreationForm

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


class SignUpTestCase(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_template_name(self):
        self.assertTemplateUsed(self.response,'registration/signup.html')

    def test_signup_content(self):
        self.assertContains(self.response, 'Sign Up Page')

    def test_signup_invalid_content(self):
        self.assertNotContains(self.response, 'ngawurr coyyy')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)

    def test_signup_form(self):
        form = self.response.context.get('form', 'invalid key: form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertTrue(self.response, 'csrfmiddlewatetoken')