import csv
import re


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def format_number(contacts_list):
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                         r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                         r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_updated = list()
    for contact in contacts_list:
        contact_as_string = ','.join(contact)
        formatted_card = re.sub(number_pattern_raw, number_pattern_new, contact_as_string)
        card_as_list = formatted_card.split(',')
        contacts_list_updated.append(card_as_list)
    return contacts_list_updated


def format_full_name(contacts_list):
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    contacts_list_updated = list()
    for contact in contacts_list:
        contact_as_string = ','.join(contact)
        formatted_card = re.sub(name_pattern_raw, name_pattern_new, contact_as_string)
        card_as_list = formatted_card.split(',')
        contacts_list_updated.append(card_as_list)
    return contacts_list_updated


def join_duplicates(contacts_list):
    for i in contacts_list:
        for k in contacts_list:
            if i[0] == k[0] and i[1] == k[1] and i is not k:
                if i[2] == '':
                    i[2] = k[2]
                if i[3] == '':
                    i[3] = k[3]
                if i[4] == '':
                    i[4] = k[4]
                if i[5] == '':
                    i[5] = k[5]
                if i[6] == '':
                    i[6] = k[6]
    contacts_list_updated = list()
    for contact in contacts_list:
        if contact not in contacts_list_updated:
            contacts_list_updated.append(contact)
    return contacts_list_updated


def write_file(contacts_list):
    with open("phone_book_formatted.csv", "w") as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(contacts_list)


if __name__ == '__main__':
    contacts = read_file('phonebook_raw.csv')
    contacts = format_number(contacts)
    contacts = format_full_name(contacts)
    contacts = join_duplicates(contacts)

    write_file(contacts)
