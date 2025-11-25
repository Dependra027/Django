#!/usr/bin/env python3
"""
SQL Query Tool for Student Database
This script provides various ways to query your SQLite database
"""

import sqlite3
import os
from django.core.management import execute_from_command_line
from django.conf import settings
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from chai.models import Student
from django.db import connection

def method1_django_orm():
    """Method 1: Using Django ORM (Object-Relational Mapping)"""
    print("=" * 60)
    print("METHOD 1: DJANGO ORM QUERIES")
    print("=" * 60)
    
    # Get all students
    print("\n1. Get all students:")
    students = Student.objects.all()
    for student in students:
        print(f"   ID: {student.id}, Name: {student.name}, Age: {student.age}, Email: {student.email}")
    
    # Filter students by age
    print("\n2. Students older than 20:")
    older_students = Student.objects.filter(age__gt=20)
    for student in older_students:
        print(f"   {student.name} (Age: {student.age})")
    
    # Search by name
    print("\n3. Students with 'Alice' in name:")
    alice_students = Student.objects.filter(name__icontains='Alice')
    for student in alice_students:
        print(f"   {student.name} - {student.email}")
    
    # Order by age
    print("\n4. Students ordered by age (youngest first):")
    young_first = Student.objects.all().order_by('age')
    for student in young_first:
        print(f"   {student.name} (Age: {student.age})")
    
    # Count students
    print(f"\n5. Total number of students: {Student.objects.count()}")
    
    # Average age
    from django.db.models import Avg
    avg_age = Student.objects.aggregate(avg_age=Avg('age'))
    print(f"   Average age: {avg_age['avg_age']:.1f}")

def method2_raw_sql():
    """Method 2: Using raw SQL with Django"""
    print("\n" + "=" * 60)
    print("METHOD 2: RAW SQL WITH DJANGO")
    print("=" * 60)
    
    with connection.cursor() as cursor:
        # Get all students
        print("\n1. Get all students (raw SQL):")
        cursor.execute("SELECT * FROM chai_student")
        students = cursor.fetchall()
        for student in students:
            print(f"   ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Email: {student[3]}")
        
        # Students older than 20
        print("\n2. Students older than 20 (raw SQL):")
        cursor.execute("SELECT name, age FROM chai_student WHERE age > 20")
        older_students = cursor.fetchall()
        for student in older_students:
            print(f"   {student[0]} (Age: {student[1]})")
        
        # Count by age groups
        print("\n3. Students by age groups (raw SQL):")
        cursor.execute("""
            SELECT 
                CASE 
                    WHEN age < 20 THEN 'Under 20'
                    WHEN age BETWEEN 20 AND 22 THEN '20-22'
                    ELSE 'Over 22'
                END as age_group,
                COUNT(*) as count
            FROM chai_student 
            GROUP BY age_group
            ORDER BY count DESC
        """)
        age_groups = cursor.fetchall()
        for group in age_groups:
            print(f"   {group[0]}: {group[1]} students")
        
        # Find students with specific email domains
        print("\n4. Students with gmail.com emails (raw SQL):")
        cursor.execute("SELECT name, email FROM chai_student WHERE email LIKE '%gmail.com'")
        gmail_students = cursor.fetchall()
        for student in gmail_students:
            print(f"   {student[0]} - {student[1]}")

def method3_direct_sqlite():
    """Method 3: Direct SQLite connection"""
    print("\n" + "=" * 60)
    print("METHOD 3: DIRECT SQLITE CONNECTION")
    print("=" * 60)
    
    # Connect directly to SQLite
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    
    # Get table schema
    print("\n1. Table schema:")
    cursor.execute("PRAGMA table_info(chai_student)")
    columns = cursor.fetchall()
    print("   Columns:")
    for col in columns:
        print(f"   - {col[1]} ({col[2]})")
    
    # Get all students
    print("\n2. All students:")
    cursor.execute("SELECT * FROM chai_student")
    students = cursor.fetchall()
    for student in students:
        print(f"   ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Email: {student[3]}")
    
    # Complex query: Students with even ID numbers
    print("\n3. Students with even ID numbers:")
    cursor.execute("SELECT name, age FROM chai_student WHERE id % 2 = 0")
    even_id_students = cursor.fetchall()
    for student in even_id_students:
        print(f"   {student[0]} (Age: {student[1]})")
    
    # Update query example
    print("\n4. Update example (adding 1 to all ages):")
    cursor.execute("UPDATE chai_student SET age = age + 1")
    conn.commit()
    print("   ✅ All student ages increased by 1")
    
    # Show updated data
    cursor.execute("SELECT name, age FROM chai_student ORDER BY age")
    updated_students = cursor.fetchall()
    print("   Updated ages:")
    for student in updated_students:
        print(f"   - {student[0]}: {student[1]} years old")
    
    # Revert the change
    cursor.execute("UPDATE chai_student SET age = age - 1")
    conn.commit()
    print("   ✅ Reverted age changes")
    
    conn.close()

def method4_custom_queries():
    """Method 4: Custom query examples"""
    print("\n" + "=" * 60)
    print("METHOD 4: CUSTOM QUERY EXAMPLES")
    print("=" * 60)
    
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    
    # Query 1: Find students with longest names
    print("\n1. Students with longest names:")
    cursor.execute("""
        SELECT name, LENGTH(name) as name_length 
        FROM chai_student 
        ORDER BY name_length DESC 
        LIMIT 3
    """)
    long_names = cursor.fetchall()
    for student in long_names:
        print(f"   {student[0]} ({student[1]} characters)")
    
    # Query 2: Students by first letter of name
    print("\n2. Students grouped by first letter of name:")
    cursor.execute("""
        SELECT SUBSTR(name, 1, 1) as first_letter, 
               COUNT(*) as count,
               GROUP_CONCAT(name, ', ') as names
        FROM chai_student 
        GROUP BY first_letter 
        ORDER BY first_letter
    """)
    by_letter = cursor.fetchall()
    for group in by_letter:
        print(f"   {group[0]}: {group[1]} students - {group[2]}")
    
    # Query 3: Age statistics
    print("\n3. Age statistics:")
    cursor.execute("""
        SELECT 
            MIN(age) as min_age,
            MAX(age) as max_age,
            AVG(age) as avg_age,
            COUNT(*) as total_students
        FROM chai_student
    """)
    stats = cursor.fetchone()
    print(f"   Min age: {stats[0]}")
    print(f"   Max age: {stats[1]}")
    print(f"   Average age: {stats[2]:.1f}")
    print(f"   Total students: {stats[3]}")
    
    # Query 4: Find duplicate emails (should be none due to unique constraint)
    print("\n4. Checking for duplicate emails:")
    cursor.execute("""
        SELECT email, COUNT(*) as count 
        FROM chai_student 
        GROUP BY email 
        HAVING COUNT(*) > 1
    """)
    duplicates = cursor.fetchall()
    if duplicates:
        for dup in duplicates:
            print(f"   ❌ Duplicate email: {dup[0]} ({dup[1]} times)")
    else:
        print("   ✅ No duplicate emails found")
    
    conn.close()

def interactive_sql():
    """Interactive SQL shell"""
    print("\n" + "=" * 60)
    print("INTERACTIVE SQL SHELL")
    print("=" * 60)
    print("Enter SQL queries (type 'exit' to quit, 'help' for examples)")
    print("=" * 60)
    
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    
    while True:
        try:
            query = input("\nSQL> ").strip()
            
            if query.lower() == 'exit':
                break
            elif query.lower() == 'help':
                print("\nExample queries:")
                print("  SELECT * FROM chai_student;")
                print("  SELECT name, age FROM chai_student WHERE age > 20;")
                print("  SELECT COUNT(*) FROM chai_student;")
                print("  SELECT * FROM chai_student ORDER BY age DESC;")
                continue
            elif not query:
                continue
            
            cursor.execute(query)
            
            # Check if it's a SELECT query
            if query.upper().startswith('SELECT'):
                results = cursor.fetchall()
                if results:
                    print(f"\nResults ({len(results)} rows):")
                    for row in results:
                        print(f"  {row}")
                else:
                    print("  No results found.")
            else:
                # For non-SELECT queries, commit the changes
                conn.commit()
                print(f"  ✅ Query executed successfully. Rows affected: {cursor.rowcount}")
                
        except sqlite3.Error as e:
            print(f"  ❌ SQL Error: {e}")
        except KeyboardInterrupt:
            print("\n  👋 Exiting...")
            break
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    conn.close()

def main():
    """Main function to run all query methods"""
    print("🎓 STUDENT DATABASE SQL QUERY TOOL")
    print("=" * 60)
    
    while True:
        print("\nChoose a method:")
        print("1. Django ORM Queries")
        print("2. Raw SQL with Django")
        print("3. Direct SQLite Connection")
        print("4. Custom Query Examples")
        print("5. Interactive SQL Shell")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            method1_django_orm()
        elif choice == '2':
            method2_raw_sql()
        elif choice == '3':
            method3_direct_sqlite()
        elif choice == '4':
            method4_custom_queries()
        elif choice == '5':
            interactive_sql()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()
