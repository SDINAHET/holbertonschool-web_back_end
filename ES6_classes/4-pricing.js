// 4-pricing.js

import Currency from './3-currency';  // Importing the Currency class

class Pricing {
  constructor(amount, currency) {
    // Assign the constructor parameters to private attributes
    this._amount = amount;
    this._currency = currency;
  }

  // Getter for 'amount'
  get amount() {
    return this._amount;
  }

  // Setter for 'amount'
  set amount(value) {
    this._amount = value;
  }

  // Getter for 'currency'
  get currency() {
    return this._currency;
  }

  // Setter for 'currency'
  set currency(value) {
    this._currency = value;
  }

  // Method to display full price in the format: amount currency_name (currency_code)
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Static method to convert the price based on the given conversion rate
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}

export default Pricing;
