#The function has one argument, which is the name of the input file
def collect_number_5_messages(name_of_the_input_file):
    content=""
    #Both 'location_of_message_number' and 'const' were chosen empirically
    location_of_message_number=35
    const=15

    file_in = open(name_of_the_input_file,'r')

    #Collecting all the number 5 messages and appending it to the content variable
    for line in file_in.readlines():
        if(line[location_of_message_number]=='5' and line[location_of_message_number-1]==','):
            content=content+line[location_of_message_number-const:]
        
    file_in.close

    #Creating file that will cotain all the number 5 messages
    file_out = open('AIS_number_5_messages','w')
    file_out.write(content)
    file_out.close