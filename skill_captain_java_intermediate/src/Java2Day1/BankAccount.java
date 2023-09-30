package Java2Day1;

public class BankAccount {
    //instance variables
   private int accountNumber;
   private String accountName;
   private double accountBalance;

   public BankAccount(int accountNumber, String accountName, double accountBalance){
       this.accountNumber = accountNumber;
       this.accountName = accountName;
       this.accountBalance = accountBalance;
    }
    public void withdrawMoney(double amount){
       accountBalance = accountBalance - amount;
    }
    public void depositMoney(double amount){
        accountBalance = accountBalance + amount;
    }
    //print the output
    public String toString(){
       return "Account Number: "+ accountNumber + "\n" +
               "Account Name: " + accountName + "\n" +
               "Account Balance : " + accountBalance;
    }
}
