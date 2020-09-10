import json
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from anxietyapp.models import ActivityDetail, ActivityType
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# *  Good rules-of-thumb include having:
#     * a separate TestClass for each model or view, or for us --- every endpoint
#     * a separate test method for each set of conditions you want to test
#     * test method names that describe their function

class TestActivityDetails(TestCase):

    # setUp() is called before every test function to set up any objects that may be modified by the test (every test function will get a "fresh" version of these objects).
    def setUp(self):
        self.username = 'testuser'
        self.password = 'foobar'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.activity_type = ActivityType.objects.create(name="Deep Thoughts by Jack Handy")

    def test_post_activity_detail(self):

        new_activity_detail = {
            "note": "I'm smart enough and people like me",
            "rating": 2,
            "activity_type_id": 1,
            "user_id": 1
            }

         #  Use the client to send the request and store the response
        response = self.client.post(
            reverse('activitydetail-list'), new_activity_detail, HTTP_AUTHORIZATION='Token ' + str(self.token)
          )

        # Getting 200 back because we have a success url
        self.assertEqual(response.status_code, 200)

        # Query the table to see if there's one activity detail instance in there. Since we are testing a POST request, we don't need to test whether an HTTP GET works. So, we just use the ORM to see if the thing we saved is in the db.
        self.assertEqual(ActivityDetail.objects.count(), 1)

        # And see if it's the one we just added by checking one of the properties. Here, name.
        self.assertEqual(ActivityDetail.objects.get().note, "I'm smart enough and people like me")

    def test_get_activity_detail(self):

        new_activity_detail = ActivityDetail.objects.create(
            note="It's fine. Everything is fine.",
            rating=2,
            activity_type_id=1,
            user_id=1
        )

        # Now we can grab all the details (meaning the one we just created) from the db
        response = self.client.get(reverse('activitydetail-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))

        # Check that the response is 200 OK.
        # This is checking for the GET request result, not the POST. We already checked that POST works in the previous test!
        self.assertEqual(response.status_code, 200)

        # response.data is the python serialized data used to render the JSON, while response.content is the JSON itself.
        # Are we responding with the data we asked for? There's just one parkarea in our dummy db, so it should contain a list with one instance in it
        self.assertEqual(len(response.data), 1)

        # test the contents of the data before it's serialized into JSON
        self.assertEqual(response.data[0]["note"], "It's fine. Everything is fine.")

        # Finally, test the actual rendered content as the client would receive it.
        # .encode converts from unicode to utf-8. Don't get hung up on this. It's just how we can compare apples to apples
        self.assertIn(new_activity_detail.note.encode(), response.content)

    def test_delete_activity_detail(self):

        new_activity_detail = ActivityDetail.objects.create(
            note="I'm freaking out here",
            rating=2,
            activity_type_id=1,
            user_id=1
        )

         #  Use the client to send the request and store the response
        response = self.client.get(reverse('activitydetail-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))


        # Check that the response is 200 OK.
        # This is checking for the GET request result, not the POST. We already checked that POST works in the previous test!
        self.assertEqual(response.status_code, 200)

        # response.data is the python serialized data used to render the JSON, while response.content is the JSON itself.
        # Are we responding with the data we asked for? There's just one parkarea in our dummy db, so it should contain a list with one instance in it
        self.assertEqual(len(response.data), 1)

        # test the contents of the data before it's serialized into JSON
        self.assertEqual(response.data[0]["note"], "I'm freaking out here")

        # Finally, test the actual rendered content as the client would receive it.
        # .encode converts from unicode to utf-8. Don't get hung up on this. It's just how we can compare apples to apples
        self.assertIn(new_activity_detail.note.encode(), response.content)
        
        url = reverse('activitydetail-detail', kwargs={'pk': new_activity_detail.id})

           
        delete_response = self.client.delete(url, HTTP_AUTHORIZATION='Token ' + str(self.token)
          )
        self.assertEqual(delete_response.status_code, 204)