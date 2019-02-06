from django.contrib.auth.models import User
from rest_framework.test import APIClient
from ..models.property import Property
from rest_framework import status
from django.test import TestCase
from django.urls import reverse



# Test Model
class ModelTestCase(TestCase):
    """This class defines the test suite for the property model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.property_name = "Palko 92"
        self.property = Property(name=self.property_name, owner=user)

    def test_model_can_create_a_property(self):
        """Test the property model can create a property."""
        old_count = Property.objects.count()
        self.property.save()
        new_count = Property.objects.count()
        self.assertNotEqual(old_count, new_count)


# Test View
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # Since user model instance is not serializable, use its Id/PK
        self.property_data = {'name': 'Go to Ibiza', 'owner': user.id}
        self.response = self.client.post(
            reverse('properties'),
            self.property_data,
            format="json")


    def test_api_can_create_a_property(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/properties/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_api_can_get_a_property(self):
        """Test the api can get a given property."""
        property = Property.objects.get(id=1)
        response = self.client.get(
            '/properties/',
            kwargs={'pk': property.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, property)


    def test_api_can_update_property(self):
        """Test the api can update a given property."""
        property = Property.objects.get()
        change_property = {'name': 'Something new'}
        res = self.client.put(
            reverse('property_details', kwargs={'pk': property.id}),
            change_property, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_api_can_delete_property(self):
        """Test the api can delete a property."""
        property = Property.objects.get()
        response = self.client.delete(
            reverse('property_details', kwargs={'pk': property.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
