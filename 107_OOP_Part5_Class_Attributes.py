# ------------------------------------------------------
# -- Object Oriented Programming => Class Attributes ---
# ------------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------


class Member:

    not_alloed_names = ["Hell", "Shit", "Baloot"]

    users_num = 0

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

        Member.users_num += 1

    def full_name(self):
        if self.fname in Member.not_alloed_names:

            raise ValueError("Name Not Allowed")

        else:

            return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title(self):

        if self.gender == "Male":

            return f"Hello Mr {self.fname}"

        elif self.gender == "Female":

            return f"Hello Miss {self.fname}"

        else:

            return f"Hello {self.fname}"

    def get_all_info(self):

        return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

    def delete_user(self):

        Member.users_num -= 1

member_one = Member("sa", "Aly", "Mohammed", "Male")

# print(member_one.full_name())

print(Member.users_num)