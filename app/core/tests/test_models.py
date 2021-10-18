from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_model_with_email_successful(self):
        """Test creating a user with email successfully"""
        email = 'test@randommail.de'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized_email(self):
        email = 'klar@ZUGROSS.DE'
        user = get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_validation_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass124')

    def test_create_superuser(self):
        email = 'klar@ZUGROSS.DE'
        superuser = get_user_model().objects.create_superuser(
            email,
            'test1234'
        )

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
