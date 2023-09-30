package Java2Day1;

import Java2Day1.BankAccount;

public class Main {
    public static void main(String[] args){
        BankAccount myAccount = new BankAccount(189009, "Berna ", 12500);
        myAccount.withdrawMoney(10.5);
        myAccount.withdrawMoney(10.5);
        myAccount.depositMoney(20.10);
        System.out.println(myAccount);
    }
}