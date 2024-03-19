car_info = {
    'distance': 100,
    'speed': 40,
    'time': 20

}


def route_info(**a):
    if (a.get('distance')) and (type(a.get('distance')) is int):
        return f"Distance is = {a['distance']}"

    if (a.get('distance')) and (type(a.get('distance')) is float):
        return f"Distance is ={a['distance']}"

    if (a.get('speed')) and (a.get('time')):
        return f"Distance is speed * time = {a['speed'] * a['time']}"

    return f"No distance info is avaibale"


print(route_info(**car_info))
