import sqlite3
import sys

def show_students():
    """Display all students in the database"""
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM chai_student ORDER BY id")
    students = cursor.fetchall()
    
    print("\n" + "="*60)
    print("CURRENT STUDENTS IN DATABASE")
    print("="*60)
    print(f"{'ID':<3} {'Name':<20} {'Age':<5} {'Email':<30}")
    print("-"*60)
    
    for student in students:
        print(f"{student[0]:<3} {student[1]:<20} {student[2]:<5} {student[3]:<30}")
    
    conn.close()
    return students

def add_student():
    """Add a new student to the database"""
    print("\n" + "="*40)
    print("ADD NEW STUDENT")
    print("="*40)
    
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: "))
    email = input("Enter student email: ").strip()
    
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO chai_student (name, age, email) VALUES (?, ?, ?)", 
                      (name, age, email))
        conn.commit()
        print(f"✅ Successfully added student: {name}")
    except sqlite3.IntegrityError:
        print("❌ Error: Email already exists!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conn.close()

def edit_student():
    """Edit an existing student"""
    students = show_students()
    
    if not students:
        print("No students found to edit.")
        return
    
    print("\n" + "="*40)
    print("EDIT STUDENT")
    print("="*40)
    
    try:
        student_id = int(input("Enter student ID to edit: "))
        
        # Find the student
        student = None
        for s in students:
            if s[0] == student_id:
                student = s
                break
        
        if not student:
            print("❌ Student not found!")
            return
        
        print(f"\nCurrent data for {student[1]}:")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Email: {student[3]}")
        
        print("\nEnter new values (press Enter to keep current value):")
        new_name = input(f"Name [{student[1]}]: ").strip() or student[1]
        new_age = input(f"Age [{student[2]}]: ").strip()
        new_age = int(new_age) if new_age else student[2]
        new_email = input(f"Email [{student[3]}]: ").strip() or student[3]
        
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        try:
            cursor.execute("UPDATE chai_student SET name=?, age=?, email=? WHERE id=?", 
                          (new_name, new_age, new_email, student_id))
            conn.commit()
            print(f"✅ Successfully updated student: {new_name}")
        except sqlite3.IntegrityError:
            print("❌ Error: Email already exists!")
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            conn.close()
            
    except ValueError:
        print("❌ Please enter a valid student ID number!")

def delete_student():
    """Delete a student from the database"""
    students = show_students()
    
    if not students:
        print("No students found to delete.")
        return
    
    print("\n" + "="*40)
    print("DELETE STUDENT")
    print("="*40)
    
    try:
        student_id = int(input("Enter student ID to delete: "))
        
        # Find the student
        student = None
        for s in students:
            if s[0] == student_id:
                student = s
                break
        
        if not student:
            print("❌ Student not found!")
            return
        
        confirm = input(f"Are you sure you want to delete {student[1]}? (yes/no): ").lower()
        
        if confirm in ['yes', 'y']:
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM chai_student WHERE id=?", (student_id,))
            conn.commit()
            conn.close()
            
            print(f"✅ Successfully deleted student: {student[1]}")
        else:
            print("❌ Deletion cancelled.")
            
    except ValueError:
        print("❌ Please enter a valid student ID number!")

def main():
    while True:
        print("\n" + "="*50)
        print("STUDENT DATABASE EDITOR")
        print("="*50)
        print("1. View all students")
        print("2. Add new student")
        print("3. Edit student")
        print("4. Delete student")
        print("5. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            show_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            edit_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()
