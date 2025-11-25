from student_picker import StudentPicker

students = [
    "Luca Ciaone",
    "Matteo Parmiciaoli",
    "Claudio Rossi",
    "Luigi Macioni",
    "Gino Ricci",
    "Gino Belli",
    "Marco Cioni",
    "Alice Mori",
    "Chiara Bianchi",
    "Paolo Conti"
]

picker = StudentPicker(students)

# --- TEST 1: Priorità 1 (match esatto) ---
print("\n=== TEST 1 — PRIORITÀ 1 (sottostringa esatta) ===")
filtered = picker.filter_students("ciao")  # matcha "Parmiciaoli"
print("Filtrati:", filtered)
print("Scelti:", picker.pick_three(filtered))

# --- TEST 2: Priorità 2 (gruppo) ---
print("\n=== TEST 2 — PRIORITÀ 2 (gruppo caratteri) ===")
filtered = picker.filter_students("xyz")  # nessun match esatto → gruppo
print("Filtrati:", filtered)
print("Scelti:", picker.pick_three(filtered))

# --- TEST 3: Priorità 3 (range min-max) ---
print("\n=== TEST 3 — PRIORITÀ 3 (range) ===")
filtered = picker.filter_students("qv")  # range q–v
print("Filtrati:", filtered)
print("Scelti:", picker.pick_three(filtered))
