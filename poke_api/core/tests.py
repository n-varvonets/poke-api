from django.test import Client, TestCase

# Create your tests here.
class IndexTestCase(TestCase):
    def setUp(self) -> None:
        # данная функция будет вьізваться перед началом каждого теста
        # в ней мьі будем инииализировать полуение http клиенат
        self.client = Client()

    def test_get_index_endpoint(self):
        # добавим функцию с апросом к главной странице с методом get
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


