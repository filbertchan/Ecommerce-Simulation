{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Could not import SolaraViz. If you need it, install with 'pip install --pre mesa[viz]'\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/bengbeng/Ecommerce-Simulation/mesa/lib/python3.10/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html\n",
      "  from .autonotebook import tqdm as notebook_tqdm\n"
     ]
    }
   ],
   "source": [
    "import mesa\n",
    "\n",
    "# agents.py\n",
    "\n",
    "class Supplier:\n",
    "    def __init__(self, supplier_id, name, products):\n",
    "        self.supplier_id = supplier_id  # Unique ID for the supplier\n",
    "        self.name = name  # Name of the supplier\n",
    "        self.products = products  # List of products offered by the supplier\n",
    "    \n",
    "    def supply_product(self, product):\n",
    "        \"\"\"Simulate supplying a product to the seller.\"\"\"\n",
    "        print(f\"Supplying {product} to the seller.\")\n",
    "        self.products.append(product)\n",
    "\n",
    "    def get_products(self):\n",
    "        \"\"\"Return the list of products the supplier offers.\"\"\"\n",
    "        return self.products\n",
    "\n",
    "\n",
    "class Seller:\n",
    "    def __init__(self, seller_id, name, inventory, marketing_strategies):\n",
    "        self.seller_id = seller_id  # Unique ID for the seller\n",
    "        self.name = name  # Name of the seller\n",
    "        self.inventory = inventory  # List of products the seller has in stock\n",
    "        self.marketing_strategies = marketing_strategies  # List of marketing strategies\n",
    "\n",
    "    def advertise(self):\n",
    "        \"\"\"Simulate advertising the products using the seller's marketing strategies.\"\"\"\n",
    "        print(f\"{self.name} is advertising using the following strategies: {', '.join(self.marketing_strategies)}\")\n",
    "\n",
    "    def sell_product(self, product):\n",
    "        \"\"\"Simulate selling a product.\"\"\"\n",
    "        if product in self.inventory:\n",
    "            self.inventory.remove(product)\n",
    "            print(f\"{self.name} sold {product}.\")\n",
    "        else:\n",
    "            print(f\"{product} is out of stock for {self.name}.\")\n",
    "\n",
    "\n",
    "class Consumer:\n",
    "    def __init__(self, consumer_id, name, demographics, preferences):\n",
    "        self.consumer_id = consumer_id  # Unique ID for the consumer\n",
    "        self.name = name  # Name of the consumer\n",
    "        self.demographics = demographics  # Demographics of the consumer (e.g., age, location)\n",
    "        self.preferences = preferences  # Consumer's product preferences\n",
    "    \n",
    "    def browse_products(self, available_products):\n",
    "        \"\"\"Simulate browsing products and choosing one based on preferences.\"\"\"\n",
    "        print(f\"{self.name} is browsing products...\")\n",
    "        for product in available_products:\n",
    "            if product in self.preferences:\n",
    "                print(f\"{self.name} is interested in {product}.\")\n",
    "                return product  # Returns the first preferred product\n",
    "        return None\n",
    "\n",
    "    def make_purchase(self, product):\n",
    "        \"\"\"Simulate making a purchase.\"\"\"\n",
    "        print(f\"{self.name} purchased {product}.\")\n",
    "\n",
    "\n",
    "class Banner:\n",
    "    def __init__(self, banner_id, location, content):\n",
    "        self.banner_id = banner_id  # Unique ID for the banner\n",
    "        self.location = location  # Where the banner is placed (e.g., homepage, product page)\n",
    "        self.content = content  # The content shown on the banner\n",
    "    \n",
    "    def display(self):\n",
    "        \"\"\"Simulate displaying the banner.\"\"\"\n",
    "        print(f\"Displaying banner at {self.location} with content: {self.content}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "mesa",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
