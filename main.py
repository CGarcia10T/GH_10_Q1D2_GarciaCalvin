from pyscript import display, document

def function1(e):
    name = document.getElementById("input1").value
    age = document.getElementById("input2").value
    school = document.getElementById("input3").value
    
    sample = f"""Student Profile:\n
    Name    : {name}\n
    Age     : {age}\n
    School  : {school}\n
    
    Notes:\n
    {name} is {age} years old and studies at {school}. This information was gathered through input fields and displayed using PyScript.
    """

    display(sample, target="output")