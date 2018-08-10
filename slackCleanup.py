#!/usr/bin/env python3

from slackclient import SlackClient

import csv
import json
import argparse

outputFile = 'channelList.csv'

parser = argparse.ArgumentParser(description='Command line options for this script')
parser.add_argument('-l', '--list', dest='command', action='store_const', const='list', help='Create a CSV list of all Slack channels')
parser.add_argument('-r', '--rename', dest='command', action='store_const', const='rename', help='Rename Slack channels based on a CSV')
parser.add_argument('-t', '--token', help='Stores the Slack API token needed to run this script')
args = parser.parse_args()

sc = SlackClient(args.token)

def listChannels():
    channelListRaw = sc.api_call('channels.list', exclude_archived=True)
    slackChannelData = channelListRaw['channels']
    length_data = len(slackChannelData)

    # Write the title row of the CSV
    dataToFile = open(outputFile, 'w', newline='')
    csvWriter = csv.writer(dataToFile, delimiter=',')
    csvWriter.writerow(['Channel ID', 'Channel Name', 'New Channel Name', 'Creator', 'Email','Members', 'Purpose', 'Topic'])

    for i in range(0, length_data):

        sd = slackChannelData[i]

        # Here's where we get the fields we want to push into the CSV
        id = sd['id']
        name = sd['name']
        members = sd['num_members']
        purpose = sd['purpose']['value']
        topic = sd['topic']['value']
        creator = sd['creator']

        # Making a second call to the API to determine the name and email of the channel creator
        userInfoRaw = sc.api_call('users.info', user=creator)
        userData = userInfoRaw['user']
        creator = userData['profile']['real_name']
        email = userData['profile']['email']

        print(f'Writing channel with ID {id} and named {name} to CSV')
        csvWriter.writerow([id, name, '', creator, email, members, purpose, topic])

        # Uncomment the following lines for testing purposes
        # new_name = name + '_test'
        # csvWriter.writerow([id, name, new_name, members, purpose, topic])
    dataToFile.close()

def renameChannels():
    # For information on the channels.rename method, see this Slack API doc https://api.slack.com/methods/channels.rename
    with open(outputFile, newline='') as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f'Renaming channel with ID {row['Channel ID']} from {row['Channel Name']} to {row['New Channel Name']}')
            sc.api_call(
                'channels.rename',
                channel=row['Channel ID'],
                name=row['New Channel Name'],
                validate=True
            )

def main():
    if args.token == None:
        print('Please pass the Slack API token to this app with the '-t' flag')
    else:
        if args.command == 'list':
            print('Downloading Slack channel list into', outputFile)
            listChannels()
        elif args.command == 'rename':
            print('Renaming Slack channels according to', outputFile)
            renameChannels()

main()
