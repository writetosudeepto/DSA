def new_menu(item_list):
    #This is the Menu list we want to update
    Menu = [['Sweet_Corn_Soup', 300.0], ['Cream_of_Tomato_Soup', 100.0], ['Bacon_and_Cheese', 150.0], ['Honey_Mustard', 230.0], ['Hot_Coffee', 50.0], ['Cold_Coffee', 50.0], ['Egg_Sandwiches', 130.0], ['Tacos', 400.0]
    #Write your code here

    for item in Menu:
        if item[0] in increase_list:
            item[1] += item[1]*10/100
    
    return Menu