from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model
        Menu.objects.create(title="Pizza", price=100, inventory=50)
        Menu.objects.create(title="Pasta", price=80, inventory=30)
        Menu.objects.create(title="Salad", price=50, inventory=100)

        # Set up the API client
        self.client = APIClient()

    def test_getall(self):
        # Send a GET request to the MenuItemsView endpoint
        response = self.client.get('/restaurant/menu/items')  # Adjust the URL path as needed

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Serialize the Menu objects manually
        menu_items = Menu.objects.all()
        serialized_data = MenuSerializer(menu_items, many=True).data


        # Verify that the response data matches the serialized data
        self.assertEqual(response.data, serialized_data)
