import csv

def nullize(string):
    if string == '\N' or string == '':
        return None
    else:
        return string

def writeRows(data, base_csv_name):
	with open('../CSV/' + base_csv_name + 'CLEAN.csv','w') as out:
		csv_out = csv.writer(out, delimiter='\t')
		for tuple in data:
			csv_out.writerow(tuple)
	

def booleanize(string):
    if string.lower() == 'no':
        return False
    elif string.lower() == 'yes':
        return True
    else:
        return string

def booleanize2(string):
	if string.lower() == 'no':
		return 0
	if string.lower() == 'yes':
		return 1
	else:
		return string

def storyLengthFormat(story_length):
    story_length_formats = ['nv', 'ss', 'jvn', 'nvz', 'sf']
    if story_length in story_length_formats:
        return story_length
    else:
        return None

def storyTypeFormat(story_type):
    story_type_formats = ['ANTHOLOGY', 'BACKCOVERART', 'COLLECTION', 'COVERART', 'INTERIORART', 'EDITOR', 'ESSAY', 'INTERVIEW', 'NOVEL', 'NONFICTION', 'OMNIBUS', 'POEM', 'REVIEW', 'SERIAL', 'SHORTFICTION', 'CHAPBOOK']
    if story_type in story_type_formats:
        return story_type
    else:
        return None

def publicationTypeFormat(publication_type):
    publication_type_formats = ['ANTHOLOGY', 'COLLECTION', 'MAGAZINE', 'NONFICTION', 'NOVEL', 'OMNIBUS', 'FANZINE', 'CHAPBOOK']
    if publication_type in publication_type_formats:
        return publication_type
    else:
        return None
