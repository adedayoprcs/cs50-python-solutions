def main():
    fullname = capitalize_fullname("adedayo", "precious", "adedeji")
    print(fullname.title())
    buildperson = build_person("person", "person")
    print(buildperson)

    
    
   
    
def capitalize_name(first_name, last_name):
    """Capitalize full name """
    full_name = f"{first_name} {last_name}"
    print(full_name.title())




def capitalize_fullname(first_name, last_name, middle =""):
    """Capitalize fullname"""
    if middle:
        full_name_ = f"{first_name} {middle} {last_name}"
        return full_name_
    else:
        full_name_ = f"{first_name} {last_name}"
        return full_name_
    
        
def build_person(firstname, lastname, middle=""):
    """Build person """
    if middle:
        person = {"first": firstname, "last": lastname, "middle" : middle} 
    else:
        person = {"first": firstname, "last": lastname,} 
        return person


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person

musician = build_person('jimi', 'hendrix', '50')
print(musician)

main()