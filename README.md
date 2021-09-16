# raffle-bot

This bot will be integrated into Discord with the purpose of tracking activity related to a "discord raffle". The bot will track posts in specific channels related to the raffle (ie. #trial-requests) and will link to the posts or copy the posts into a private channel. The bot will ask for approval from the person in charge of the raffle. If the post is deemed acceptable to be awarded tickets, the bot will add the user (if the user is not already added) to a pinned post and update the amount of tickets the user received for the approved post. The alert post will then be deleted.

## Dependencies

- Python 3
- discord.py library

## Roadmap

- Bot interacts with polls to tally tickets as well
- Potential algorithm for the bot to actually execute the raffle and pick the winner.
