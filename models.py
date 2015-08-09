"""
Module defines the classes that store the relevant financial details of a user.

Module has the public function that Loads user data from db.

class FinAccounts(object): Class that stores user_id, list of credit cards and list
						   of checking accounts.
class FinAccountCc(object): Class that stores credit card details.
class FinAccountChecking(object): Class that stores checking account details.
"""
import pymysql

from literals import db_literals, qry, dict_elements

class FinAccounts(object):
	"""Class that stores user_id, list of credit cards and list of checking accounts."""
	def __init__(self, user_id):
		self._user_id = user_id
		self._fin_account_cc = []
		self._fin_account_checking = []

	def GetUserId():
		return self._user_id

	def SetUserId(user_id):
		self._user_id = user_id

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		response = "User Id: %s \n\n\nCredit Cards:\n\n" % (self._user_id)
		for element in self._fin_account_cc:
			response += element.__repr__() + "\n"
		response += "\n\n\nChecking Accounts:\n\n"
		for element in self._fin_account_checking:
			response += element.__repr__() + "\n"
		return response


class FinAccountCc(object):
	"""Class that stores credit card details."""
	def __init__(self, credit_limit, balance, min_payment, min_payment_date):
		self._credit_limit = credit_limit
		self._balance = balance
		self._min_payment = min_payment
		self._min_payment_date = min_payment_date

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return "Credit Limit: %s, Balance: %s, Min Payment: %s, Min Payment Date: %s" % (self.GetCreditLimit(), self.GetBalance(), self.GetMinPayment(), self.GetMinPaymentDate())

	def GetCreditLimit(self):
		return self._credit_limit

	def SetCreditLimit(self, credit_limit):
		self._credit_limit = credit_limit

	def GetBalance(self):
		return self._balance

	def SetBalance(self, balance):
		self._balance = balance

	def GetMinPayment(self):
		return self._min_payment

	def SetMinPayment(self, min_payment):
		self._min_payment = min_payment

	def GetMinPaymentDate(self):
		return self._min_payment_date

	def SetMinPaymentDate(self, min_payment_date):
		self._min_payment_date = min_payment_date



class FinAccountChecking(object):
	"""Class that stores checking account details."""
	def __init__(self, av_balance):
		self._av_balance = av_balance

	def __str__(self):
		return "Checking Balance: %s" % (self.GetAvBalance())

	def __repr__(self):
		return self.__str__()

	def GetAvBalance(self):
		return self._av_balance

	def SetAvBalance(self, av_balance):
		self._av_balance = av_balance

def LoadUser(user_id):
	"""Load all relevant data for user_id from FinMan db."""
	connection = pymysql.connect(host=db_literals.host,
                             user=db_literals.user,
                             password=db_literals.password,
                             db=db_literals.db,
                             charset=db_literals.charset,
                             cursorclass=pymysql.cursors.DictCursor)
	fin_account = FinAccounts(user_id)
	with connection.cursor() as cursor:
		qry_cc_accounts = qry.qry_cc_accounts
		cursor.execute(qry_cc_accounts, user_id)
		cc_accounts = cursor.fetchall()
		for cc in cc_accounts:
			fin_account._fin_account_cc.append(FinAccountCc(cc[dict_elements.CREDIT_LIMIT], cc[dict_elements.BALANCE], cc[dict_elements.MIN_PAYMENT], cc[dict_elements.MIN_PAYMENT_DATE]))
		qry_checking_accounts = qry.qry_checking_accounts
		cursor.execute(qry_checking_accounts, user_id)
		checking_accounts = cursor.fetchall()
		for checking in checking_accounts:
			fin_account._fin_account_checking.append(FinAccountChecking(checking[dict_elements.AV_BALANCE]))
