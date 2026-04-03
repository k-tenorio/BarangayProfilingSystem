from model.db_connections import connect_db

# READ
def get_all_residents():
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        SELECT
            r.resident_id,
            CONCAT(r.first_name, ' ', r.last_name) AS full_name,
            r.sex,
            TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) AS age,
            COALESCE(ra.purok, '') AS purok,
            r.civil_status,
            CONCAT(COALESCE(ra.purok, ''), ', ', COALESCE(ra.street, ''), ', ', COALESCE(ra.house_id, '')) AS address
        FROM residents r
        LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
        WHERE r.is_archived = 0
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data


# GET ALL PUROKS
def get_all_puroks():
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        SELECT DISTINCT ra.purok 
        FROM resident_addresses ra
        INNER JOIN residents r ON ra.resident_id = r.resident_id
        WHERE ra.purok IS NOT NULL 
          AND ra.purok != '' 
          AND r.is_archived = 0
        ORDER BY ra.purok
    """

    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return [row[0] for row in data]


# GET RESIDENT DETAILS
def get_resident_details(resident_id):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            r.*, 
            ra.purok, ra.street, ra.house_id,
            rc.contact_number, rc.email,
            rec.emergency_contact_name, rec.emergency_contact_number,
            rp.father_name, rp.mother_name,
            rpi.blood_type, rpi.height_cm, rpi.weight_kg
        FROM residents r
        LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
        LEFT JOIN resident_contacts rc ON r.resident_id = rc.resident_id
        LEFT JOIN resident_emergency_contacts rec ON r.resident_id = rec.resident_id
        LEFT JOIN resident_parents rp ON r.resident_id = rp.resident_id
        LEFT JOIN resident_physical_info rpi ON r.resident_id = rpi.resident_id
        WHERE r.resident_id = %s
    """
    cursor.execute(query, (resident_id,))
    data = cursor.fetchone()
    conn.close()
    return data


# SEARCH 
def search_residents(keyword, search_by="name"):
    conn = connect_db()
    cursor = conn.cursor()

    if search_by == "name":
        query = """
            SELECT
                r.resident_id,
                CONCAT(r.first_name, ' ', r.last_name) AS full_name,
                r.sex,
                TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) AS age,
                COALESCE(ra.purok, '') AS purok,
                r.civil_status,
                CONCAT(COALESCE(ra.purok, ''), ', ', COALESCE(ra.street, ''), ', ', COALESCE(ra.house_id, '')) AS address
            FROM residents r
            LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
            WHERE r.is_archived = 0
              AND (CONCAT(r.first_name, ' ', r.last_name) LIKE %s 
               OR r.resident_id LIKE %s)
        """
        params = (f"%{keyword}%", f"%{keyword}%")
    else:
        query = """
            SELECT
                r.resident_id,
                CONCAT(r.first_name, ' ', r.last_name) AS full_name,
                r.sex,
                TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) AS age,
                COALESCE(ra.purok, '') AS purok,
                r.civil_status,
                CONCAT(COALESCE(ra.purok, ''), ', ', COALESCE(ra.street, ''), ', ', COALESCE(ra.house_id, '')) AS address
            FROM residents r
            LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
            WHERE r.is_archived = 0
              AND r.resident_id LIKE %s
        """
        params = (f"%{keyword}%",)

    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return data


#  FILTER 
def filter_residents(filters):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        SELECT
            r.resident_id,
            CONCAT(r.first_name, ' ', r.last_name) AS full_name,
            r.sex,
            TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) AS age,
            COALESCE(ra.purok, '') AS purok,
            r.civil_status,
            CONCAT(COALESCE(ra.purok, ''), ', ', COALESCE(ra.street, ''), ', ', COALESCE(ra.house_id, '')) AS address
        FROM residents r
        LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
        WHERE r.is_archived = 0
    """

    params = []

    if filters.get('sex') and filters['sex'] != 'All':
        query += " AND r.sex = %s"
        params.append(filters['sex'])

    if filters.get('purok') and filters['purok'] != 'All':
        query += " AND ra.purok = %s"
        params.append(filters['purok'])

    if filters.get('civil_status') and filters['civil_status'] != 'All':
        query += " AND r.civil_status = %s"
        params.append(filters['civil_status'])

    if filters.get('age_range') and filters['age_range'] != 'All':
        age_range = filters['age_range']
        if age_range == '0-17':
            query += " AND TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) BETWEEN 0 AND 17"
        elif age_range == '18-59':
            query += " AND TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) BETWEEN 18 AND 59"
        elif age_range == '60+':
            query += " AND TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) >= 60"

    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return data


#  SORT 
def sort_residents(sort_by, order='ASC'):
    conn = connect_db()
    cursor = conn.cursor()

    sort_columns = {
        'ResidentID': 'r.resident_id',
        'Full Name': 'CONCAT(r.first_name, " ", r.last_name)',
        'Age': 'TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE())',
        'Purok': 'ra.purok'
    }

    if sort_by not in sort_columns:
        sort_by = 'ResidentID'

    column = sort_columns[sort_by]
    order = 'ASC' if order.upper() == 'ASC' else 'DESC'

    query = f"""
        SELECT
            r.resident_id,
            CONCAT(r.first_name, ' ', r.last_name) AS full_name,
            r.sex,
            TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) AS age,
            COALESCE(ra.purok, '') AS purok,
            r.civil_status,
            CONCAT(COALESCE(ra.purok, ''), ', ', COALESCE(ra.street, ''), ', ', COALESCE(ra.house_id, '')) AS address
        FROM residents r
        LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
        WHERE r.is_archived = 0
        ORDER BY {column} {order}
    """

    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data


#  UPDATE RESIDENT 
def update_resident(resident_id, data):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        resident_query = """
            UPDATE residents SET
                first_name = %s, middle_name = %s, last_name = %s,
                sex = %s, date_of_birth = %s, place_of_birth = %s,
                nationality = %s, religion = %s,
                is_deceased = %s, is_pwd = %s,
                civil_status = %s,
                updated_at = NOW()
            WHERE resident_id = %s
        """

        resident_params = (
            data['first_name'], data['middle_name'], data['last_name'],
            data['sex'], data['date_of_birth'], data['place_of_birth'],
            data['nationality'], data['religion'],
            data['is_deceased'], data['is_pwd'],
            data['civil_status'],
            resident_id
        )
        cursor.execute(resident_query, resident_params)

        address_query = """
            INSERT INTO resident_addresses (resident_id, purok, street, house_id)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                purok = VALUES(purok),
                street = VALUES(street),
                house_id = VALUES(house_id)
        """
        cursor.execute(address_query, (resident_id, data['purok'], data['street'], data['house_id']))

        contact_query = """
            INSERT INTO resident_contacts (resident_id, contact_number, email)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                contact_number = VALUES(contact_number),
                email = VALUES(email)
        """
        cursor.execute(contact_query, (resident_id, data['contact_number'], data['email']))

        emergency_query = """
            INSERT INTO resident_emergency_contacts (resident_id, emergency_contact_name, emergency_contact_number)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                emergency_contact_name = VALUES(emergency_contact_name),
                emergency_contact_number = VALUES(emergency_contact_number)
        """
        cursor.execute(emergency_query, (resident_id, data['emergency_contact_name'], data['emergency_contact_number']))

        parent_query = """
            INSERT INTO resident_parents (resident_id, father_name, mother_name)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                father_name = VALUES(father_name),
                mother_name = VALUES(mother_name)
        """
        cursor.execute(parent_query, (resident_id, data['father_name'], data['mother_name']))

        physical_query = """
            INSERT INTO resident_physical_info (resident_id, blood_type, height_cm, weight_kg)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                blood_type = VALUES(blood_type),
                height_cm = VALUES(height_cm),
                weight_kg = VALUES(weight_kg)
        """
        cursor.execute(physical_query, (resident_id, data['blood_type'], data['height_cm'], data['weight_kg']))

        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


#  ARCHIVE RESIDENT 
def archive_resident(resident_id, archived_by="System"):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        UPDATE residents 
        SET is_archived = 1, 
            archived_at = NOW(),
            archived_by = %s
        WHERE resident_id = %s AND is_archived = 0
    """

    try:
        cursor.execute(query, (archived_by, resident_id))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


#  RESTORE RESIDENT 
def restore_resident(resident_id):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        UPDATE residents 
        SET is_archived = 0, 
            archived_at = NULL,
            archived_by = NULL
        WHERE resident_id = %s AND is_archived = 1
    """

    try:
        cursor.execute(query, (resident_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


#  GET ARCHIVED RESIDENTS 
def get_archived_residents():
    conn = connect_db()
    cursor = conn.cursor()

    query = """
        SELECT
            r.resident_id,
            CONCAT(r.first_name, ' ', r.last_name) AS full_name,
            r.sex,
            TIMESTAMPDIFF(YEAR, r.date_of_birth, CURDATE()) AS age,
            COALESCE(ra.purok, '') AS purok,
            r.civil_status,
            CONCAT(COALESCE(ra.purok, ''), ', ', COALESCE(ra.street, ''), ', ', COALESCE(ra.house_id, '')) AS address,
            DATE_FORMAT(r.archived_at, '%Y-%m-%d %H:%i') AS archived_at,
            r.archived_by
        FROM residents r
        LEFT JOIN resident_addresses ra ON r.resident_id = ra.resident_id
        WHERE r.is_archived = 1
        ORDER BY r.archived_at DESC
    """

    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data


#  PERMANENTLY DELETE RESIDENT 
def permanently_delete_resident(resident_id):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        delete_queries = [
            "DELETE FROM resident_addresses WHERE resident_id = %s",
            "DELETE FROM resident_contacts WHERE resident_id = %s",
            "DELETE FROM resident_emergency_contacts WHERE resident_id = %s",
            "DELETE FROM resident_parents WHERE resident_id = %s",
            "DELETE FROM resident_physical_info WHERE resident_id = %s",
            "DELETE FROM residents WHERE resident_id = %s AND is_archived = 1"
        ]

        for delete_query in delete_queries:
            cursor.execute(delete_query, (resident_id,))

        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


#  GET RESIDENT COUNT 
def get_resident_count():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            COUNT(*) as total,
            SUM(CASE WHEN is_archived = 0 THEN 1 ELSE 0 END) as active,
            SUM(CASE WHEN is_archived = 1 THEN 1 ELSE 0 END) as archived
        FROM residents
    """

    cursor.execute(query)
    data = cursor.fetchone()
    conn.close()
    return data


#  GET RESIDENTS BY AGE GROUP 
def get_residents_by_age_group():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            SUM(CASE WHEN TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) < 18 THEN 1 ELSE 0 END) as children,
            SUM(CASE WHEN TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) BETWEEN 18 AND 59 THEN 1 ELSE 0 END) as adults,
            SUM(CASE WHEN TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) >= 60 THEN 1 ELSE 0 END) as seniors
        FROM residents
        WHERE is_archived = 0
    """

    cursor.execute(query)
    data = cursor.fetchone()
    conn.close()
    return data


#  GET RESIDENTS BY SEX 
def get_residents_by_sex():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            sex,
            COUNT(*) as count
        FROM residents
        WHERE is_archived = 0
        GROUP BY sex
    """

    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data