# Person

## Description
This class represents every living person.

## Parent class
None

## Attributes

* ```first_name```
    * data type: string
    * description: stores the person's first name
* ```last_name```
    * data type: string
    * description: stores the person's last name
* ```year_of_birth```
    * data type: integer
    * description: stores the person's year of birth
* ```gender```
    * data type: string (male/female/notsure)
    * description: stores the person's gender
* ```mood```
    * data type: integer
    * description: stores the level of mood of the person
* ```energy```
    * data type: integer
    * description: stores the level of energy of the person

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
All of the arguments of the class itself.

#### Return value
None


### ```increase_energy```
Increases the ```energy``` level by the object's ```delta``` attribute.

#### Arguments
* ```delta```
  * data_type: integer
  * description: holds the value with what the energy level will be modified.


#### Return value
```delta``` value

### ```increase_mood```
Increases the ```mood``` level by the object's ```delta``` attribute.

#### Arguments
* ```delta```
  * data_type: integer
  * description: holds the value with what the mood level will be modified.


#### Return value
```delta``` value
