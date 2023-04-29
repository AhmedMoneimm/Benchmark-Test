import csv
from datetime import datetime
from pywinauto.application import Application

app_info = {
    1: {'name': 'Notepad', 'path': 'notepad.exe'},
    2: {'name': 'Calculator', 'path': 'calc.exe'},
    3: {'name': 'Paint', 'path': 'mspaint.exe'},
    4: {'name': 'Snipping Tool', 'path': 'SnippingTool.exe'},
    5: {'name': 'File Explorer', 'path': 'explorer.exe'}
}

app_names = [(app_num, app_data['name']) for app_num, app_data in app_info.items()]

app_data_dict = {app_num: {'name': app_data['name'], 'path': app_data['path'], 'times': []} for app_num, app_data in app_info.items()}

for i in range(10):
    print(f"Iteration {i+1}:")
    for app_num, app_data in app_info.items():
        start_time = datetime.now()

        app = Application().start(app_data['path'])

        app.kill()

        end_time = datetime.now()

        elapsed_time = (end_time - start_time).total_seconds() * 1000
        print(f"{app_data['name']} ({app_data['path']}) took {elapsed_time:.2f} milliseconds to open and close")

        app_data_dict[app_num]['times'].append(elapsed_time)

    print('---------------------------------------------------------------------')

for app_num, app_data in app_data_dict.items():
    times = app_data['times']
    avg_time = sum(times) / len(times)
    app_data['avg_time'] = avg_time

with open('app_times.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['App Number', 'App Name', 'Time 1(ms)', 'Time 2(ms)', 'Time 3(ms)', 'Time 4(ms)', 'Time 5(ms)', 'Time 6(ms)', 'Time 7(ms)', 'Time 8(ms)', 'Time 9(ms)', 'Time 10(ms)', 'Average Time(ms)'])

    
    for app_num, app_name in app_names:
        app_data = app_data_dict[app_num]
        times = app_data['times']
        avg_time = app_data['avg_time']
        row = [app_num, app_name] + times + [avg_time]
        writer.writerow(row)