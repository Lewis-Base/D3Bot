from pathlib import Path

#txt file should be encoded in ANSI

ATTENDEE_PATH = Path("C:/####################################/D3Bot/v01/attendees_test.txt")
DB_PATH = Path("C:/#################################/D3Bot/v01/real_data.csv")

def clean_name(text):
    text = text.rstrip('\n')
    text = text.replace('?','')
    text = text.replace(':','')
    text = text.split(' ')[0]
    text = text.lower()
    return(text)

def create_attendees_list(txt_file_path):

    attendees_list = []
    
    attendees_list_file = open(txt_file_path, "r")
    for _ in attendees_list_file:
        _ = clean_name(_)
        attendees_list.append(_)
    attendees_list_file.close()
    
    return(attendees_list)

'''
a = create_attendees_list(ATTENDEE_PATH)
print(a)
'''
