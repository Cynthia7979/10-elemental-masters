from reality import *

Act(1, 'Unexplained events', (
    Scene(1, 'The jail escapee', "May 27, 1999 at 4:07 PM UTC", 54, 52, (
        Action('Knucles', 'glides north', quantity=Quantity(800, 'miles per hour'), features=('1500 feet above Lake Sakakawea', 'following Highway 83')),
        Entity('small thunderstorm', features=('visible', 'to the south')),
        Entity('sky', children_items=(
            Entity('sky', dimensions=Rational(3, 8), features=('scattered with cirrus clouds',)),
            Entity('sky', dimensions=Rational(1, 8), features=('scattered with altostratus clouds',))
        )),
        Action('wind', '', quantity=Quantity(15, 'miles per hour')),
        Action('wind', 'gusts', quantity=Quantity(20, 'miles per hour')),
        Entity('patches of snow', features=('small', 'in ditches', 'visible', 'hard to see')),
        Action('credits', 'display on screen'),
        Pause(40),
        Character(
            'Knucles', dimensions=(Quantity(25+Rational(1, 3), 'inches'), Quantity(4, 'inches'), Quantity(2.5, 'inches')), 
            features=('resembles a human with differences', 'neither male or female'), children_items=(
                Entity('fur', color='FFA000E0', dimensions=Quantity(Rational(3, 4), 'inch'), position='entire body'),
                Entity('hands', dimensions=Quantity(140, 'percent')),
                Entity('haze', color='FFA0FF00', dimensions=Quantity(Rational(1, 2), 'millimeter'), position='pupil border', features=('reflective', 'glittery')),
                Entity('mouth', dimensions=Rational(2, 3))                
        ))
    ))
))
