# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.popup import Popup
#
# # Lists of arrays of dictionaries that contain task entries.
# remaining_tasks = []
#
# # Default largest id for remaining_tasks.
# largest_id = 0
#
#
# def add_task_to_json(self):
#     global largest_id
#
#     try:
#         new_task = create_task(self)
#     except PostError as e:
#         error_text = str(e)
#
#         content = BoxLayout(orientation='vertical')
#         message_label = Label(text=error_text)
#         dismiss_button = Button(text='OK')
#
#         content.add_widget(message_label)
#         content.add_widget(dismiss_button)
#
#         popup = Popup(title='Error', content=content,
#                       size_hint=(0.5, 0.25))
#         dismiss_button.bind(on_press=popup.dismiss)
#         popup.open()
#     else:
#         remaining_tasks.append(new_task)
#         largest_id += 1
#
#         update_remaining_tasks(self)
#
#
# def update_remaining_tasks(self):
#     """
#     Updates the view_of_remaining_tasks Label on WindowOne to show
#     any new tasks that the user added. This function is called as the
#     user transitions from WindowTwo to WindowOne, so view_of_remaining_tasks
#     will be updated when the user goes back to WindowOne.
#
#     :param self: screens_setup.WindowTwo.update_tasks
#     :return: None
#     """
#
#     window_1_access = self.manager.get_screen('window_one')
#
#     window_1_access.ids.view_of_remaining_tasks.text = ""
#     screen1_text = ""
#
#     for index in range(len(remaining_tasks)):
#         screen1_text += 'Task: ' + remaining_tasks[index]['body'] + '\n'
#         screen1_text += 'Time: ' + remaining_tasks[index]['time'] + '\n'
#
#         if remaining_tasks[index]['priority']:
#             screen1_text += 'Priority level is: HIGH' + '\n' + '\n'
#         else:
#             screen1_text += 'Priority level is: LOW' + '\n' + '\n'
#
#     window_1_access.ids.view_of_remaining_tasks.text = screen1_text
