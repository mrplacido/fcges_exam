from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class Exam1ViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_missing_int_endpoint_scenario_1(self):
        url = '/find_missing_int/'
        payload = {'array': [1, 3, 6, 4, 1, 2]}

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assuming the expected result for the given payload is 5
        self.assertEqual(response.data['result'], 5)

    def test_missing_int_endpoint_scenario_2(self):
        url = '/find_missing_int/'
        payload = {'array': [1, 2, 3]}

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assuming the expected result for the given payload is 4
        self.assertEqual(response.data['result'], 4)

    def test_missing_int_endpoint_scenario_3(self):
        url = '/find_missing_int/'
        payload = {'array': [-1, -1, -1, -5]}

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assuming the expected result for the given payload is 1
        self.assertEqual(response.data['result'], 1)

    def test_missing_int_endpoint_scenario_4(self):
        url = '/find_missing_int/'
        payload = {'array': [1, 3, 6, 4, 1, 7, 8, 10]}

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assuming the expected result for the given payload is 2
        self.assertEqual(response.data['result'], 2)

    def test_invalid_payload(self):
        url = '/find_missing_int/'
        # Invalid payload missing the 'array' key
        invalid_payload = {}

        response = self.client.post(url, invalid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_empty_array(self):
        url = '/find_missing_int/'
        # Empty array should result in the missing integer being 1
        payload = {'array': []}

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 1)


class Exam2ViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_find_divisible_scenario_1(self):
        response = self.client.post('/find_divisible/', {'a': 6, 'b': 11, 'k': 2}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)

    def test_find_divisible_scenario_2(self):
        response = self.client.post('/find_divisible/', {'a': 0, 'b': 11, 'k': 2}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 6)


class Exam3ViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_rotate_array_scenario_1(self):
        # Test case 1
        data = {'array': [3, 8, 9, 7, 6], 'k': 3}
        response = self.client.post('/rotate/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rotated_array'], [9, 7, 6, 3, 8])

    def test_rotate_array_scenario_2(self):
        # Test case 2
        data = {'array': [0, 0, 0], 'k': 1}
        response = self.client.post('/rotate/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rotated_array'], [0, 0, 0])

    def test_rotate_array_scenario_3(self):
        # Test case 3
        data = {'array': [1, 2, 3, 4], 'k': 4}
        response = self.client.post('/rotate/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rotated_array'], [1, 2, 3, 4])