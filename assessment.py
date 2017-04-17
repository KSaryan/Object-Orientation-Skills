"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

1. The three main design advantages of object orientation are abstraction, encapsulation, 
and polymorphism. Abstraction means that you or someone else can create a method or a class
somewhere else and then you can later use that method or class without having to know how
it works. For example, I can use len() without having to know how it works exactly.
Encapsulation means you can organize better. You can keep everything you need together. For 
example, your Cat class can contain everything about cats. Or your shipping.py file, can contain 
all the functions that have to do with shipping. Finally, polymorphism means you can
change things. You can create a new class that inherits from  your Cat class. It can
take on some of the attributes and methods while overriding others.

2. A class is, as said in lecture, a type of thing. It's some type of object that has
been defined and has certain attributes and methods associated with it. So, all the instances
of that class will only have those attributes and methods you gave the class or the class inherited
from another class (unless you assign more). 

3. These are the attributes that are specific to this one particular instance of this class.
It's kind of like when a baby is born: there were always humans but this is a particular human;
all humans have certain attributes, like hair color, but this baby's hair color is brown. The 
brown hair color is its instance attribute. However, maybe the child grows up and changes its hair color.
That would be like reassigning the instance attribute. 

4. A method is a function that is connected to a particular class. The method can only be used
with the class it is connected to. And it must be defined when the class is defined.

5. An instance is one incarnation of a class. Book could be a class, but War and Peace is one
instance of a book. It shares many class attributes and methods with other books: it's rectangular, 
you can read it. However, it also has some instance attributes: page count, language.

6. A class attribute is true of all the instances of that class, while an instance attribute
is particular to each instance. For example, if you had a class called Melon. Shape may be a 
class attribute, since all melons are round. However, color or width would be instance
attributes since some melons will be differing colors and sizes.

"""


# Parts 2 through 5:
class Student(object):
    """terrific students"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        return "<>{}, student<>". format(self.first_name)


class Question(object):
    """difficult questions"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        return "<>this is a question<>"

    def ask_and_evaluate(self):
        """asks questions and returns if user got right answer"""

        print self.question
        user_answer = raw_input ("Your answer: ")

        # I turned the correct answer into a string, in case it was an interger
        return user_answer == str(self.correct_answer)


class Exam (object):
    """exams"""
    
    def __init__(self, name):
        self.name = name
        self.questions = []
    
    def __repr__(self):
        return "{} exam".format(self.name)
    
    def add_question(self, question, answer):
        """adds questions to exam"""

        question1= Question(question, answer)
        self.questions.append(question1)
    
    def administer(self):
        """"administers exam and and returnds score as percentage"""

        score = 0
        for question in self.questions:
            result = question.ask_and_evaluate()
            if result:
                score += 1
        
        return (float(score)/len(self.questions)) * 100

# I wasn't sure if you wanted this way...

# class StudentExam(object):
#     """stores student, exam, and student's exam score"""
    
#     def __init__(self, student, exam):
#         self.student = student
#         self.exam = exam
#         self.student_score = None 
    
#     def __repr___(self):
#         return "<>{} taking {} exam<>".format(self.student, self.exam)
    
#     def take_test(self):
#         self.student_score = self.exam.administer()
#         print "{}, you have earned a score of {} percent on the {}.".format(self.student.first_name, 
#             self.student_score, self.exam)


# def example (exam_name, student_first_name, student_last_name, student_adresss):
#     """creates student and exam; administers exam"""

#     exam = Exam(exam_name)
#     exam.add_question("In which continent is Italy?", "Europe")
#     exam.add_question("What is 2+3?", 5)
#     student = Student(student_first_name, student_last_name, student_adresss)
#     student_exam = StudentExam(student, exam)
#     student_exam.take_test()

# .... or this way

class StudentExam(object):
    """stores student, exam, and student's exam score"""
    
    def __init__(self, student_first_name, student_last_name, student_adresss, exam_name):
        self.student = Student(student_first_name, student_last_name, student_adresss)
        self.exam = Exam(exam_name)
        self.student_score = None 
    
    def __repr___(self):
        return "<>{} taking {} exam<>".format(self.student, self.exam)
    
    def take_test(self):
        """administers test and prints score"""

        self.student_score = self.exam.administer()
        
        print "{}, you have earned a score of {} percent on the {}.".format(self.student.first_name, 
            self.student_score, self.exam)


def example (student_first_name, student_last_name, student_adresss, exam_name):
    """creates student and exam; administers exam"""

    student_exam = StudentExam(student_first_name, student_last_name, student_adresss, exam_name)
    student_exam.exam.add_question("In which continent is Italy?", "Europe")
    student_exam.exam.add_question("What is 2+3?", 5)
    student_exam.take_test()


class Quiz(Exam):
    """Quiz that is pass/fail"""

    def __init__(self):
        super(Quiz, self).__init__("quiz")
    
    def __repr__(self):
        return "<>this is only a quiz<>"
    
    def administer(self):
        """administers quiz and returns 1 or 0 to reprsent pass/fail"""

        percentage = super(Quiz, self).administer()
        
        if percentage >= 50:
            return 1
        else:
            return 0


class StudentQuiz(StudentExam):
    """stores student, quiz name, and pass/fail"""
    
    def __init__(self, student_first_name, student_last_name, student_adresss):
        super(StudentQuiz, self).__init__(student_first_name, student_last_name, student_adresss, "quiz")
        self.quiz = Quiz()
    
    def __repr__(self):
        return "<>{}'s quiz<>".format(self.student.first_name)
    
    def take_quiz(self):
        """administers quiz and prints pass/fail results"""

        self.student_score = self.quiz.administer()
        
        if self.student_score == 1:
            print "{}, you passed!".format(self.student.first_name)
        else:
            print "Sorry, {}, you failed.".format(self.student.first_name)


def example2 (student_first_name, student_last_name, student_adresss):
    """creates student and quiz; administers quiz"""

    student_quiz = StudentQuiz(student_first_name, student_last_name, student_adresss)
    student_quiz.quiz.add_question("In which continent is Italy?", "Europe")
    student_quiz.quiz.add_question("What is 2+3?", 5)
    student_quiz.take_quiz()






