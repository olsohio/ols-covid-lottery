### General Info
- Confidential Entries Directory
    - Where entry data is stored containing personal information
    
- Confidential Results Directory
    - Where the results file containing containing personal information will populate
    
- Public Results Directory
    - File containing no personal information
    - Contains reference number, slot and group numbers

### Use instructions
- Rename "entries-Template.csv" to "entries.csv" in the Confidential Entries Directory
  - Headers must match exactly
  - Field 1 is the users Entry or "Reference Number"
  - Field 2 is name
  - Field 3 is email (for sending group and slot number)
  - Populate this file with your data!
- Set your Group Size at by changing the "group_size" variable on line 4
  
- Once data is loaded run the "main.py" script
    - Results files will be put into respective directories referenced above
    - Public Results will also be printed to the terminal
    
- Questions? Email support[at]olsohio.org
  
  