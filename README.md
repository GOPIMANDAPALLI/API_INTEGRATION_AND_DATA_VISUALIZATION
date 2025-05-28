# API_INTEGRATION_AND_DATA_VISUALIZATION

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : MANDAPALLI GOPI

*INTERN ID* : CT04DN1772

*DURATION* : 4-WEEKS

*MENTOR* : NEELA SANTOSH

*DESCRIPTION FOR USING MATPLOTLIB AND USING PUBLIC API LIKE(OPENWEATHERMAP.ORG) FOR THE TASK* :

This project, developed using the PyCharm Integrated Development Environment (IDE), is a beginner-level weather data visualization tool written in Python. The main objective of this project is to allow users to enter the name of a city and receive a visual representation of the current temperature in that city. It serves as an excellent introduction to working with RESTful APIs, handling JSON data, and creating basic data visualizations using Python libraries.

The core functionality of the application relies on the OpenWeatherMap API, which provides access to real-time weather data from across the globe. In this specific implementation, the API endpoint /data/2.5/weather is used. The user inputs the name of a city, and the application constructs a URL with query parameters including the city name, a valid API key, and the unit system (metric). A request is sent to this URL using the requests module, and the response  which is in JSON format is parsed using Python's json module.

From the response, the application extracts two key pieces of information: the current temperature and the timezone offset of the specified city. These values are stored in two separate lists: one for temperature and one for time. The temperature value reflects the real-time temperature in degrees Celsius, while the timezone value represents the city’s offset from Coordinated Universal Time (UTC) in seconds. It is important to note that the timezone value is not a timestamp and therefore should not be used directly as a time axis label on a plot. However, in this basic implementation, it is used as such just to demonstrate the plotting functionality.

To present the weather data visually, the application uses the matplotlib.pyplot library, a widely used plotting tool in Python. A simple line chart is generated using the temperature and time data. The chart includes various stylistic elements to enhance readability and aesthetics, such as custom font settings, a grid, labeled axes, a marker on the data point, and a descriptive title. The use of markers and font customization demonstrates basic styling features in matplotlib. However, the graph's title "24-Hour Temperature Forecast for [City Name]" is misleading because the current API endpoint used only provides a single data point: the current temperature. To accurately plot a 24-hour temperature forecast, a different endpoint such as /data/2.5/forecast, which returns 5-day data in 3-hour intervals, would need to be used.

Despite its limitations, this project is a valuable starting point for students and developers interested in API integration, data extraction, and visual representation of information. It provides hands-on experience with sending HTTP requests, parsing JSON responses, and plotting data. The project also demonstrates how external data sources can be integrated into Python applications to create useful tools.

Overall, the application showcases how real-world data can be transformed into meaningful visual output using Python. Developed entirely in PyCharm, the project also highlights the benefits of using a professional development environment, including better code organization, syntax highlighting, debugging support, and overall improved productivity. With some modifications  particularly by integrating the 5-day/3-hour forecast API  this project can be significantly enhanced to plot detailed, time-based forecasts.



*OUTPUT FOR USING MATPLOTLIB* :
  
  PHOTO-1 :
  ![Image](https://github.com/user-attachments/assets/d6879a77-cc31-41a0-a3f9-ddd7c7a1191d)
  PHOTO-2 :
![Image](https://github.com/user-attachments/assets/dd123076-e638-4152-b9d5-b75d06acc06c)
  PHOTO-3 :
![Image](https://github.com/user-attachments/assets/df9dc1c9-44d7-48b2-b2bf-7f9838843e73)
 
 



*DESCRIPTION FOR WITHOUT USING OPENWEATHERMAP FOR THE TASK* :

This Python program, developed using the Matplotlib library, creates a visual representation of temperature data over a specific time range for a user-specified city. Upon execution, the user is prompted to enter a city name, which is then used in the chart title to personalize the output. The program uses predefined temperature and time values six data points representing hourly temperatures from 6:00 AM to 11:00 AM. These values are stored in two lists: temperature and time. Using the matplotlib.pyplot module, a line graph is plotted with custom markers, colors, and font styles to enhance visual clarity. The graph includes a title, labeled X (Time) and Y (Temperature) axes, and a grid for better readability. Although the program does not fetch real-time data, it effectively demonstrates how to use Matplotlib to plot static data and is useful for learning how to visualize temperature trends in a simple, user-interactive way.


*OUTPUT FOR WITHOUT USING OPENWEATHERMAP * :

  PHOTO-1 :
  ![Image](https://github.com/user-attachments/assets/ff38b49c-25fa-460d-8b06-ae93a63659c5)
  PHOTO-2 :
![Image](https://github.com/user-attachments/assets/28d262c4-11db-43d1-9844-414c0c9f7fe0)






