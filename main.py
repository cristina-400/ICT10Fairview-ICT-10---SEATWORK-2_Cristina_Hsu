from pyscript import display,document


def general_weighted_average(e): #event for handdling

    first_name = (document.getElementById('first name').value)
    last_name = (document.getElementById('last name').value)

    math = float(document.getElementById('math').value)
    science = float(document.getElementById('science').value)
    english = float(document.getElementById('english').value)
    ict = float(document.getElementById('ict').value)
    ss = float(document.getElementById('ss').value)
    pe = float(document.getElementById('pe').value)
    subjects = ['Mathematics', 'Science', 'English', 'ICT', 'Social Studies', 'Physical Education']

    

    units_subject = (5, 3, 2, 1) #weights for subjects


    weighted_sum = (math * 5 + science * 5 + english * 5 + ss * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units


    summary =f""" {subjects[0]}: {math:.0f}
    {subjects[1]}: {science:.0f}
    {subjects[2]}: {english:.0f}
    {subjects[3]}: {ict:.0f}
    {subjects[4]}: {ss:.0f}
    {subjects[5]}: {pe:.0f}
  
"""
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
    