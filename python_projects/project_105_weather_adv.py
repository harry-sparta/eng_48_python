# Make a weather/clothing game
# Ask for user input and depending on the response advise on their attire.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
    ## - when sunny >> respond with 'take your shorts!'
    ## - stormy >> respond with 'take rain coat'
    ## - rainy >> respond with 'Take your umbrella'
    ## - rainy and stormy >> 'stay home'
    ## - anything else respond with 'sorry, i didn't quite catch that'

# Game codes-------------------------------------------------------------------------------------
weather = {'sunny': 'take your shorts!',
            'stormy': 'take rain coat!',
            'rainy': 'take your umbrella!',
            'rainy&stormy': 'stay home!'}

current_weather = input('enter weather condition (sunny, stormy, rainy, rainy&stormy):    ')
current_weather_format = current_weather.strip().lower()

while current_weather_format not in weather:
    print('sorry I didn\'t quite catch that. Try again.')
    current_weather = input('enter weather condition (sunny, stormy, rainy, rainy&stormy):    ')
    current_weather_format = current_weather.strip().lower()
print(weather[current_weather_format])

