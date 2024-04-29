import datetime
import random

class Medication:
    def __init__(self, name, dosage, schedule):
        self.name = name
        self.dosage = dosage
        self.schedule = schedule

    def __str__(self):
        return f"{self.name}, Dosage: {self.dosage}, Schedule: {', '.join(self.schedule)}"

class MedicationTracker:
    def __init__(self):
        self.medications = []

    def add_medication(self, medication):
        self.medications.append(medication)

    def show_medications(self):
        if not self.medications:
            print("No medications added yet.")
        else:
            print("Medications:")
            for idx, med in enumerate(self.medications, 1):
                print(f"{idx}. {med}")

    def check_medication_schedule(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        medications_to_take = []
        for med in self.medications:
            if current_time in med.schedule:
                medications_to_take.append(med)
        return medications_to_take

class HealthTrackerApp:
    def __init__(self):
        self.medication_tracker = MedicationTracker()
        self.user_name = None
        self.physical_activities = []

    def welcome_message(self):
        print("Welcome to Health Tracker App for Seniors!")
        print("1. Add Medication")
        print("2. Show Medications")
        print("3. Check Medication Schedule")
        print("4. Track Physical Activity")
        print("5. Dial 911 (Emergency)")
        print("6. Personalized Health Tips")
        print("7. Exit")

    def get_user_name(self):
        self.user_name = input("Please enter your name: ")

    def track_physical_activity(self):
        activity = input("Enter the physical activity performed: ")
        duration = input("Enter the duration of the activity (in minutes): ")
        self.physical_activities.append((activity, duration))
        print("Physical activity tracked successfully.")

    def dial_emergency_contact(self):
        print("Dialing 911 (Emergency)...")
        # Add code to dial 911 here

    def show_personalized_health_tips(self):
        health_tips = [
            "Stay hydrated by drinking plenty of water throughout the day.",
            "Get at least 30 minutes of moderate exercise daily to maintain a healthy lifestyle.",
            "Incorporate a variety of colorful fruits and vegetables into your diet for optimal nutrition.",
            "Remember to take short breaks and stretch if you spend long periods sitting.",
            "Prioritize getting enough sleep each night to support overall health and well-being."
        ]
        tip = random.choice(health_tips)
        print(f"Hello, {self.user_name}! Here's a personalized health tip for you:\n{tip}")

    def main_menu(self):
        while True:
            self.welcome_message()
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter medication name: ")
                dosage = input("Enter dosage: ")
                schedule = input("Enter schedule (HH:MM format, separate multiple times by comma): ").split(",")
                medication = Medication(name, dosage, schedule)
                self.medication_tracker.add_medication(medication)
                print("Medication added successfully.")

            elif choice == "2":
                self.medication_tracker.show_medications()

            elif choice == "3":
                medications_to_take = self.medication_tracker.check_medication_schedule()
                if medications_to_take:
                    print("It's time to take the following medications:")
                    for med in medications_to_take:
                        print(f"- {med.name} ({med.dosage})")
                else:
                    print("No medications scheduled at this time.")

            elif choice == "4":
                self.track_physical_activity()

            elif choice == "5":
                self.dial_emergency_contact()

            elif choice == "6":
                self.show_personalized_health_tips()

            elif choice == "7":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

def main():
    app = HealthTrackerApp()
    app.get_user_name()
    app.main_menu()

if __name__ == "__main__":
    main()

