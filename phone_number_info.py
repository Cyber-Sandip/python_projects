# first dawnload phonenumber-------> pip install phonenumbers
import phonenumbers
from phonenumbers import carrier, geocoder 
import pyfiglet


print("-------------------------------------------------------------------------------------------------")
print(pyfiglet.figlet_format("phone  info\n\n",justify="center",font=""))
print(pyfiglet.figlet_format("by cyber-sandip\n\n",justify="center",font=""))
print("-------------------------------------------------------------------------------------------------")
country_code="+ "+input("Enter country code without "+" : " )
mobile_number = country_code + input("enter your mobile number : ") 
parsed_number = phonenumbers.parse(mobile_number)
carrier_name = carrier.name_for_number(parsed_number, "en")
geolocation = geocoder.description_for_number(parsed_number, "en")

# Print the information
print(f"Mobile Number: {mobile_number}")
print(f"Carrier Name: {carrier_name}")
print(f"Geolocation: {geolocation}")