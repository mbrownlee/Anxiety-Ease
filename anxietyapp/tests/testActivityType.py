import json
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from anxietyapp.models import ActivityType
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# *  Good rules-of-thumb include having:
#     * a separate TestClass for each model or view, or for us --- every endpoint
#     * a separate test method for each set of conditions you want to test
#     * test method names that describe their function

class TestActivityType(TestCase):

    # setUp() is called before every test function to set up any objects that may be modified by the test (every test function will get a "fresh" version of these objects).
    def setUp(self):
        self.username = 'testuser'
        self.password = 'foobar'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        

    def test_get_activity_types(self):

        new_activity_type = ActivityType.objects.create(
            name="Deep Breathing"
            
             )

        # Now we can grab all the area (meaning the one we just created) from the db
        response = self.client.get(reverse('activitytype-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))

        # Check that the response is 200 OK.
        # This is checking for the GET request result, not the POST. We already checked that POST works in the previous test!
        self.assertEqual(response.status_code, 200)

        # response.data is the python serialized data used to render the JSON, while response.content is the JSON itself.
        # Are we responding with the data we asked for? There's just one parkarea in our dummy db, so it should contain a list with one instance in it
        self.assertEqual(len(response.data), 1)

        # test the contents of the data before it's serialized into JSON
        self.assertEqual(response.data[0]["name"], "Deep Breathing")

        # Finally, test the actual rendered content as the client would receive it.
        # .encode converts from unicode to utf-8. Don't get hung up on this. It's just how we can compare apples to apples
        self.assertIn(new_activity_type.name.encode(), response.content)

    