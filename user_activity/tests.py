from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.utils import timezone

from .models import UserActivity
import datetime


class UserActivitynModelTests(TestCase):

    def test_start_time_in_future(self):

        time = timezone.now() + datetime.timedelta(days=30)
        startTime = UserActivity(start_time=time)
        self.assertIs(startTime.start_time_in_future(), False)

    def test_end_time_in_future(self):

        time = timezone.now() + datetime.timedelta(days=30)
        endTime = UserActivity(end_time=time)
        self.assertIs(endTime.end_time_in_future(), False)
