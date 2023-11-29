## Bryan Xaysanavongphet 11/24/23
## Replaces the GDPR section within a URL

#main function to replace the GDPR
def replace_placeholders(url, dynamic_number):
  # Replace placeholders in the URL
  replaced_url = url.replace("${GDPR}", "#{request.keyValue('_fw_gdpr')}") \
                     .replace("${GDPR_CONSENT_" + str(dynamic_number) + "}", "#{request.keyValue('_fw_gdpr_consent')}")
  return replaced_url

#Main function
def main():
  
  #Assigning a default value to the GDPR Consent number
  dynamic_number = 0
  
  #Giving the user some options to select from. ("Will update these over time")
  print("Please select the GDPR CONSENT number")
  print("1. Doubleclick: '755'")
  print("2. Volkswagen: '68'")
  print("3. 'Other': Please enter the value")
  userInput = input()
  
  #If statement for the menu options
  if userInput == 1:
    dynamic_number = 755
  elif userInput == 2:
    dynamic_number = 68
  elif userInput == 3:
    print("Please enter the value")
    dynamic_number = input()
  
  #Counter for the URLS
  counter = 0
  
  #While loop to keep asking for the urls
  while True:
    #counter to keep track of how many URLs until the loop has ended
    counter+=1
    # Get URL input from the user
    print (f"\nThis is URL #{counter} ")
    user_input = input("Enter a URL (type 'end' to exit): \n")

    # Check if the user wants to end the program
    if user_input.lower() == 'end':
      break
  
    # Replace placeholders and display the result
    result_url = replace_placeholders(user_input, dynamic_number)
    print("\nThe new modified URL is:\n", result_url)
    print("-----------------------------------------------------------------")


if __name__ == "__main__":
  main()
