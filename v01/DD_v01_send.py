from pathlib import Path

def create_send_list(poap_links_list, attendee_list, db_list):

    send_list = []

    k = 0

    for i in attendee_list:

        for j in db_list:

            if i.lower() == (((j[1]).split())[0]).lower():

                send_list.append([j[3], poap_links_list[k]])

        k += 1

    return(send_list)
