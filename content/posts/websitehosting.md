---
title: "Website Hosting using Render"
date: 2026-01-11
draft: false
description: "Render is a good free choice for website hosting."
tags: ["Render", "Hosting", "Deployment", "Free"]
---

### What:

- Render https://www.render.com is a good choice for hosting static sites like this one.

#### The Free Hobby Plan:

The Hobby plan is free ($0/month) and includes several useful features:

- **Custom domains:** Use your own brand.
- **Global CDN:** Fast delivery worldwide.
- **Automatic SSL:** Secure by default.
- **Continuous deployment:** Updates automatically on each GitHub push.

### How to get started:

1. Create a GitHub repository and push your Hugo project.
2. Create a new Static Site on Render and connect the repository.
3. Set the **Build Command** to `hugo`.
4. Set the **Publish Directory** to `public`.
5. Add a custom domain if desired.

### Prompt used to get started on Google Gemini (copy-friendly):

```text
I have a local Hugo project ready. Act as a DevOps Engineer and guide me through pushing this to a new GitHub repository and deploying it to Render. Specifically, tell me the exact 'Build Command' and 'Publish Directory' required in the Render dashboard for a Hugo site to ensure the build doesn't fail.
```
