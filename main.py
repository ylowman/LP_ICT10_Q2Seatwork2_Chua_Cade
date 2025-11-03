from pyscript import document, display

def print_grade(e):
    # Get student info
    fn = document.getElementById("firstName").value
    ln = document.getElementById("lastName").value

    # Get grades
    sci = float(document.getElementById("science").value)
    math = float(document.getElementById("math").value)
    eng = float(document.getElementById("english").value)
    ict = float(document.getElementById("ict").value)
    fil = float(document.getElementById("filipino").value)
    pe = float(document.getElementById("pe").value)

    # Store in a list
    grades = [sci, math, eng, ict, fil, pe]
    subjects = ["Science", "Math", "English", "ICT", "Filipino", "PE"]

    # Calculate average
    average = round(sum(grades) / len(grades), 2)

    # Clear previous results
    display("", target="name", append=False)
    display("", target="grades", append=False)
    display("", target="average", append=False)

    # Display results

    # Show the student's name
    display(f"Name: {fn} {ln}", target="name")

    # Show all subjects with their grades
    for subject, grade in zip(subjects, grades):
        display(f"{subject}: {grade}", target="grades", append=True)

    # Show the computed average
    display(f"Average: {average:.2f}", target="average")