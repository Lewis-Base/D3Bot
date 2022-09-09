def the_list(url):
    
    from DD_v01_csv import create_db_list
    from DD_v01_notion_scrape import scrape
    from DD_v01_attendees import create_attendees_list
    from DD_v01_poap import create_poap_links_list
    from DD_v01_send import create_send_list

    import csv
    from pathlib import Path

    DB_PATH = Path("C:/######################/D3Bot/v01/test_data.csv")
    POAP_LINK_PATH = Path("C:/###################/D3Bot/v01/poap_link_test.txt")

    notion_page = url

    ATTENDEE_PATH = Path(scrape(notion_page))

    poap_link_list = create_poap_links_list(POAP_LINK_PATH)
    attendee_list = create_attendees_list(ATTENDEE_PATH)
    db_list = create_db_list(DB_PATH)

    send_list = create_send_list(poap_link_list,attendee_list,db_list)

    return (send_list)
