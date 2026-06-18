import sqlite3

DB_PATH = "data/db/analytics.db"
ALLOWED_CITIES = {"Mumbai", "Delhi", "Bangalore", "Chennai"}

def city_kpi(city: str):
    """Calculate KPIs for a specific city using parameterized SQL to prevent injection."""
    # Validate city against allowlist
    if city not in ALLOWED_CITIES:
        print(f"Error: City '{city}' is not in the allowed cities list.")
        print(f"Allowed cities: {', '.join(sorted(ALLOWED_CITIES))}")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Parameterized query - safe from SQL injection
    query = """
        SELECT 
            COUNT(*) as total_customers,
            AVG(monthly_spend) as avg_spend,
            SUM(churned) as churned_count
        FROM customers_raw
        WHERE city = ?
    """
    
    cursor.execute(query, (city,))
    result = cursor.fetchone()
    conn.close()
    
    total, avg_spend, churned = result
    print(f"City: {city}")
    print(f"  Total Customers: {total}")
    print(f"  Avg Monthly Spend: ${avg_spend:.2f}" if avg_spend else "  Avg Monthly Spend: N/A")
    print(f"  Churned Count: {churned}")
    print()

# Test with valid city
city_kpi("Mumbai")

# Test with SQL injection attempt (should return 0 rows, not all rows)
city_kpi("Mumbai' OR 1=1 --")
