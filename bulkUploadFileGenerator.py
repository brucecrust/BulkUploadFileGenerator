# Import the library 'xlsxwriter' for creating Excel files.
import xlsxwriter

# Import the library 'tkinter' for the GUI.
import tkinter as tk
import tkinter.font as tkFont

# Import the function 'random.randint' for randomized phone numbers.
from random import randint

# Import the functions 'os.remove' and 'os.path' for the removal and replacement of old Excel files. 
from os import remove, path

# Import UI creation functions.
import UI

# Import random person generator
from mimesis import Person

class GenerateBulkUploadFiles(object):
	"""
	This class creates an Excel file with n number of patients
	for the purpose of bulk patient uploads.
	"""
	def __init__(self):
		"""
		Creates base variables for the tkinter UI, generated patient details,
		initial variables later changed with user input, counts for incrementing patient names and emails, and UI message handling.
		
		"""
		
		self.person = Person("en")

		# Lists used to store generated user information. 
		self.emailArray = []
		self.nameArray = []
		self.phoneArray = []
		
		# Base phone number string which is used for randomized patient phone numbers.
		self.localPhoneNumber = "5550"
		
		# Initial variables that are later changed with user input.
		self.fileName = None
		self.patientName = None
		self.email = None
		
		# Defines the created submit button.
		self.submitButton = None
		
		# Stores output GUI label messages.
		self.submissionMessagesArray = []
		
		# Used to determine what row a GUI label message should be placed in.
		self.submitMessageRow = 0
		
		# Used to increment patient names and email addresses.
		self.nameCount = 1
		self.emailCount = 1
		
	def handleSubmit(self, fileName, patientName, patientAmount):
		"""
		Creates calls for assigning user input to variables, storing generated patient data in lists, and basic input handling. Parameters passed to this method are then passed to other appropriate methods.
		
		Args:
			fileName (str): The name of the resulting output Excel file.
			patientName (str): The patient name to be incremented.
			emailPrefix (str): The first portion of an email address, before the @ sign, to be incremented.
			emailDomain (str): The last portion of an email address, after the @ sign.
			patientAmount (int): The amount of patients to generate
		"""
		
		# Defines the max amount of messages displayed within the program (a total of 8 messages).
		if self.submitMessageRow >= 5:
			# If the list is larger than 8 messages, the labels should be removed from the list and destroyed.
			for m in self.submissionMessagesArray:
				m.destroy()
			self.submissionMessagesArray = []
			
			# Reset the position of output messages.
			self.submitMessageRow = 0
			
		# Set user input values to variables.	
		self.setInitValues(fileName, patientName, patientAmount)
		
		# Check if user input is valid; if not, an output error message is thrown in the UI.
		self.validateInput()	
			
		# Last check of user input. If this fails, no file is created.	
		if (
		self.fileName != "" and isinstance(self.patientAmount, int)
		):
			# Delete identical worksheets and reset lists/increment amounts.
			self.deleteWorkSheet()
			
			# Store generated patient information in lists.
			self.appendArrays()
			
			# Generate the Excel file.
			self.createWorkSheet()
			
			# Output message indicating that the file was created successfully.
			message = UI.createLabel(root, f"The worksheet file {self.fileName} has been created and {str(self.patientAmount)} patient(s) have been added.", self.submitMessageRow, 2, customFont)
			self.submissionMessagesArray.append(message)
			self.submitMessageRow += 1
			
	def validateInput(self):
		"""
		Validates user input, and displays UI labels if an error occurs.
		"""
		
		# The following 'if' statements throw a UI error output message if user input is not valid.
		if self.fileName == "":
			message = UI.createLabel(root, "Please enter a file name.", self.submitMessageRow, 2, customFont, "red")
			self.submissionMessagesArray.append(message)
			self.submitMessageRow += 1

		if self.patientName == "":
			self.patientName = "Test"
		
		try: 
			self.patientAmount = int(self.patientAmount)
		except:
			message = UI.createLabel(root, "Please enter an integer value for the Patient Amount field.", self.submitMessageRow, 2, customFont, "red")
			self.submissionMessagesArray.append(message)
			self.submitMessageRow += 1
	
	def generatePhoneNumbers(self):
		"""
		Generates randomized, fictitious phone numbers for patients. 
		"""
		# Generate a random phone numbers using the initial '555-0' number.
		initialPhoneNumber = str(randint(100,999)) + self.localPhoneNumber + str(randint(100,999))
		
		# Cast the phone number to an integer.
		phoneNumber = int(initialPhoneNumber)
		return phoneNumber

	def setInitValues(self, fileName, patientName, patientAmount):
		"""
		Assigns user input to variables for later use.
		
		Args:
			fileName (str): The name of the resulting output Excel file.
			patientName (str): The patient name to be incremented.
			emailPrefix (str): The first portion of an email address, before the @ sign, to be incremented.
			emailDomain (str): The last portion of an email address, after the @ sign.
			patientAmount (int): The amount of patients to generate
		"""
		
		# Assign user input to variables.
		self.fileName = fileName.get()
		self.patientName = patientName.get()
		self.patientAmount = patientAmount.get()

	def deleteWorkSheet(self):
		"""
		'Resets' patient data lists, increment counts, and removes identical Excel files.
		"""
		
		# Reset patient data lists.
		self.emailArray = []
		self.nameArray = []
		self.phoneArray = []
		
		# Reset increment counts.
		self.nameCount = 1
		self.emailCount = 1
		
		# Delete identical Excel file.
		if path.isfile(self.fileName + '.xlsx'):
			remove(self.fileName + '.xlsx')
		
	def createWorkSheet(self):
		"""
		Creates the Excel file with appropriate column headers and generated patient information.
		"""
		
		self.initFileName = self.fileName
		
		# Create the generated bulk upload Excel file.
		workbook = xlsxwriter.Workbook(self.fileName + '.xlsx')
		worksheet = workbook.add_worksheet()
		
		col = 0
		row = 1
		
		# Create Excel columns for patient information.
		worksheet.write(0, 0, 'Full Name')
		worksheet.write(0, 1, 'Email')
		worksheet.write(0, 2, 'Phone')
		worksheet.write(0, 3, 'DOB')
		worksheet.write(0, 4, 'Gender')
		worksheet.write(0, 5, 'BMI')
			
			
		# Extract generated patient information from lists, and write them tol the Excel file.
		for n in self.nameArray:
			worksheet.write(row, col, n)
			row += 1
		
		col = 1
		row = 1
		
		for e in self.emailArray:
			worksheet.write(row, col, e)
			row += 1
			
		col = 2
		row = 1
			
		for p in self.phoneArray:
			worksheet.write(row, col, p)
			row += 1
			
		# Close the Excel file.	
		workbook.close()
		
	def appendArrays(self):
		"""
		Adds patient information to lists, and increments patient names and email addresses.
		"""
		
		# Generate incremented patient information, and append the data to the appropriate lists.
		for x in range(int(self.patientAmount)):
			generatedName = self.person.full_name()
			name = f"{self.patientName}-{generatedName}"
			self.nameArray.append(name)
			
		for x in range(int(self.patientAmount)):
			generatedEmail = self.person.email()
			email = f"{self.patientName}-{generatedEmail}"
			self.emailArray.append(email)
		
		for x in range(int(self.patientAmount)):
			endPhoneNumber = self.generatePhoneNumbers()
			# Translate phone numbers into a standard phone number format.
			endPhoneNumber = format(int(str(endPhoneNumber)[:-1]), ",").replace(",", "-") + str(endPhoneNumber)[-1] 
			
			# Check if the phone number already exists in the array.
			while endPhoneNumber in self.phoneArray:
				endPhoneNumber = self.generatePhoneNumbers()
				endPhoneNumber = format(int(str(endPhoneNumber)[:-1]), ",").replace(",", "-") + str(endPhoneNumber)[-1]
			else:
				self.phoneArray.append(endPhoneNumber)				
		
	def createGUI(self):
		"""
		Creates the tkinter GUI and starts the mainloop.
		"""

		# Set initial GUI resolution and title.
		root.geometry("700x150")
		root.title("Bulk Upload File Generator")
		
		# Create input field labels.
		UI.createLabel(root, "* File name", 0, 0, customFont)
		fileName = UI.createEntry(root, 0, 1)
		
		UI.createLabel(root, "Patient prefix", 1, 0, customFont)
		patientName = UI.createEntry(root, 1, 1)

		UI.createLabel(root, "* Number of patients", 2, 0, customFont)
		patientAmount = UI.createEntry(root, 2, 1)
		
		# Create button for input submission.
		self.submitButton = UI.createButton(root, "Submit", lambda: self.handleSubmit(fileName, patientName, patientAmount), 3, 0)
		
		
# Instantiate GenerateBulkUpload class with a custom font. 		
root = tk.Tk()
customFont = tkFont.Font(family="Helvetica", size=10)
bufg = GenerateBulkUploadFiles()
bufg.createGUI()
root.resizable(False, False)
root.mainloop()