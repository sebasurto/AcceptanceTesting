# Steps para la característica: Add a task to the to-do list (1)

from behave import given, when, then

@given('the to-do list is empty')
def step_given_empty_todo_list(context):
    context.to_do_list = []

@when('I add a task with name "{name}" and description "{description}"')
def step_add_task(context, name, description):
    task = {'name': name, 'description': description, 'status': 'Incomplete'}
    context.to_do_list.append(task)

@then('the task "{name}" should be in the to-do list')
def step_task_in_todo_list(context, name):
    task_names = [task['name'] for task in context.to_do_list]
    assert name in task_names


# Steps para la característica: List all tasks in the to-do list (2)

@given(u'the to-do list contains tasks')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the to-do list contains tasks')

@when('I list all tasks')
def step_list_all_tasks(context):
    pass  # No action needed, as this is just a verification step

@then(u'I should see the following tasks')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the following tasks')


# Steps para la característica: Mark a task as completed (3)

@when('I mark the task "{task_name}" as completed')
def step_mark_task_as_completed(context, task_name):
    for task in context.to_do_list:
        if task['name'] == task_name:
            task['status'] = 'Complete'
            break

@then('the task "{task_name}" should be marked as completed')
def step_verify_task_completed(context, task_name):
    for task in context.to_do_list:
        if task['name'] == task_name:
            assert task['status'] == 'Complete'
            break


# Steps para la característica: Clear the entire to-do list (4)

@when('I clear the entire to-do list')
def step_clear_entire_todo_list(context):
    context.to_do_list.clear()

@then('the to-do list should be empty')
def step_verify_empty_todo_list(context):
    assert len(context.to_do_list) == 0


# Steps para la característica: Edit a task in the to-do list (5)

@when('I edit the task "{old_task_name}" with new name "{new_name}", new description "{new_description}", and new status "{new_status}"')
def step_edit_task(context, old_task_name, new_name, new_description, new_status):
    for task in context.to_do_list:
        if task['name'] == old_task_name:
            task['name'] = new_name
            task['description'] = new_description
            task['status'] = new_status
            break

@then('the task "{new_name}" should be in the to-do list with description "{new_description}" and status "{new_status}"')
def step_verify_edited_task(context, new_name, new_description, new_status):
    for task in context.to_do_list:
        if task['name'] == new_name:
            assert task['description'] == new_description
            assert task['status'] == new_status
            break


# Steps para la característica: Delete a specific task from the to-do list (6)

@when('I delete the task "{task_name}"')
def step_delete_task(context, task_name):
    for task in context.to_do_list:
        if task['name'] == task_name:
            context.to_do_list.remove(task)
            break

@then('the task "{task_name}" should not be in the to-do list')
def step_verify_task_not_in_list(context, task_name):
    task_names = [task['name'] for task in context.to_do_list]
    assert task_name not in task_names



