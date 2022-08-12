import { Account } from '../models'

export class AccountModel {
    private static accountModelInstance = new AccountModel();

    private constructor() {}

    static getInstance() : AccountModel {
        return this.accountModelInstance;
    }

    account: Account;

    login(email: string, password: string): Account {
        this.account = new Account();
        console.log(email, password);
        return this.account;
    }
    
    registrati(email: string, password: string): Account {
        this.account = new Account();
        return this.account;
    }
    
    logout() : void {
        this.account = null;
    }
    
    cambiaPsw(psw_new: string) : void {
        this.account.password = psw_new;
    }

}
