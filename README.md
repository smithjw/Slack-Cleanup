# Slack-Cleanup

`slackCleanup.py` is primarily designed as a tool to assist with the bulk renaming of Slack channels in your Team. By passing it sever command line options, you can activate different functionality.

To run `slackCleanup.py` you will need to pass a Slack Token with the `-t | --token` flag. You can generate a token [here](https://api.slack.com/custom-integrations/legacy-tokens). Following the `-t` flag you can then either pass it the `-l | --list`, `-r | --rename`, or `-a | --archive` flags.

### Listing Channels
`-l | --list` will write all public Slack channels to a CSV file with the following fields:

- Channel ID
- Channel Name
- New Channel Name (This field is left blank)
- To Archive
- Creator
- Email
- Members
- Purpose
- Topic

### Renaming Channels
`-r | --rename`

Once you have filled in the `New Channel Name` field, you can run `slackCleanup.py` with the `-r` flag. This will work through the CSV renaming all channels in the CSV to the value in the `New Channel Name`.

### Archiving Channels
`-a | --archive`

Running `slackCleanup.py` with the `-a` flag will look for a column in "Channel List.csv" in the same folder as this script named "To Archive". If you would like to pick from your own csv, please use the `-f | --file` flag. The archive function will work through the CSV archiving all channels listed in the CSV where there is any value in the "To Archive" column.

### Flags

- `-l | --list` - Create a CSV list of all Slack channels
- `-r | --rename` - Rename Slack channels based on a CSV
- `-a | --archive` - Archive Slack channels based on a CSV
- `-t | --token` - Stores the Slack API token needed to run this script
- `-f | --file` - Specify the name of the file to be used

## Enjoy
