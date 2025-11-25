import re
import random

class StudentPicker:

    def __init__(self, students):
        """
        students: lista di stringhe "Nome Cognome"
        """
        self.students = students

    def filter_students(self, query):
        """
        Applica la logica di priorità:
        1. Atomo (sottostringa esatta)
        2. Gruppo di caratteri
        3. Range min-max + spazio
        """
        query = query.strip()
        students = self.students

        # 1️⃣ PRIORITÀ 1 – match esatto come sottostringa
        exact_regex = re.compile(re.escape(query), re.IGNORECASE)
        exact_matches = [s for s in students if exact_regex.search(s)]

        if exact_matches:
            print("[PRIORITÀ 1] Trovati match esatti.")
            return exact_matches

        # 2️⃣ PRIORITÀ 2 – gruppo di caratteri
        group_regex = re.compile(f"[{re.escape(query)}]", re.IGNORECASE)
        group_matches = [s for s in students if group_regex.search(s)]

        if group_matches:
            print("[PRIORITÀ 2] Trovati match come gruppo di caratteri.")
            return group_matches

        # 3️⃣ PRIORITÀ 3 – range min-max + spazio
        minimo = min(query.lower())
        massimo = max(query.lower())

        range_regex = re.compile(f"[{minimo}-{massimo} ]", re.IGNORECASE)
        range_matches = [s for s in students if range_regex.search(s)]

        print("[PRIORITÀ 3] Trovati match tramite range.")
        return range_matches

    def pick_three(self, filtered_students):
        """
        Ritorna 3 studenti random, o meno se non disponibili.
        """
        if len(filtered_students) <= 3:
            return filtered_students
        
        return random.sample(filtered_students, 3)
