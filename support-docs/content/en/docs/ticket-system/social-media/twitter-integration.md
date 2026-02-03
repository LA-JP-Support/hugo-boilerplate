---
title: "How to Import Tweets Through Twitter Integration"
date: 2026-01-30
lastmod: 2026-01-30
draft: false
translationKey: "twitter-integration"
description: "LiveAgent's Twitter support channel can import tweets that match specific search criteria by converting them into tickets."
keywords: ["Twitter", "integration", "LiveAgent", "Agent", "account"]
category: "ticket-system/social-media"
---
## How to Import Tweets into Support Tickets with Twitter Channel

### Twitter Integration Overview
LiveAgent's Twitter support channel can import tweets that match specific search criteria by converting them into tickets.

### Twitter Integration Setup

![Twitter Integration Setup Screen](/liveagent/scripts/file.php?view=Y&file=d4e94b4f72b1ac282b930c8bdc2ae98f)

### Adding Search Queries and Language Settings
When you add a new query, a field will be added. Enter the keywords you want to search for in that field. Also, when searching for Japanese tweets, select "Japanese" in the "Language" option.

### About Twitter Search API
Twitter's search API is available for tweet searches. For more details, please refer to [Twitter's official page](https://dev.twitter.com/rest/public/search) (in English).

### Search Query Examples and Search Results

| Search Term | Searched Tweets |
|-------------|-----------------|
| twitter search | Searches for tweets containing both twitter and search. This is the basic operation |
| "happy hour" | Searches for tweets that exactly match "happy hour" |
| love OR hate | Searches for tweets containing love or hate (or both) |
| beer -root | Searches for tweets containing beer but excluding root |
| #haiku | Searches for tweets containing hashtag #haiku |
| from:twitterapi | Searches for tweets sent from user @twitterapi |
| to:twitterapi | Searches for tweets sent to user @twitterapi |
| @mashable | Searches for tweets related to the mashable account |
| superhero since:2010-12-27 | Searches for tweets containing superhero from December 27, 2010 (year-month-day) |
| ftw until:2010-12-27 | Searches for tweets containing ftw until December 27, 2010 |
| movie -scary | Searches for tweets containing movie but not containing scary |
| flight :( | Searches for tweets containing flight and the symbol :( (" :) " and " :( " are emoticons ;p ) |
| hilarious filter:links | Searches for tweets containing hilarious with link URLs |
| news source:twitterfeed | Searches for tweets containing news that were posted using TwitterFeed |

### Important Notes
※These search APIs may be subject to specification changes on Twitter's side.