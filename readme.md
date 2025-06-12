# ClickAndShare

**ClickAndShare** is a Django-based web application that allows users to generate shareable links tied to user-submitted content. Each link is associated with an expiration timestamp, after which the content becomes inaccessible. This project is ideal for securely sharing time-sensitive information or notes.

## Overview

ClickAndShare provides a lightweight interface to:

- Create temporary, user-defined content links.
- Set an expiration time for each message.
- View content until the link's expiration time.
- Auto-generate link identifiers if not manually provided.

## Key Features

- **Time-Based Expiration:**  
  Each link becomes inactive after the specified datetime, ensuring content privacy.

- **Custom or Random Identifiers:**  
  Users can enter a custom identifier for the link or allow the system to generate a random one.

- **Minimalistic Interface:**  
  Simple form-driven design for creating and viewing messages.

- **Time-Aware Comparisons:**  
  Uses timezone-aware datetime comparison to avoid inconsistencies across systems.

## Use Cases

- Sending time-sensitive messages or reminders  
- Sharing expiring links for events or announcements  
- Creating ephemeral messages during online assessments or timed instructions  


## Technology Stack

- **Framework**: Django (Python)
- **Frontend**: HTML, Bootstrap
- **Database**: Mariadb 
- **Timezone Handling**: `django.utils.timezone` for reliable datetime processing