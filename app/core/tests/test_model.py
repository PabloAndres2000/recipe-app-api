from django.test import TestCase
#No es recomendable testear los modelos, por que a lo largo del proyecto puede ir cambiando
#Por eso es mejor utilizar los modelos que vienen por defecto de Django
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful
        """
        email = 'gustavo992@gmial.com'
        password = 'testpass123'
        user = get_user_model().objects.create(
            email=email,
            password=password
        )
        #Si el usuario que ingreso el usuario es identico al usuario que esta registrado retornara un True
        #De lo contrario no pasara el test
        assert user.email == email
        assert user.password == password

    def test_new_user_email_normalized(self):
        email = 'gustavo992@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser('pablito@gmail.com', 'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)