from behave import *

@given("Two numbers are Given")
def step_impl(context):
    context.a = 10
    context.b = 20

@when("Two numbers are added")
def step_impl(context):
    context.sum = context.a + context.b

@then("Sum is displayed")
def step_impl(context):
    print(context.sum)