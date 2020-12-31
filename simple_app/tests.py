from django.test import TestCase
from django.urls import reverse

from .models import Transaction

# Create your tests here.
class AppTest(TestCase):

    def setUp(self):
        Transaction.objects.create(cc_num='1234567890', exp_date='01/21', cvc_num='999')

    def test_transaction_contents(self):
        transaction = Transaction.objects.get(id=1)
        expected_ccnum = f'{transaction.cc_num}'
        expected_expdate = f'{transaction.exp_date}'
        expected_cvcnum = f'{transaction.cvc_num}'

        self.assertEqual(expected_ccnum, '1234567890')
        self.assertEqual(expected_expdate, '01/21')
        self.assertEqual(expected_cvcnum, '999')

    def test_transaction_str_repr(self):
        transaction = Transaction.objects.get(id=1)
        self.assertEqual(str(transaction), 'Transaction 1')

    def test_transaction_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Transaction 1')
        self.assertTemplateUsed(response, 'index.html')

    def test_transaction_detail_view(self):
        response = self.client.get('/1/')
        no_response = self.client.get('/999999/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, '1234567890')
        self.assertTemplateUsed(response, 'detail.html')
