# Exploring Knowledge Representation in AI Lab
# Ontology, Semantic Networks, Frames and Knowledge_Representation
Ontology_Semantic_Networks_Frames_&amp;_Knowledge_Representation

# Lab Introduction
In artificial intelligence, knowledge representation is a cornerstone for enabling machines to understand, reason, and act intelligently within a domain. Unlike raw data, structured knowledge allows AI systems to capture the meaning of concepts, their properties, and relationships, which is critical for reasoning and decision-making.
This lab focuses on three key representation techniques: ontologies, semantic networks, and frames. Students will learn how to define concepts and their relationships using an ontology, visualise associations through semantic networks, and represent complex objects or situations with frames. These methods provide the foundation for building intelligent systems that can model domains such as education, healthcare, and libraries in a way that supports both human understanding and machine reasoning.

The ontology representation in this lab is not in OWL (Web Ontology Language) or RDF (Resource Description Framework). Instead, the lab uses a Python dictionary to mimic ontology concepts, their properties, and relationships.
By engaging in this lab, students will bridge theoretical concepts from Session 6 with practical implementation, developing a deeper appreciation of how structured, declarative, and procedural knowledge can be encoded in AI systems.

# Ontology Lab (Python)

# Lab Objectives
By the end of this lab, students will be able to:
1.	Define and construct a simple ontology for a given domain.
2.	Represent relationships between concepts using a semantic network.
3.	Model knowledge using frames with attributes and inheritance.
4.	Differentiate between structural, declarative, and procedural knowledge in examples.

# Lab Activities

# Step 1: Set Up Environment
Choose one option:
1.	Python (optional, for implementation)
2.	Google Colab (optional, for implementation)
3.	Pen and paper or a diagramming tool (for semantic networks)

# Step 2: Building an Ontology
1.	Choose a simple domain (e.g., University System).
2.	Identify entities (e.g., Student, Course, Lecturer, Department).
3.	Define relationships:
 	Student → enrolled_in → Course
 	Lecturer → teaches → Course
 	Course → belongs_to → Department
4.	Represent the ontology as a structured list or in OWL/RDF syntax (if using tools like Protégé).

# Step 3: Creating a Semantic Network
1.	Using the same domain, draw a graph where:
 	Nodes = entities (Student, Lecturer, Course, Department).
 	Edges = relationships (enrolled_in, teaches, belongs_to).

3.	 Example:
 	Student “is a” Person
 	Course “is a” Academic Unit
 	Department “is part of” University

# Step 4: Designing Frames
1.	Create a Frame for “Course” with attributes (slots):
 	Course Code
 	Course Title
 	Credits
 	Lecturer (filler: Name of Lecturer)
 	Students (filler: list of enrolled students)
2.	Show Inheritance:
 	Frame ElectiveCourse inherits from Course but has an additional slot (Prerequisites).

# Step 5: Identifying Types of Knowledge
 	Given the ontology and frames created, classify knowledge into:
 	Structural Knowledge: Student–Course–Lecturer relationships.
 	Declarative Knowledge: “CS101 is a Course with 3 Credits.”
 	Procedural Knowledge: “To register for a Course, a Student must log into the portal and pay fees.”

# Lab Questions
1.	How does an ontology differ from a database schema?
2.	Why are semantic networks useful for representing associative knowledge?
3.	Give a real-world example of where frames would be more useful than rules.
4.	Which type of knowledge (structural, declarative, procedural) is hardest for machines to represent, and why?

# Expected Output
 	A simple ontology for the chosen domain.
 	A semantic network diagram.
 	A frame-based knowledge structure with inheritance.
 	A short reflection on structural vs. declarative vs. procedural knowledge.
