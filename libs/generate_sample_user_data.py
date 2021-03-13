import json
import datetime


def generate_sample_user_data():
    """
    must create user_data.json prior run
    :return: write sample user_data in user_data.json
    """
    try:
        with open('../user_data.json', 'r') as f:
            user_data = json.load(f)

        largest_id = 0
        upcoming = {"Overdue": []}
        for i in range(0, 8):
            curr_date = (datetime.date.today() + datetime.timedelta(
                days=i)).strftime("%Y-%m-%d")
            upcoming[curr_date] = []

            for j in range(3):
                upcoming[curr_date].append({
                    "id": largest_id,
                    "subject": f"cs230 hw{largest_id + 1}",
                    "time": "23:59",
                    "priority": "none",
                })

                largest_id += 1

        user_data["theme"] = "todolst"
        user_data["largest_id"] = largest_id
        user_data["upcoming"] = upcoming
        user_data["completed"] = []

        with open('../user_data.json', 'w') as f:
            json.dump(user_data, f)

    except Exception as e:
        print(e)


generate_sample_user_data()
