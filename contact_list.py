class ContactList:
    
# #contacts as a list of dictionaries - __Dict__ or [{}] .sorted by name
    def __init__(self, group):
        self.group = group
        self.list = list
        self.friends = []
        self.work_buddies = []
# 3 instance methods, add_contact({}), remove_contact('Alice'), find_shared_contacts

    def add_contact(self, name, number):
        if self.group == 'My Friends':
            self.friends.append({'name': f'{name}', 'number': f'{number}'})
        if self.group == 'Work Buddies':
            self.work_buddies.append({'name': f'{name}', 'number': f'{number}'})
        #print(f'{self.group} : {self.work_buddies}')
    def remove_contact():
        pass
    def find_shared_contact():
        pass
        
# # group name, friends work_buddies, extended family, etc..
#friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
#work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends')
my_work_buddies = ContactList('Work Buddies')

my_friends_list.add_contact("Alice", "867-5309")
my_friends_list.add_contact("Carlos", "55-5555")

my_work_buddies.add_contact("Bob", "555-5555")
my_work_buddies.add_contact("Alice", "867-5309")



print(f'{my_friends_list.group} : {my_friends_list.friends}')
#My Friends : [{'name': 'Alice', 'number': '867-5309'}, {'name': 'Carlos', 'number': '55-5555'}]
print(f'{my_work_buddies.group} : {my_work_buddies.work_buddies}')
#Work Buddies : [{'name': 'Bob', 'number': '555-5555'}, {'name': 'Alice', 'number': '867-5309'}]

# (anotherContactList) to compare and find same name/phone
# # For example:

# # ```python
# # friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
# # work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

# # my_friends_list = ContactList('My Friends', friends)
# # my_work_buddies = ContactList('Work Buddies', work_buddies)

# # friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
# # friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age


# jane = Person("Jane", "Doe", 25)


# print(jane.__dict__)
#'{"first_name": "Jane", "last_name": "Doe", "age": 25}'