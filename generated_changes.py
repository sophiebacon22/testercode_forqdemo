 Here is the code to rewrite the wallet class in PHP:

```php
<?php

class Wallet {

  private $balance;

  public function __construct($initialBalance = 0) {
    $this->balance = $initialBalance;
  }

  public function getBalance() {
    return $this->balance;
  }

  public function deposit($amount) {
    if ($amount > 0) {
      $this->balance += $amount;
    }
  }

  public function withdraw($amount) {
    if ($amount > 0 && $amount <= $this->balance) {
      $this->balance -= $amount;
    }
  }

}
```

The key aspects are:

- The class is named Wallet
- There is a private $balance property to store the current balance 
- A constructor to set the initial balance
- getBalance() method to retrieve the current balance
- deposit() method to add money to the balance
- withdraw() method to remove money from the balance, if there are sufficient funds

This implements the basic logic and operations for a wallet class in PHP. Let me know if you need any clarification or have additional requirements to implement!