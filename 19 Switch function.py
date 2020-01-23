#switch python
def get_car_color(car):
    if car == 'ford':
        return ['red', 'black', 'white', 'silver', 'gold']
    elif car == 'audi':
        return ['black', 'white']
    elif car == 'volkswagen':
        return ['purple', 'orange', 'green']
    elif car == 'mercedes':
        return ['black']
    else:
        return ['pink']
print(get_car_color('audi'))