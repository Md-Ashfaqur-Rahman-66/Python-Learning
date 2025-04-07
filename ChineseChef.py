from Chef import Chef
class ChineseChef(Chef):

    def make_special_dish(self):                #overrighting the 'make_special_dish' function of 'Chef' class
        print("The Chef makes orange Chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")