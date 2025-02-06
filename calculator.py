# Import OS module to execute shell commands
import os
# Install and import tkinter as a module
print("Checking if tkinter is installed......")
try:
   from tkinter import *
   print("tkinter is already installed, opening window......")
except:
      print("Installing tkinter......")
      # windows
      os.system("pip install tkinter")
      # *Nix
      os.system("pip3 install tkinter")
      os.system("pip3 install tkinter --break-system-packages")
      os.system("sudo apt-get install python3-tk")
      os.system("cls")
      os.system("clear")
      print("tkinter has been installed, please relaunch the program")
      quit()
# Main code
# Create frame for holding buttons
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="teal")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj
# Create buttons
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj
# Create the main window and set the title to "Calculator"
class app(Frame):
      def calc(self, display):
              try:
                 display.set(eval(display.get()))
              except:
                    display.set("ERROR")

      def __init__(self):
          Frame.__init__(self)
          self.option_add('*Font', 'arial 20 bold')
          self.pack(expand=YES, fill=BOTH)
          self.master.title('Calculator')
          # Create a special variable to display numbers in the entry widget
          display = StringVar()
          # Set up the entry widget, which displays the numbers
          Entry(self, relief=RIDGE, textvariable=display,
justify='right', bd=30, bg="blue").pack(side=TOP, expand=YES, fill=BOTH)
          # Create the "Clear" ("C") button
          for clearButton in (["C"]):
              erase = iCalc(self, TOP)
              for ichar in clearButton:
                  button(erase, LEFT, ichar, lambda
storeObj=display, q=ichar: storeObj.set(''))

          for numButton in ("789/", "456*", "123-", "0.+"):
              FunctionNum = iCalc(self, TOP)
              for iEquals in numButton:
                  button(FunctionNum, LEFT, iEquals, lambda
                  storeObj=display, q=iEquals: storeObj
                  .set(storeObj.get() + q))
          EqualButton = iCalc(self, TOP)
          for iEquals in "=":
              if iEquals == '=':
                 btniEquals = button(EqualButton, LEFT, iEquals)
                 btniEquals.bind('<ButtonRelease-1>', lambda e, s=self,
                 storeObj=display: s.calc(storeObj), '+')
              else:
                  btniEquals = button(EqualButton, LEFT, iEquals,
                  lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                  (storeObj.get() + s))

         

# Main program execution
if __name__ == '__main__':
   app().mainloop()
