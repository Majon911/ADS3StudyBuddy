# The MAIN function StudyBuddy

storage = []


class Node:
    def __init__(self, tutorname, degree, field, year, q_answered, time_active, score):
        self.tutorname = tutorname
        self.degree = degree
        self.field = field
        self.year = year
        self.q_answered = q_answered
        self.time_active = time_active
        self.score = score
        self.adjacencyList = []
        self.visited = False

    def dfs(self, inputed_year, inputed_field, inputed_degree):
        self.visited = True
        self.score = 0
        self.score = self.score + self.q_answered  # Weights to be adjusted
        self.score = self.score + self.time_active
        if inputed_field == "OTHER":
            if self.year >= inputed_year:
                self.score = self.score + 20
                if self.degree == inputed_degree:
                    self.score = self.score + 30
                    storage.append((self.tutorname, self.score, self.field, self.degree))
        else:
            if self.year >= inputed_year:
                self.score = self.score + 10
                if self.field == inputed_field:
                    self.score = self.score + 20
                    if self.degree == inputed_degree:
                        self.score = self.score + 30
                        storage.append((self.tutorname, self.score, self.field, self.degree))
                    else:
                        storage.append((self.tutorname, self.score, self.field, self.degree))

        for n in self.adjacencyList:
            if not n.visited:
                n.dfs(inputed_year, inputed_field, inputed_degree)


# Time_active in months
def tutor_list(inputed_year, inputed_field, inputed_degree):
    tutor1 = Node("Michael", "BDBA", "MATH", 3, 5, 4, 0)  # root
    tutor2 = Node("Juan", "BBA", "LAW", 2, 7, 16, 0)  # Starts BBA
    tutor1.adjacencyList.append(tutor2)
    tutor3 = Node("Anna", "BDBA", "MATH", 3, 12, 10, 0)  # Starts BDBA
    tutor1.adjacencyList.append(tutor3)
    tutor4 = Node("Big John", "BDBA", "STATISTICS", 1, 5, 1, 0)
    tutor3.adjacencyList.append(tutor4)
    tutor5 = Node("Alicia", "BBA", "FINANCE", 2, 8, 12, 0)
    tutor2.adjacencyList.append(tutor5)
    tutor6 = Node("Annie", "BA", "MATH", 3, 3, 10, 0)  # Starts BA
    tutor1.adjacencyList.append(tutor6)
    tutor7 = Node("Franco", "BDBA", "MENTORSHIP", 3, 5, 3, 0)
    tutor3.adjacencyList.append(tutor7)
    tutor8 = Node("Giovanni", "IR", "LAW", 4, 10, 13, 0)  # Starts IR
    tutor1.adjacencyList.append(tutor8)
    tutor9 = Node("Anna", "IR", "MENTORSHIP", 3, 12, 9, 0)
    tutor8.adjacencyList.append(tutor9)
    tutor10 = Node("Michael", "BAM", "MATH", 4, 6, 7, 0)  # Starts BAM
    tutor1.adjacencyList.append(tutor10)
    tutor11 = Node("Oscar", "BAM", "STATISTICS", 2, 8, 6, 0)
    tutor10.adjacencyList.append(tutor11)
    tutor12 = Node("Annie", "BLL", "LAW", 1, 15, 2, 0)  # Starts BLL
    tutor1.adjacencyList.append(tutor12)
    tutor13 = Node("Aaron", "BDBA", "STATISTICS", 3, 5, 14, 0)
    tutor4.adjacencyList.append(tutor13)
    tutor14 = Node("Pablo", "BBA", "FINANCE", 2, 4, 14, 0)
    tutor5.adjacencyList.append(tutor14)
    tutor15 = Node("Andrew", "BBA", "MATH", 3, 1, 15, 0)
    tutor2.adjacencyList.append(tutor15)
    tutor16 = Node("Patricia", "BAM", "FINANCE", 4, 13, 4, 0)
    tutor10.adjacencyList.append(tutor16)
    tutor17 = Node("Joanna", "IR", "STATISTICS", 4, 8, 16, 0)
    tutor8.adjacencyList.append(tutor17)
    tutor18 = Node("Jorge", "BBA", "MENTORSHIP", 3, 4, 10, 0)
    tutor2.adjacencyList.append(tutor18)
    tutor19 = Node("Adi", "IR", "LAW", 3, 2, 5, 0)
    tutor8.adjacencyList.append(tutor19)
    tutor20 = Node("Patricio", "BDBA", "BUSINESS", 1, 5, 5, 0)
    tutor3.adjacencyList.append(tutor20)
    tutor21 = Node("Adrianna", "BBA", "BUSINESS", 2, 7, 4, 0)
    tutor2.adjacencyList.append(tutor21)
    tutor22 = Node("Andrew", "BBA", "BUSINESS", 3, 11, 10, 0)
    tutor21.adjacencyList.append(tutor22)
    print("\n\nAVAILABLE TUTORS:")
    tutor1.dfs(inputed_year, inputed_field, inputed_degree)

# The available tutors sorted according to their score.
    storage.sort(key=lambda storage: storage[1], reverse=True)
    for i in storage:
     print("The tutor is:", i[0], "and his/her score is:", i[1], "DETAILS:", i[2] + ",", i[3])


def main():
    print("StudyBuddy Prototype v. 1.0.2")
    print("---------------------------------------------------------")
    print("Welcome to the StudyBuddy Application!")
    print("A higher score means a more suitable tutor according to our algorithm.")
    print("In order to get matched, answer the following questions!")
    print("---------------------------------------------------------\n")
    inputed_year = int(input("Which year are you on?: "))
    inputed_field = input("What is the field in which you have a problem? \n(Choose: STATISTICS, MATH, LAW, BUSINESS, FINANCE, MENTORSHIP, OTHER): ")
    inputed_degree = input("What is your degree? \n(Choose: BBA, BDBA, BA, IR, BLL, BAM, ect.): ")

    tutor_list(inputed_year, inputed_field, inputed_degree)
    print("\nNOTE: If none tutors printed, none available because of study year or lack of expertise in field!")

    input('\n\nPRESS ENTER TO CLOSE THE WINDOW!')


main()
