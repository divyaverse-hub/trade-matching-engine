# Simple Limit Order Book & Matching Engine

A lightweight Python implementation of a financial order book and trade execution engine built using native data structures.

## Overview
This project simulates how a financial exchange (like stock or crypto markets) matches buy and sell orders. It maintains an active limit order book, sorts incoming bids and asks by price-time priority, and executes trades automatically when prices cross.

## Key Features
- **Order Book State:** Separate structures for managing Buy (Bids) and Sell (Asks) orders.
- **Price-Time Priority:** 
  - Buy orders are prioritized by highest price first.
  - Sell orders are prioritized by lowest price first.
- **Automated Trade Execution:** Matches orders when `Highest Buy Price >= Lowest Sell Price`.
- **Partial Fills:** Handles partial order fulfillment and updates remaining quantities in real-time.

## Project Structure
- `engine.py`: Core logic containing order placement, priority sorting, matching loop, and trade reporting.

## How to Run
1. Make sure Python 3.x is installed on your system.
2. Clone this repository:
   ```bash
   git clone <https://github.com/divyaverse-hub>
