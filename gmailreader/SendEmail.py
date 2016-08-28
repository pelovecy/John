from temboo.Library.Google.Gmail import SendEmail
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("accountName", "myFirstApp", "abc123xxxxxxxxxxxxxx")

# Instantiate the Choreo
sendEmailChoreo = SendEmail(session)

# Get an InputSet object for the Choreo
sendEmailInputs = sendEmailChoreo.new_input_set()

# Set the Choreo inputs
sendEmailInputs.set_FromAddress("yourValueHere")
sendEmailInputs.set_Username("yourValueHere")
sendEmailInputs.set_Subject("yourValueHere")
sendEmailInputs.set_ToAddress("yourValueHere")
sendEmailInputs.set_MessageBody("yourValueHere")
sendEmailInputs.set_Password("yourValueHere")

# Execute the Choreo
sendEmailResults = sendEmailChoreo.execute_with_results(sendEmailInputs)

# Print the Choreo outputs
print("Success: " + sendEmailResults.get_Success())