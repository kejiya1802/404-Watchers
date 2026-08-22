import os
from dotenv import load_dotenv

load_dotenv()


# --------------------------------------------------
# Application
# --------------------------------------------------

APP_NAME = os.getenv(
    "APP_NAME",
    "404 Watcher"
)

HOST = os.getenv(
    "HOST",
    "127.0.0.1"
)

PORT = int(
    os.getenv(
        "PORT",
        5000
    )
)

DEBUG = os.getenv(
    "DEBUG",
    "True"
).lower() == "true"


# --------------------------------------------------
# Scraper
# --------------------------------------------------

REQUEST_TIMEOUT = int(
    os.getenv(
        "REQUEST_TIMEOUT",
        15
    )
)


# --------------------------------------------------
# Database
# --------------------------------------------------

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "watcher.db"
)


# --------------------------------------------------
# Competitors
# --------------------------------------------------

COMPETITORS = [

    {
        "id": 1,
        "name": "OpenAI",
        "pricing": "https://openai.com/business/pricing/",
        "changelog": "https://openai.com/news/",
        "careers": "https://openai.com/careers/"
    },

    {
        "id": 2,
        "name": "Anthropic",
        "pricing": "https://www.anthropic.com/pricing",
        "changelog": "https://www.anthropic.com/news",
        "careers": "https://www.anthropic.com/careers"
    },

    {
        "id": 3,
        "name": "Google Cloud",
        "pricing": "https://cloud.google.com/pricing",
        "changelog": "https://cloud.google.com/release-notes",
        "careers": "https://www.google.com/about/careers/"
    },

    {
        "id": 4,
        "name": "Microsoft Azure",
        "pricing": "https://azure.microsoft.com/en-us/pricing/",
        "changelog": "https://azure.microsoft.com/en-us/updates/",
        "careers": "https://careers.microsoft.com/"
    },

    {
        "id": 5,
        "name": "AWS",
        "pricing": "https://aws.amazon.com/pricing/",
        "changelog": "https://aws.amazon.com/new/",
        "careers": "https://www.amazon.jobs/"
    },

    {
        "id": 6,
        "name": "GitHub",
        "pricing": "https://github.com/pricing",
        "changelog": "https://github.blog/changelog/",
        "careers": "https://www.github.careers/"
    },

    {
        "id": 7,
        "name": "GitLab",
        "pricing": "https://about.gitlab.com/pricing/",
        "changelog": "https://about.gitlab.com/releases/",
        "careers": "https://about.gitlab.com/jobs/"
    },

    {
        "id": 8,
        "name": "Vercel",
        "pricing": "https://vercel.com/pricing",
        "changelog": "https://vercel.com/changelog",
        "careers": "https://vercel.com/careers"
    },

    {
        "id": 9,
        "name": "Cloudflare",
        "pricing": "https://www.cloudflare.com/plans/",
        "changelog": "https://developers.cloudflare.com/changelog/",
        "careers": "https://www.cloudflare.com/careers/"
    },

    {
        "id": 10,
        "name": "MongoDB",
        "pricing": "https://www.mongodb.com/pricing",
        "changelog": "https://www.mongodb.com/docs/release-notes/",
        "careers": "https://www.mongodb.com/careers"
    },

    {
        "id": 11,
        "name": "Datadog",
        "pricing": "https://www.datadoghq.com/pricing/",
        "changelog": "https://www.datadoghq.com/product-updates/",
        "careers": "https://careers.datadoghq.com/"
    },

    {
        "id": 12,
        "name": "Snowflake",
        "pricing": "https://www.snowflake.com/en/pricing/",
        "changelog": "https://www.snowflake.com/en/releases/",
        "careers": "https://careers.snowflake.com/"
    },

    {
        "id": 13,
        "name": "Stripe",
        "pricing": "https://stripe.com/pricing",
        "changelog": "https://stripe.com/blog",
        "careers": "https://stripe.com/jobs"
    },

    {
        "id": 14,
        "name": "Twilio",
        "pricing": "https://www.twilio.com/en-us/pricing",
        "changelog": "https://www.twilio.com/en-us/changelog",
        "careers": "https://www.twilio.com/en-us/company/jobs"
    },

    {
        "id": 15,
        "name": "HubSpot",
        "pricing": "https://www.hubspot.com/pricing",
        "changelog": "https://www.hubspot.com/product-updates",
        "careers": "https://www.hubspot.com/careers"
    },

    {
        "id": 16,
        "name": "Notion",
        "pricing": "https://www.notion.com/pricing",
        "changelog": "https://www.notion.com/releases",
        "careers": "https://www.notion.com/careers"
    },

    {
        "id": 17,
        "name": "Slack",
        "pricing": "https://slack.com/pricing",
        "changelog": "https://slack.com/release-notes",
        "careers": "https://slack.com/careers"
    },

    {
        "id": 18,
        "name": "Atlassian",
        "pricing": "https://www.atlassian.com/software/pricing",
        "changelog": "https://www.atlassian.com/software/jira/whats-new",
        "careers": "https://www.atlassian.com/company/careers"
    },

    {
        "id": 19,
        "name": "Docker",
        "pricing": "https://www.docker.com/pricing/",
        "changelog": "https://www.docker.com/blog/",
        "careers": "https://www.docker.com/career-opportunities/"
    },

    {
        "id": 20,
        "name": "Redis",
        "pricing": "https://redis.io/pricing/",
        "changelog": "https://redis.io/blog/",
        "careers": "https://redis.io/careers/"
    },

    {
        "id": 21,
        "name": "Elastic",
        "pricing": "https://www.elastic.co/pricing",
        "changelog": "https://www.elastic.co/guide/en/elastic-stack/current/release-notes.html",
        "careers": "https://www.elastic.co/about/careers"
    },

    {
        "id": 22,
        "name": "DigitalOcean",
        "pricing": "https://www.digitalocean.com/pricing",
        "changelog": "https://docs.digitalocean.com/release-notes/",
        "careers": "https://www.digitalocean.com/careers"
    },

    {
        "id": 23,
        "name": "Heroku",
        "pricing": "https://www.heroku.com/pricing",
        "changelog": "https://devcenter.heroku.com/changelog",
        "careers": "https://www.heroku.com/careers"
    },

    {
        "id": 24,
        "name": "Linear",
        "pricing": "https://linear.app/pricing",
        "changelog": "https://linear.app/changelog",
        "careers": "https://linear.app/careers"
    },

    {
        "id": 25,
        "name": "Figma",
        "pricing": "https://www.figma.com/pricing/",
        "changelog": "https://www.figma.com/whats-new/",
        "careers": "https://www.figma.com/careers/"
    }
]


MONITORED_PAGES = [
    "pricing",
    "changelog",
    "careers"
]