import streamlit as st

st.subheader('GECA SGPA CALCULATOR')
st.text('By Mohammad Saad')

branches = ['Civil', 'Electrical', 'Mechanical', 'EnTC', 'CSE', 'IT']
semesters = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
ITI = ['Chemistry',3, 'Mechanics',3, 'BcomIT',3, 'Engg Exploration',2, 'M1',4, 'Lab Mechanics',1,'Lab Chemistry',1, 'lab BcomIT',1]
ITII = ['Communication Skills',2,'M2',4, 'EGD',2 ,'Physics',4,'elective1 (3 credit)',3,'Lab Elective(for BEE/BCE)',1,'Lab Communication Skills',1,'Lab Computer Workshop',2, 'Lab EGD',1,'Lab Physics',1]
ITIII = ['M3',3, 'DMS',3, 'DS',3, 'CN',3, 'OOP',3,'DEM',3, 'elective1 (3 credit)',3, 'elective2 (3 credit)',3, 'Lab DS ',1,'Lab CN',1,'Lab OOP',1,'Lab DEM',1]
ITIV = ['M4',4,'DAA',3,'DBMS',3,'OS',3,'IOT',3,'elective1',3,'elective2',3,'elective3',3,'lab OS',1,'lab DBMS',1,'lab DAA',1,'lab IOT',1]
ITV = ['AI',3, 'ML',3, 'TOC',4, 'SE',3, 'elective1',3, 'elective2',3, 'elective3',3,'Lab ML',1,'Lab SE',1,'Lab CPL',2,'Mini Project',2]
ITVI = ['AI', 'ML', 'TOC', 'SE', 'elective1', 'elective2', 'sem6']
ITVII = ['AI', 'ML', 'TOC', 'SE', 'elective1', 'elective2', 'sem7']
ITVIII = ['AI', 'ML', 'TOC', 'SE', 'elective1', 'elective2', 'sem8']
grades = ['A++', 'A+', 'A', 'B+', 'B', 'C+', 'C','Not Opted']
grades2 = ['A++', 'A+', 'A', 'B+', 'B', 'C+', 'C']
sgpa = 0.0

if 'selected_grades' not in st.session_state:
    st.session_state.selected_grades = {}

a, b, c = st.columns(3)
branch = a.selectbox('Branch', [''] + branches)
semester = b.selectbox('Semester', [''] + semesters)
st.text('_____________________________________________________________________________________')
# submit1 = st.button('Submit')
x, y, z, w = st.columns(4)
l, m, n = st.columns(3)
flag = 1
# code = branch+semester
try:
    if branch and semester:
        if branch == 'IT' and semester == 'I':
            code = ITI
        elif branch == 'IT' and semester == 'II':
            code = ITII
        elif branch == 'IT' and semester == 'III':
            code = ITIII
        elif branch == 'IT' and semester == 'IV':
            code = ITIV
        elif branch == 'IT' and semester == 'V':
            code = ITV
        # elif branch == 'IT' and semester == 'VI':
        #     code = ITVI
        # elif branch == 'IT' and semester == 'VII':
        #     code = ITVII
        # elif branch == 'IT' and semester == 'VIII':
        #     code = ITVIII
        else:
            flag = 0
            st.text(f'NO DATA PROVIDED FOR {branch} Branch {semester} semester')
            image_url = 'data:image/png;base64,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'
            st.image(image_url, caption='Image from URL', use_column_width=True)
except Exception as e:
    st.text('Sorry for the inconvenience, we are working on it')
    st.text(e)

sub_count = 0
total = 0
elective = ['elective1','elective2','elective3']
if flag == 1 and semester and branch:
    

    selected_grades = [] 
    credits = []
    grade_num = []
    buffer = [0,1, 2, 3, 4, 5]
    grade_num = []
    for i in range(len(code)):
        if code[i] in buffer:
            credits.append(code[i])
        else:
            if code[i] in elective:
                selected_grade = x.selectbox(code[i], grades, key=f'key_{i}')
            else:
                selected_grade = x.selectbox(code[i], grades2, key=f'key_{i}')
            if selected_grade == 'Not Opted':
                sub_count = sub_count + 1
            selected_grades.append(selected_grade)

    def calc(selected_grades):
        global sub_count
        global sgpa
        global grade_num
        global total
        score = 0
       
        for grade in selected_grades:
            if grade == 'A++':
                grade_num.append(10)
            elif grade == 'A+':
                grade_num.append(9)
            elif grade == 'A':
                grade_num.append(8)
            elif grade == 'B+':
                grade_num.append(7)
            elif grade == 'B':
                grade_num.append(6)
            elif grade == 'C+':
                grade_num.append(5)
            elif grade == 'C':
                grade_num.append(4)
            else:
                grade_num.append(0)

        for i in range(len(credits)):
            score = score + (credits[i] * grade_num[i])
            total = credits[i] + total
        total = total - (sub_count * 3)
        sgpa = score / total

    calculate = l.button('Calculate SGPA')
    if calculate:
        grade_num = calc(selected_grades)
        m.subheader(f'SGPA : {sgpa:.3f}')
        n.subheader(f'credits : {total}')

st.text('In case of any reports or suggestions kindly Mail')
st.text('saadiqbal1921@gmail.com')
text = st.text_area('or write suggestions')
button2 = st.button('submit')



