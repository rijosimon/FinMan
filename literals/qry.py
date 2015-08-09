qry_cc_accounts = "select f_c.CREDIT_LIMIT, f_c.BALANCE, f_c.MIN_PAYMENT, f_c.MIN_PAYMENT_DATE from fin_accounts as fin inner join fin_account_cc as f_c on fin.ID = f_c.ID where fin.TYPE = 'Credit' and fin.USER_ID = %s"
qry_checking_accounts = "select f_ck.AV_BALANCE from fin_accounts as fin inner join fin_account_checking as f_ck on fin.ID = f_ck.ID where fin.USER_ID = %s and fin.TYPE = 'Checking'"