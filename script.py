Practice Notebook - Putting It All Together
Hello, coders! Below we have code similar to what we wrote in the last video. Go ahead and run the following cell that defines our get_event_date, current_users and generate_report methods.

def get_event_date(event):
  return event.date
​
def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout"and len(machines[event.machine]) > 0:
      machines[event.machine].remove(event.user)
  return machines
​
def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))
class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
Ok, we have an Event class that has a constructor and sets the necessary attributes. Next let's create some events and add them to a list by running the following cell.

Now we've got a bunch of events. Let's feed these events into our custom_users function and see what happens.

users = current_users(events)
print(users)
{'webserver.local': {'lane'}, 'myworkstation.local': set(), 'mailserver.local': set()}
No output should be generated from running the custom function definitions above. To check that our code is doing everything it's supposed to do, we need an Event class. The code in the next cell below initializes our Event class. Go ahead and run this cell next.


generate_report(users)
webserver.local: lane
