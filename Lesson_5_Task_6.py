# Pavel Krupenya
# Lessons
subj = {}
new_str = ""
with open("text_6.txt", "r", encoding="utf8") as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.replace("-", "0").split()
        for el in lecture:
            if ord(el) in range(48,58):
               new_str += el
        lecture = new_str
        new_str = ""
        for el in practice:
            if ord(el) in range(48,58):
               new_str += el
        practice = new_str
        new_str = ""
        for el in lab:
            if ord(el) in range(48,58):
               new_str += el
        lab = new_str
        new_str = ""
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f"Total amount of hours for the subject - \n {subj}")
input("\nPress Enter for exit")