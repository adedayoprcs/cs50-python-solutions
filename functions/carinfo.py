def make_car(manufactural, model,):
    tow_package = {}
    tow_package['manufactural_name'] = manufactural
    tow_package['model_name'] = model
    return tow_package

car = make_car('subaru', 'outback')
print(car)
