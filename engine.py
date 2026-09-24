# Simple Order Book & Matching Engine

class OrderBook:
    def __init__(self):
        self.buy_orders = []   # List of dicts: [{'trader': 'Alice', 'qty': 10, 'price': 150}]
        self.sell_orders = []  # List of dicts: [{'trader': 'Bob', 'qty': 10, 'price': 148}]
        self.trade_history = []

    def add_order(self, trader, side, qty, price):
        order = {
            "trader": trader,
            "side": side.upper(),
            "qty": qty,
            "price": price
        }
        
        if order["side"] == "BUY":
            self.buy_orders.append(order)
            # Sort Buy orders: Highest price first
            self.buy_orders.sort(key=lambda x: x["price"], reverse=True)
        elif order["side"] == "SELL":
            self.sell_orders.append(order)
            # Sort Sell orders: Lowest price first
            self.sell_orders.sort(key=lambda x: x["price"])

        # Try matching trades whenever a new order enters
        self.match_orders()

    def match_orders(self):
        # Match while top Buy price >= top Sell price
        while self.buy_orders and self.sell_orders:
            highest_buy = self.buy_orders[0]
            lowest_sell = self.sell_orders[0]

            if highest_buy["price"] >= lowest_sell["price"]:
                # Determine how many shares can be traded
                traded_qty = min(highest_buy["qty"], lowest_sell["qty"])
                execution_price = lowest_sell["price"]  # Passive price

                # Record the trade
                trade = {
                    "buyer": highest_buy["trader"],
                    "seller": lowest_sell["trader"],
                    "qty": traded_qty,
                    "price": execution_price
                }
                self.trade_history.append(trade)

                # Update remaining quantities
                highest_buy["qty"] -= traded_qty
                lowest_sell["qty"] -= traded_qty

                # Remove fully filled orders
                if highest_buy["qty"] == 0:
                    self.buy_orders.pop(0)
                if lowest_sell["qty"] == 0:
                    self.sell_orders.pop(0)
            else:
                break  # No match possible right now

    def display_summary(self):
        print("=== EXECUTED TRADES ===")
        for t in self.trade_history:
            print(f"Trade: {t['buyer']} bought {t['qty']} shares from {t['seller']} at ${t['price']}")
        
        print("\n=== UNMATCHED BUY ORDERS ===")
        for b in self.buy_orders:
            print(f"{b['trader']} wants {b['qty']} shares at ${b['price']}")
            
        print("\n=== UNMATCHED SELL ORDERS ===")
        for s in self.sell_orders:
            print(f"{s['trader']} offers {s['qty']} shares at ${s['price']}")

# --- TESTING THE ENGINE ---
if __name__ == "__main__":
    book = OrderBook()

    # Simulate incoming orders
    print("Submitting Orders...\n")
    book.add_order("Alice", "BUY", 10, 150)   # Alice wants 10 @ $150
    book.add_order("Bob", "SELL", 5, 148)    # Bob sells 5 @ $148 (Match!)
    book.add_order("Charlie", "SELL", 10, 152) # Charlie sells 10 @ $152 (No match)
    book.add_order("David", "BUY", 8, 149)    # David wants 8 @ $149 (No match)
    book.add_order("Eve", "SELL", 5, 149)     # Eve sells 5 @ $149 (Matches with Alice's remaining 5!)

    # Show Final State
    book.display_summary()