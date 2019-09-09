class Student:

    P_percent = 0.05
    H_percent = 0.30
    Q_percent = 0.25
    Proj_percent = 0.40

    def __init__(self, ID, firstName, lastName, gender, birthdate, participationGrade, homeworkGrade, quizGrade, ProjectGrade):
        self.ID = ID
        self.fullName = firstName + " " + lastName
        self.email = firstName + "_" + lastName + "@edu.aua.am"
        self.gender = gender
        self.birthdate = birthdate
        self.participation = participationGrade
        self.homework = homeworkGrade
        self.quiz = quizGrade
        self.Project = ProjectGrade


    def getPersonalInfo(self):
        print ("Personal information for Student #" + self.ID +" \n")
        print(self.ID)
        print(self.fullName)
        print(self.email)
        print(self.gender)
        print(self.birthdate)
        print(" \n")


    def getCurrentGrade(self):
        Part_calculated = float(self.P_percent * self.participation)
        HW_calculated = float(self.H_percent * self.homework)
        QZ_calculated = float(self.Q_percent * self.quiz)
        Proj_calculated = float(self.Proj_percent * self.Project)
        finalGrade = float(Part_calculated + HW_calculated + QZ_calculated + Proj_calculated)
        print("The Students final grade is:" + str(finalGrade) + "\n")


def main():

    st1 = Student("AUA123", "name1", "sur1", "Male", "04/09/2019", 98, 99, 75, 80)
    st2 = Student("AUA456", "name2", "sur2", "Female", "02/05/2018", 89, 98, 96, 88)

    st1.getPersonalInfo()
    st1.getCurrentGrade()

    st2.getPersonalInfo()
    st2.getCurrentGrade()

main()
