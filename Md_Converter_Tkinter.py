# Function -> md file to Pdf file Converter.
# Button  -> Converter
# Input -> Address
# Label -> Message after Completion or Error Msg
# Automate the Program using the Short-Cut
# Here TK_SILENCE_DEPRECATION = 1 so that the depricated versions can also work with.
import markdown_it
import pdfkit 
import os
from os import path
os.environ['TK_SILENCE_DEPRECATION'] = '1'
from tkinter import *
from PIL import Image,ImageTk

# Declaring the Color Schema of the GUI. 
background_color = "#1C2833"
foreground_color = "#EBF5FB"
btn_foreground_color = "#28B463"

# Function to convert the MD File & it's Content into HTML Format.
def mdToHtml(folderAddress,filename,mdFile):
   # Object of markdown_it class.
   md = markdown_it.MarkdownIt()
   # Rendering and Extracting the Content.
   html_content = md.render(mdFile.read())
   # Importing Custom Css file which includes basic styling of the HTML (and Pdf aslo).
   cssFile = open("/Users/abhishekjhawar/Desktop/Project/Winter_Vacation/MD_CONVERTER/Styles.css", 'r') 
   # Extracting the Css content from the File.
   cssContent = cssFile.read()
   # Adding the Content inside a <style> tag and add that to the HTML file.
   Html_content= f"<html><head><style>{cssContent}</style></head><body>{html_content}</body></html>"
   Htmlfile = open(folderAddress + "/" + filename + ".html", "w+")
   # Making a HTML file for the Resp md file and write all the content.
   Htmlfile.write(Html_content)
   Htmlfile.close()
   return

# Main Function OR Core Functionality of the Application.
def mdToPdf(folderAddress,filename):
   # Checking if the HTMl file Exists or Not.
   # If the File doesn't Exists then CALL mdToHtml(parameters) function.
   if path.exists(folderAddress + "/" + filename + ".html") == False:
      address = folderAddress + "/" + filename + ".md"
      mdFile = open(address, "r")
      mdToHtml(folderAddress,filename,mdFile)
   else:
   # Configuring the pdf structure and pdf_converter module.
      pass
   config = pdfkit.configuration(wkhtmltopdf ="/usr/local/bin/wkhtmltopdf")
   options = {
      'enable-local-file-access': True,
      'encoding': 'UTF-8'
    }
   try:
      pdfkit.from_file(
         folderAddress + "/" + filename + ".html",
         folderAddress + "/" + filename + ".pdf",
         configuration = config,
         options = options
      )
   # If Pdf is not converted or due to address problem.
   except Exception as e:
      print("Error Encountered : ", str(e))
      
   # Removing the HTML file After the Pdf generation.
   Htmladdress = folderAddress + "/" + filename + ".html"
   os.remove(Htmladdress)
   return

# Function is all about Framing the Extracted File Address and the Call the Core Functionality of the Application with proper file-address or parameters.
def FileAddress(file_address):
   folderAddress, full_filename = os.path.split(file_address)
   filename, _ = os.path.splitext(full_filename)
   mdToPdf(folderAddress,filename)

# Interface OR GUI : Creating the Window for the application
def Tkinter_Application():
   window = Tk()
   window.geometry("750x350")
   window.title("Md_Converter")
   window.resizable(False, False)
   window['bg'] = background_color
   window['pady'] = 65
   window['padx'] = 25
   create_input_frame(window)
   window.mainloop()

# Function Switches the Window from one activity to another activity.
# Here FileAddress() Function is Which is Extracted the File-Address.
def switch_frame(window,file_path):
    FileAddress(file_path)
    input_frame.destroy()
    create_converted_frame(window)  

# Creating or Crafting First Activity of Inputting the Md File Address and a button to Convert/call mdToPdf()
def create_input_frame(window):
    global input_frame
    input_frame = Frame(window, bg = background_color)
    input_frame.pack(fill='both', expand = False)
    Fileaddress = StringVar()
   #  Label for File Address Input
    label = Label(input_frame, text="Enter the Md File Address : ", foreground = foreground_color, background = background_color, font = ("Arial", 20), pady = 20)
    label.pack()
   # File Input
    File_Address = Entry(input_frame, background = "#F7F9F9", fg = "#922B21", font = ('Arial', 17, 'normal'), textvariable = Fileaddress, width = 35, show = "*")
    File_Address.pack()
   #  Button to call the File address extraction and then call mdToPdf() function.
    converter_button = Button(input_frame, text = "Convert", width = 12,activeforeground = btn_foreground_color, foreground = btn_foreground_color, font = ('Arial', 18, 'italic'), command = lambda : switch_frame(window,File_Address.get()))
    converter_button.pack(pady = (20, 20),padx = (20,20))
 
# Successful Converting Last Frame 
# After converting the md file into pdf then this frame will pop-up.  
def create_converted_frame(window):
    converted_frame = Frame(window, bg = background_color)
    converted_frame.pack(fill = 'both', expand = False)
    Label(converted_frame, text = " The File is Converted into PDF Format  ! ", foreground = foreground_color, background = background_color, font = ("Arial", 20,"bold")).pack(pady = 40)

if __name__ == '__main__':
   Tkinter_Application()


