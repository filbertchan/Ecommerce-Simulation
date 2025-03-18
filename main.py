# agents.py

class Supplier:
    def __init__(self, supplier_id, name, products):
        self.supplier_id = supplier_id  # Unique ID for the supplier
        self.name = name  # Name of the supplier
        self.products = products  # List of products offered by the supplier
    
    def supply_product(self, product):
        """Simulate supplying a product to the seller."""
        print(f"Supplying {product} to the seller.")
        self.products.append(product)

    def get_products(self):
        """Return the list of products the supplier offers."""
        return self.products


class Seller:
    def __init__(self, seller_id, name, inventory, marketing_strategies):
        self.seller_id = seller_id  # Unique ID for the seller
        self.name = name  # Name of the seller
        self.inventory = inventory  # List of products the seller has in stock
        self.marketing_strategies = marketing_strategies  # List of marketing strategies

    def advertise(self):
        """Simulate advertising the products using the seller's marketing strategies."""
        print(f"{self.name} is advertising using the following strategies: {', '.join(self.marketing_strategies)}")

    def sell_product(self, product):
        """Simulate selling a product."""
        if product in self.inventory:
            self.inventory.remove(product)
            print(f"{self.name} sold {product}.")
        else:
            print(f"{product} is out of stock for {self.name}.")


class Consumer:
    def __init__(self, consumer_id, name, demographics, preferences):
        self.consumer_id = consumer_id  # Unique ID for the consumer
        self.name = name  # Name of the consumer
        self.demographics = demographics  # Demographics of the consumer (e.g., age, location)
        self.preferences = preferences  # Consumer's product preferences
    
    def browse_products(self, available_products):
        """Simulate browsing products and choosing one based on preferences."""
        print(f"{self.name} is browsing products...")
        for product in available_products:
            if product in self.preferences:
                print(f"{self.name} is interested in {product}.")
                return product  # Returns the first preferred product
        return None

    def make_purchase(self, product):
        """Simulate making a purchase."""
        print(f"{self.name} purchased {product}.")


class Banner:
    def __init__(self, banner_id, location, content):
        self.banner_id = banner_id  # Unique ID for the banner
        self.location = location  # Where the banner is placed (e.g., homepage, product page)
        self.content = content  # The content shown on the banner
    
    def display(self):
        """Simulate displaying the banner."""
        print(f"Displaying banner at {self.location} with content: {self.content}")
