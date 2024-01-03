from behave import *

to_do_list = []

@given('the to-do list is empty')
def step_impl(context):
    context.to_do_list = []

@when('I add a task with name "{name}" and description "{description}"')
def step_impl(context, name, description):
    task = {'name': name, 'description': description, 'status': 'Incomplete'}
    context.to_do_list.append(task)

@then('the task "{name}" should be in the to-do list')
def step_impl(context, name):
    for task in context.to_do_list:
        if task['name'] == name:
            assert True
            return
    assert False
