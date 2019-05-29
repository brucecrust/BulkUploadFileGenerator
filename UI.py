import os

import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import *

def createLabel(tkGUI, label, itemRow, itemColumn, customFont, foregroundColor="black"):
    """
    Creates and returns labels for use in the GUI.
    
    Args:
        tkGUI (class): The tkinter class for use in creating the GUI.
        label (str): The text content of the label.
        itemRow (int): The grid row where the label should be placed.
        itemColumn (int): The grid column where the label should be placed.
        customFont1 (class): The font of the label.
        foregroundColor (str): The color of the font.
    """
    
    # Create and return label.
    label = tk.Label(tkGUI, text=label, fg=foregroundColor, font=customFont)
    label.grid(row=itemRow, column=itemColumn, sticky="w")
    return label
    
def createEntry(tkGUI, itemRow, itemColumn, textVariable=None, isPassword=False):
    """
    Creates and returns a field for user input.
    
    Args:
        tkGUI (class): The tkinter class for use in creating the GUI.
        itemRow (int): The grid row where the label should be placed.
        itemColumn (int): The grid column where the label should be placed.
    """
    
    # Create and return user input entry field.
    if isPassword:
        entry = tk.Entry(tkGUI, show="*")
    else:
        entry = tk.Entry(tkGUI, textvariable=textVariable)
    entry.grid(row=itemRow, column=itemColumn)
    return entry
    
def createButton(tkGUI, textItem, commandFunction, itemRow, itemColumn, dirSticky=None, font=None):
    """
    Creates and returns a button for use in the GUI.
    
    Args: 
        tkGUI (class): The tkinter class for use in creating the GUI.
        textItem (str): The text content of the button.
        commandFunction (function): The function that used when the user selects the button.
        itemRow (int): The grid row where the label should be placed.
        itemColumn (int): The grid column where the label should be placed.
    """
    
    # Create and return button.
    button = tk.Button(tkGUI, text=textItem, command=commandFunction, font=tkFont.Font(family="Helvetica", size=10, weight="bold", font=font))
    button.grid(row=itemRow, column=itemColumn, sticky=dirSticky)
    return button

def createRadioButton(tkGUI, textItem, itemVariable, itemRow, itemColumn, itemValue):
    """
    Creates and returns a button for use in the GUI.

    Args: 
        tkGUI (class): The tkinter class for use in creating the GUI.
        textItem (str): The text content of the button.
        itemVariable (IntVar): The associated variable used for tracking the state of the radio buttons.
        itemRow (int): The grid row where the label should be placed.
        itemColumn (int): The grid column where the label should be placed.
        itemValue (int): The value of the radio button in correlation with the itemVariable.
    """
    radioButton = tk.Radiobutton(tkGUI, text=textItem, variable=itemVariable, value=itemValue)
    radioButton.grid(row=itemRow, column=itemColumn)
    return radioButton

def createSeparator(tkGUI, dirSticky, itemRow, itemColumn):
    separator = Separator(tkGUI,orient=HORIZONTAL).grid(row=itemRow, columnspan=itemColumn, sticky=dirSticky)
    return separator

def createLabelFrame(tkGUI, textItem, dirSticky, itemRow, itemColumn, itemColumnSpan, padX, padY, iPadX, iPadY):
    labelFrame = tk.LabelFrame(tkGUI, text=textItem)
    labelFrame.grid(row=itemRow, column=itemColumn, columnspan=itemColumnSpan, stick=dirSticky,
        padx=padX, pady=padY, ipadx=iPadX, ipady=iPadY
    )
    return labelFrame

def createCheckBox(tkGUI, textItem, itemRow, itemColumn, invokeFunction, itemVariable):
    checkbox = tk.Checkbutton(tkGUI, text=textItem, command=invokeFunction, variable=itemVariable)
    checkbox.grid(row=itemRow, column=itemColumn)
    return checkbox

def createListBox(tkGUI, itemRow, itemColumn, optionsList, height):
    listBox = tk.Listbox(tkGUI, height=height)
    listBox.delete(0, "end")
    for i in optionsList:
        listBox.insert("end", i)
    listBox.grid(row=itemRow, column=itemColumn)
    return listBox

def createDropdown(tkGUI, itemVariable, optionsList, itemRow, itemColumn):
    dropdown = tk.OptionMenu(tkGUI, itemVariable, *optionsList)
    dropdown.grid(row=itemRow, column=itemColumn)
    return dropdown

def onKeyRelease(event, dropdownList, dropdown):
    value = event.widget.get()
    value = value.strip().lower()
    if value == "":
        data = dropdownList
    else:
        data = []
        for i in dropdownList:
            if i is not None:
                if value in i.lower():
                    data.append(i)
        
    self.dropdownUpdate(data, dropdown)

def dropdownUpdate(data, dropdown):
    dropdown.delete(0, "end")
    data = sorted(data, key=str.lower)
    for i in data:
        dropdown.insert("end", i)

    dropdown.select_set(0)
    dropdown.event_generate("<<ListboxSelect>>")