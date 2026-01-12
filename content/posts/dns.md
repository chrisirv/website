---
title: "DNS Hosting using Cloudflare"
date: 2026-01-11
draft: false
description: "Cloudflare offers free DNS and low cost domain name registration providing a rock-solid foundation for automation."
tags: ["Cloudflare", "DNS", "Infrastructure", "Low cost"]
---

### What is Cloudflare?

- [Cloudflare](https://www.cloudflare.com/application-services/products/dns/) is an authoritative DNS service that offers fast response times (averaging ~11ms) and redundancy for free bundled with various basic security protections for your site and being API first is good for automation.

#### The Free Plan:

The Free plan is **$0/month** and includes everything a hobbyist or tester needs:

- **Global Anycast Network:** Your DNS records are replicated across 330+ cities for instant lookups.
- **Unmetered DDoS Protection:** Shields your domain from attacks at the DNS level.
- **DNSSEC:** Adds a cryptographic layer to prevent DNS spoofing and "man-in-the-middle" attacks.
- **Proxied Records (The "Orange Cloud"):** Masks your real server IP and provides free SSL and CDN caching automatically.
- **Cloudflare Pages Integration:** Seamlessly connects your Hugo site to your domain without manual CNAME headaches.

### Understanding Domain Registration Costs

For any website, it is usually cheaper to move your domain and is the only mandatory recurring cost or the **Domain Registration Fee** of about $8.00 for a typical .com per year.

*Note: Cloudflare also includes **WHOIS Privacy Protection** for free, which usually costs an extra $10-$15/year at other registrars.*

### How to get started:

1. Create a free account at Cloudflare.com and click **Add a Site**.
2. Enter your domain (e.g., `deft.technology`) and select the **Free $0** plan.
3. Cloudflare will scan your existing records. Review them and click continue.
4. Log into your domain registrar (e.g., Namecheap or Porkbun) and replace your old nameservers with the two provided by Cloudflare.
5. Once "Active," toggle the **Proxy status** to "Proxied" for your website records to enable the CDN and SSL features.

### Prompt used to get started on Google Gemini (copy-friendly):

```text
I am moving my domain's DNS to Cloudflare to support my Hugo site. Act as a Network Engineer. Explain the difference between 'Proxied' and 'DNS Only' modes in the Cloudflare dashboard. Also, help me generate the specific MX and SPF records needed to ensure my email doesn't go to spam after the move.
