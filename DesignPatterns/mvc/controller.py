from models import Car
import view

def showAll():
    print "Showall"
    #gets list of all Person objects
    car_in_db = Car.getAll()
    #calls view
    return view.showAllView(car_in_db)

def start():
    view.startView()
    input = raw_input()[0].lower()
    print (input=='y')
    if input == 'y':
        return showAll()
    else:
        return view.endView()

if __name__ == "__main__":
    #running controller function
    start()