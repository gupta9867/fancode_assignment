from collections import defaultdict
from ..api_automation_framework.get_method import get_status_code, get_response_body
from ..api_automation_framework.report_utils import create_test


def get_fan_code_users(users_response):
    fan_code_users = set()
    if users_response:
        users_data = users_response.json()
        for user in users_data:
            geo = user.get("address", {}).get("geo", {})
            lat = geo.get("lat")  # -40 to 5
            lat = float(lat) if lat else lat

            long = geo.get("lng")  # 5 to 100
            long = float(long) if long else long

            if lat and long and (-40 < lat < 5) and (5 < long < 100):
                fan_code_users.add(user.get("id"))

    return fan_code_users


def get_users_todos_completed_count(todos_response):
    users_todos_count = defaultdict(dict)
    if todos_response:
        todos_data = todos_response.json()

        for todo in todos_data:
            user_id = todo.get("userId")

            user_todos_count = users_todos_count.get(user_id, {"completed": 0, "non_completed": 0})
            completed = todo.get("completed")

            if completed:
                user_todos_count["completed"] += 1
            else:
                user_todos_count["non_completed"] += 1

            users_todos_count[user_id] = user_todos_count

    # print(users_todos_count)
    return users_todos_count


def test_verify_todo_api():
    test = create_test("Verify Todo Response and Status Code")
    status_code = get_status_code("/todos")
    users_response = get_response_body("/users")
    todos_response = get_response_body("/todos")
    fan_code_users = get_fan_code_users(users_response)
    users_todos_count = get_users_todos_completed_count(todos_response)
    users = list(users_todos_count.keys())

    for userId in fan_code_users:
        user_todos_count = users_todos_count.get(userId)
        if user_todos_count:
            completed = user_todos_count.get("completed")
            non_completed = user_todos_count.get("non_completed")
            print(completed, non_completed)
            assert completed >= non_completed
