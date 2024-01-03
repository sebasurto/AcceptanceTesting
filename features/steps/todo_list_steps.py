from behave import given, when, then
from behave import use_step_matcher

# Step definitions for the "Add a task to the to-do list" feature (Step 1)
use_step_matcher("re")

@given('the to-do list is empty')
def step_empty_todo_list(context):
    context.todo_list = []

@when('I add a task with name "(.*)" and description "(.*)"')
def step_add_task(context, name, description):
    task = {'name': name, 'description': description, 'status': 'Incomplete'}
    context.todo_list.append(task)
    context.last_added_task = task

@then('the task "(.*)" should be in the to-do list')
def step_check_task_in_list(context, name):
    for task in context.todo_list:
        if task['name'] == name:
            assert task == context.last_added_task
            return
    assert False, f'Task "{name}" not found in the to-do list'

# Step definitions for the "List all tasks in the to-do list" feature (Step 2)

@given('the to-do list contains tasks:')
def step_todo_list_contains_tasks(context):
    for row in context.table:
        task = {'name': row['name'], 'description': row['description'], 'status': row['status']}
        context.todo_list.append(task)

@when('I list all tasks')
def step_list_all_tasks(context):
    context.listed_tasks = context.todo_list

@then('I should see the following tasks:')
def step_check_tasks_listed(context):
    for row in context.table:
        name = row['name']
        description = row['description']
        status = row['status']
        found = False
        for task in context.listed_tasks:
            if task['name'] == name and task['description'] == description and task['status'] == status:
                found = True
                break
        assert found, f'Task "{name}" not found in the listed tasks'

# Step definitions for the "Mark a task as completed" feature (Step 3)

@given('the to-do list contains tasks for marking as completed:')
def step_todo_list_contains_tasks_for_marking(context):
    for row in context.table:
        task = {'name': row['name'], 'description': row['description'], 'status': row['status']}
        context.todo_list.append(task)

@when('I mark the task "(.*)" as completed')
def step_mark_task_completed(context, task_name):
    for task in context.todo_list:
        if task['name'] == task_name:
            task['status'] = 'Complete'
            context.marked_task = task
            return

@then('the task "(.*)" should be marked as completed')
def step_check_task_marked_completed(context, task_name):
    for task in context.todo_list:
        if task['name'] == task_name:
            assert task['status'] == 'Complete'
            assert task == context.marked_task
            return
    assert False, f'Task "{task_name}" not found in the to-do list or not marked as completed'

# Step definitions for the "Clear the entire to-do list" feature (Step 4)

@when('I clear the entire to-do list')
def step_clear_entire_todo_list(context):
    context.todo_list = []

@then('the to-do list should be empty')
def step_check_empty_todo_list(context):
    assert len(context.todo_list) == 0

# Step definitions for the "Edit a task in the to-do list" feature (Step 5)

@given('the to-do list contains tasks for editing:')
def step_todo_list_contains_tasks_for_editing(context):
    for row in context.table:
        task = {'name': row['name'], 'description': row['description'], 'status': row['status']}
        context.todo_list.append(task)

@when('I edit the task "(.*)" with new name "(.*)", new description "(.*)", and new status "(.*)"')
def step_edit_task(context, old_task_name, new_name, new_description, new_status):
    for task in context.todo_list:
        if task['name'] == old_task_name:
            task['name'] = new_name
            task['description'] = new_description
            task['status'] = new_status
            context.edited_task = task
            return

@then('the task "(.*)" should be in the to-do list with description "(.*)" and status "(.*)"')
def step_check_task_edited(context, new_name, new_description, new_status):
    assert context.edited_task['name'] == new_name
    assert context.edited_task['description'] == new_description
    assert context.edited_task['status'] == new_status

# Step definitions for the "Delete a specific task from the to-do list" feature (Step 6)

@given('the to-do list contains tasks for deleting:')
def step_todo_list_contains_tasks_for_deleting(context):
    for row in context.table:
        task = {'name': row['name'], 'description': row['description'], 'status': row['status']}
        context.todo_list.append(task)

@when('I delete the task "(.*)"')
def step_delete_task(context, task_name):
    for task in context.todo_list:
        if task['name'] == task_name:
            context.deleted_task = task
            context.todo_list.remove(task)
            return

@then('the task "(.*)" should not be in the to-do list')
def step_check_task_not_in_list(context, task_name):
    for task in context.todo_list:
        assert task['name'] != task_name
    assert context.deleted_task['name'] == task_name

