---
title: gcore-radar-reports-methodologies
order: 50
displayName: Gcore Radar
published: true
toc:
   --1--Overview: "Overview"
   --1--Top attack origin and countries: "top-attack-origin-and-victim-countries"
   --1--Targeted industries: "targeted-industries"
   --1--Attack characteristics: "attack-characteristics"
   --1--Popular attack types: "popular-attack-types" 
pageTitle: Uncover DDoS Attack Trends with Gcore Radar Reports | Gcore
pageDescription: Learn how Gcore Radar tracks global DDoS attacks, identifies top targeted industries, and predicts future trends using unique methodologies.
---
# Gcore Radar reports methodologies

## Overview 

Gcore Radar is a twice-annual report on the changing DDoS attack landscape based on Gcore’s internal statistics. With a vast, globally distributed network of scrubbing centers around the world, we can track the key characteristics of attacker activity over time. ​In this article, we’ll explain how we collect and process data for all of the information found in Gcore Radar.

## Top attack origin and victim countries

Gcore Radar data shows where an IP address from which an attack was launched is registered. The attacker themself is not necessarily physically located in that country. Pinpointing the exact country from which an attack was coordinated is a daunting task, considering attackers often employ distributed botnets.

At the application layer, this data shows where the attack came from without question. But at the network layer, the legitimacy of the origin IP addresses can be compromised or altered. As a result, we place a higher emphasis on the geographical location of the data centers where the attack packets were initially detected, instead of solely relying on IP addresses for the identification of the source.

When discussing the top countries targeted by attacks, we look at billing details and IP addresses that were the recipients of these assaults. Customers are classified based on their geographical positions, and then the attack traffic is correlated with their respective locations.

## Targeted industries

To determine which industries were most frequently targeted and subjected to the biggest DDoS attacks, we first group all affected customers by industry—information we gather from customers when they register for DDoS Protection to ensure we can offer tailored countermeasures for their industry. Then, we calculate attack frequency and traffic per industry. Comparing across industries gives us metrics on which industries are the biggest targets for DDoS attacks.

## Attack characteristics

The data we share in Gcore Radar includes the duration and power of attacks repelled over a six-month period. We compare this data, as well as the total number of attacks we stopped, with the previous half-year period to evaluate how the threat landscape is evolving. 

Together, these attack characteristics allow us to predict near-future trends and ensure we’re ahead of the curve in what we provide in DDoS Protection.

## Popular attack types

We identify the most popular attack types, like UDP, ICMP, and SYN flood, using a proprietary, automated attack-type recognition feature.