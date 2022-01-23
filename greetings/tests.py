from django.test import TestCase
from .models import Names
from .forms import NameForm


class ModelTesting(TestCase):

    def setUp(self):
        self.name = Names.objects.create(first_name='Bob', last_name='Fisher')

    def test_names_model(self):
        name = self.name
        self.assertTrue(isinstance(name, Names))
        self.assertEqual(str(name), 'Bob Fisher')

    def test_names_form_valid(self):
        form = NameForm(data={
            'first_name': 'Kord',
            'last_name': 'Borry'
            })

        self.assertTrue(form.is_valid())

    def test_names_form_valid_2(self):
        form = NameForm(data={
            'first_name': 'Albus',
            'last_name': 'Borry'
            })

        self.assertTrue(form.is_valid())

    def test_names_form_invalid(self):
        form = NameForm(data={})

        self.assertFalse(form.is_valid())

    def test_names_form_invalid_2(self):
        form = NameForm(data={
            'first_name': 'Bob',
            'last_name': 'Fisher'
            })

        # invalid cause Bob Fisher is in Database
        self.assertFalse(form.is_valid())
