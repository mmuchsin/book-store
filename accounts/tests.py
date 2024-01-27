from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

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
    username = 'newuser'
    email = 'newuser@email.com'
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_template_name(self):
        self.assertTemplateUsed(self.response,'account/signup.html')

    def test_signup_content(self):
        self.assertContains(self.response, 'Sign Up Page')

    def test_signup_invalid_content(self):
        self.assertNotContains(self.response, 'ngawurr coyyy')

    def test_signup_form(self):
        get_user_model().objects.create_user(self.username, self.email) # create dummy user
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)