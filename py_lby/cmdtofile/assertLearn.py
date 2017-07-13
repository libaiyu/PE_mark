#! python 3

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither lihght is red! ' + str(stoplight)

market_2nd = {'ns':'green','ew':'red'}
mission_16th = {'ns':'red','ew':'green'}

switchLights(mission_16th)
switchLights(market_2nd)