from django.test import TestCase, Client
from .models import Item

# Create your tests here.
class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def setUp(self):
        self.item_instance = Item.objects.create(
            name='Test Item',
            amount=100,
            description='Test Description',
            categories='Test Category'
        )

    def test_model_fields(self):
        item = Item.objects.get(id=self.item_instance.id)
        self.assertEqual(item.name, 'Test Item')
        self.assertEqual(item.amount, 100)
        self.assertEqual(item.description, 'Test Description')
        self.assertEqual(item.categories, 'Test Category')

