#Snake_case
finished_tasks = 12
hours_spent = 1.5
course_name = "Python"
time_per_one_task = hours_spent/finished_tasks
print(time_per_one_task)
#or
#СamelCase
FinishedTasks = 12
HoursSpent = 1.5
CourseName = "Python"
TimePerOneTask = HoursSpent/FinishedTasks
print(TimePerOneTask)

print("Курс:", course_name + ", всего задач:", finished_tasks, ", затрачено часов:", hours_spent,", среднее время выполнения:", time_per_one_task, "часа.")
#f-строка
print(f"Курс: {course_name}, всего задач: {finished_tasks}, затрачено часов: {hours_spent}, среднее время выполнения: {time_per_one_task} часа.")
#f-строка с абзацем
print(f"Курс: {course_name}, всего задач: "
      f"{finished_tasks}, затрачено часов: {hours_spent}, "
      f"среднее время выполнения: {time_per_one_task} часа.")

