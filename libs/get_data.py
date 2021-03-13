import json
import datetime


# date = '%Y-%m-%d'
# data_time = '%Y-%m-%d %H:%M'


def theme_setting(theme_name):
    """
    :param theme_name: name of the theme - todolst, dark
    :return: color palate for the theme
    """
    if theme_name == 'todolst':
        return {
            "primary_color": [103 / 255, 58 / 255, 183 / 255, 1],
            "primary_variant_color": [50 / 255, 11 / 255, 134 / 255, 1],
            "secondary_color": [255 / 255, 191 / 255, 0, 1],
            "text_color": [0, 0, 0, 1],
            "background_color": [1, 1, 1, 1],
            "good_color": [67 / 255, 160 / 255, 71 / 255, 1],
            "bad_color": [229 / 255, 57 / 255, 53 / 255, 1]
        }
    elif theme_name == 'dark':
        return {
            "primary_color": [103 / 255, 58 / 255, 183 / 255, 1],
            "primary_variant_color": [50 / 255, 11 / 255, 134 / 255, 1],
            "secondary_color": [255 / 255, 191 / 255, 0, 1],
            "text_color": [0, 0, 0, 1],
            "background_color": [1, 1, 1, 1],
            "good_color": [67 / 255, 160 / 255, 71 / 255, 1],
            "bad_color": [229 / 255, 57 / 255, 53 / 255, 1]
        }
    else:
        raise ValueError


def add_item_to_dict(dict_obj, key, value):
    """
    add an item to a list inside a dict or create a list contain this item in
    the dict
    :param dict_obj: dictionary will hold this list
    :param key: key for the list
    :param value: value of the item
    :return: add list of item to the dict
    """
    if key not in dict_obj.keys():
        if type(value) == list:
            dict_obj[key] = value
        else:
            dict_obj[key] = [value]

    elif type(dict_obj[key]) == list:
        if type(value) == list:
            for item in value:
                dict_obj[key].append(item)
        else:
            dict_obj[key].append(value)


def get_upcoming_tasks():
    """
    :return: upcoming tasks separate in overdue or on_time dict
    """
    try:
        with open('../user_data.json', 'r') as f:
            data = json.load(f)

        upcoming_data = data['upcoming']
        upcoming_tasks = {'overdue': {}, 'on_time': {}}
        curr_date = datetime.date.today()

        for date in upcoming_data:
            # put all existed overdue tasks to new overdue
            if date == 'overdue':
                for overdue_date in upcoming_data['overdue']:
                    overdue_date_obj = datetime.datetime. \
                        strptime(overdue_date, "%Y-%m-%d").date()
                    upcoming_tasks['overdue'][overdue_date_obj] = \
                        upcoming_data['overdue'][overdue_date]

            # check if task can go to overdue or on_time
            else:
                due_date_obj = datetime.datetime. \
                    strptime(date, "%Y-%m-%d").date()

                # all tasks with date prior than today will go in overdue
                if due_date_obj < curr_date:
                    add_item_to_dict(upcoming_tasks['overdue'], due_date_obj,
                                     upcoming_data[date])

                # if task with today date then check time
                elif due_date_obj == curr_date:
                    curr_time = datetime.datetime.now().time()

                    # all tasks with pasted time will go in overdue
                    for task in upcoming_data[date]:
                        task_due_time = datetime.datetime.strptime(
                            task['time'], '%H:%M').time()

                        if task_due_time > curr_time:
                            break
                        else:
                            add_item_to_dict(upcoming_tasks['overdue'],
                                             curr_date, task)

                # all task that not filter in overdue can go in on_time
                else:
                    upcoming_tasks['on_time'][due_date_obj] = \
                        upcoming_data[date]

        # print(upcoming_tasks)
        return upcoming_tasks

    except Exception as e:
        print(e)


# def get_next7days_tasks(upcoming_on_time_tasks):
#     """
#     :return:
#     """
#     next7days = [date for date in
#                  [datetime.date.today() + datetime.timedelta(days=i) for i in
#                   range(8)]]
#
#     print(next7days)
#
#
# get_next7days_tasks()


def get_completed_tasks():
    try:
        with open('../user_data.json', 'r') as f:
            data = json.load(f)

        completed_tasks = data['completed']
        curr_datetime = datetime.datetime.now()
        period_24h = datetime.timedelta(days=1)

        # remove task completed more than 24 hours
        for task, index in zip(completed_tasks, range(len(completed_tasks))):
            completed_time_obj = datetime.datetime.strptime(
                task['completed_time'], '%Y-%m-%d %H:%M')

            if (curr_datetime - completed_time_obj) > period_24h:
                del completed_tasks[index]
            else:
                task['completed_time'] = completed_time_obj

        # print(completed_tasks)
        return completed_tasks

    except Exception as e:
        print(e)


get_completed_tasks()
