#!/usr/bin/env python3
"""
Simple SQL Shell for Student Database
Usage: python sql_shell.py "SELECT * FROM chai_student;"
"""

import sqlite3
import sys

def execute_sql(query):
    """Execute SQL query and return results"""
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        cursor.execute(query)
        
        # Check if it's a SELECT query
        if query.strip().upper().startswith('SELECT'):
            results = cursor.fetchall()
            return results
        else:
            # For non-SELECT queries, commit changes
            conn.commit()
            return f"Query executed successfully. Rows affected: {cursor.rowcount}"
            
    except sqlite3.Error as e:
        return f"SQL Error: {e}"
    except Exception as e:
        return f"Error: {e}"
    finally:
        if 'conn' in locals():
            conn.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: python sql_shell.py \"SQL_QUERY\"")
        print("\nExample queries:")
        print('  python sql_shell.py "SELECT * FROM chai_student;"')
        print('  python sql_shell.py "SELECT name, age FROM chai_student WHERE age > 20;"')
        print('  python sql_shell.py "SELECT COUNT(*) FROM chai_student;"')
        return
    
    query = sys.argv[1]
    result = execute_sql(query)
    
    if isinstance(result, str):
        print(result)
    else:
        print(f"Results ({len(result)} rows):")
        for row in result:
            print(f"  {row}")

if __name__ == "__main__":
    main()
