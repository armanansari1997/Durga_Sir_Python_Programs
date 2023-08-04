from behave import *


@given('Book details')
def impl_bk(context):
    print('Book details entered')
    # print('Book2')


@then('Verify book name')
def impl_bk(context):
    print('Verify book name')
    # print('Verify2')
