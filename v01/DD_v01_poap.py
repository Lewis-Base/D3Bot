from pathlib import Path

POAP_LINK_PATH = Path("C:/########################/D3Bot/v01/poap_link_test.txt")



def create_poap_links_list(txt_file_path):

    poap_links_list = []

    poap_links_file = open(txt_file_path, "r")
    for _ in poap_links_file:
        _ = _.rstrip('\n')
        poap_links_list.append(_)
    poap_links_file.close()
    
    return(poap_links_list)

'''
a = create_poap_links_list(POAP_LINK_PATH)
print(a)
'''
