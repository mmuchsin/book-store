from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
        return super().setUp()

    def test_home_page_exits_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, 'Ucup Home Page')

    def test_home_page_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'Iki ra ono woyyy')

    def test_home_page_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
        return super().setUp()

    def test_about_page_exits_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_about_page_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'Iki ra ono woyyy')

    def test_about_page_url_resolves_aboutpageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)