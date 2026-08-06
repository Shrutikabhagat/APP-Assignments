class Printer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Printer, cls).__new__(cls)
            print("Printer Created")
        return cls._instance

    def print_document(self, document):
        print(f"Printing: {document}")


# Multiple users accessing the same printer
user1 = Printer()
user2 = Printer()

user1.print_document("Assignment.pdf")
user2.print_document("ProjectReport.docx")

if user1 is user2:
    print("Only one Printer object exists.")
else:
    print("Different Printer objects exist.")