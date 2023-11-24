#main function to replace the GDPR
def replace_placeholders(url):
  # Replace placeholders in the URL
  replaced_url = url.replace("${GDPR}", "#{request.keyValue('_fw_gdpr')}") \
                     .replace("${GDPR_CONSENT_68}", "#{request.keyValue('_fw_gdpr_consent')}")
  return replaced_url


def main():
  while True:
    # Get URL input from the user
    user_input = input("/nEnter a URL (type 'end' to exit): ")

    # Check if the user wants to end the program
    if user_input.lower() == 'end':
      break

    # Replace placeholders and display the result
    result_url = replace_placeholders(user_input)
    print("\nModified URL:", result_url)
    print()

#calling main
if __name__ == "__main__":
  main()
