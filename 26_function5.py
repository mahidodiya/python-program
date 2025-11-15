#create lambda function that return true if city passed as 1st argument exist in list passed argument as 2nd argument, if city does not exist return false
''' 
isCityExist('Bhavnagar',['Bombay','Baroda','rajkot']) # false
isCityExist('rajkot',['Bombay','Baroda','rajkot']) # true 
'''
isCityExist=lambda city,city_list: city in city_list

city=input("Enter city name:")
city_list = input("Enter cities separated by comma: ").split(',')

print(isCityExist(city,city_list))