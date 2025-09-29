# ----------------------------
# Session 6: Ontology
# Activity: Knowledge Representation in Python
# Instructor: Prince C. Banda
# ----------------------------

# 1. Representing an Ontology using dictionaries
ontology = {
    "Student": {"is_a": "Person", "enrolled_in": "Course"},
    "Lecturer": {"is_a": "Person", "teaches": "Course"},
    "Course": {"is_a": "AcademicUnit", "belongs_to": "Department"},
    "Department": {"is_a": "Faculty", "part_of": "University"}
}

print("📘 Ontology Representation")
for concept, relations in ontology.items():
    print(f"{concept}: {relations}")

# 2. Semantic Network (Graph using adjacency list)
semantic_network = {
    "Student": ["Person", "Course"],
    "Lecturer": ["Person", "Course"],
    "Course": ["AcademicUnit", "Department"],
    "Department": ["Faculty", "University"]
}

print("\n🌐 Semantic Network Connections")
for node, edges in semantic_network.items():
    print(f"{node} --> {', '.join(edges)}")

# 3. Frames: Using Classes with Inheritance
class Course:
    def __init__(self, code, title, credits, lecturer):
        self.code = code
        self.title = title
        self.credits = credits
        self.lecturer = lecturer
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

class ElectiveCourse(Course):  # Inherits from Course
    def __init__(self, code, title, credits, lecturer, prerequisites):
        super().__init__(code, title, credits, lecturer)
        self.prerequisites = prerequisites

# Example usage
cs101 = Course("CS101", "Intro to AI", 3, "Mr. Banda")
cs101.add_student("Alice")
cs101.add_student("Bob")

cs202 = ElectiveCourse("CS202", "Machine Learning", 3, "Mr. Ranjan", ["CS101"])
cs202.add_student("Charlie")

print("\n🖼 Frame Representation")
print(f"{cs101.title} taught by {cs101.lecturer}, Students: {cs101.students}")
print(f"{cs202.title} taught by {cs202.lecturer}, Prerequisites: {cs202.prerequisites}, Students: {cs202.students}")

# 4. Types of Knowledge Example
print("\n📚 Types of Knowledge")
print("Structural Knowledge: Student -> enrolled_in -> Course")
print("Declarative Knowledge: CS101 is a Course with 3 credits.")
print("Procedural Knowledge: To register, a Student must log into the portal and pay fees.")
