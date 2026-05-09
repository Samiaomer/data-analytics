# Create dictionary with contact information
contact_info = {
    "name": "Samia Omer",
    "address": "123 Maple Street",
    "city": "Cambridge",
    "state": "MA",
    "zip": "02139"
}

# Format and print mailing address using a multi-line f-string
print(f"""
{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

# contact_info dictionary (name removed)
contact_info = {
    "address": "123 Maple Street",
    "city": "Cambridge",
    "state": "MA",
    "zip": "02139"
}

# full_name dictionary
full_name = {
    "first_name": "Samia",
    "last_name": "Omer"
}

# add honorific using update()
full_name.update({
    "honorific": "Ms."
})

# add full_name into contact_info
contact_info.update({
    "full_name": full_name
})

# print formatted mailing address
print(f"""
{contact_info['full_name']['honorific']} {contact_info['full_name']['first_name']} {contact_info['full_name']['last_name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")