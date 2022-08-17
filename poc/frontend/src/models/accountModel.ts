import { Account } from '../models'

export class AccountModel {
    private static accountModelInstance : AccountModel = AccountModel.construct_session();

    private static construct_session() : AccountModel {
        let result : AccountModel = JSON.parse(window.sessionStorage.getItem('AccountModel'));
        if(!result) {
            result = new AccountModel();
            window.sessionStorage.setItem('AccountModel', JSON.stringify(result));
        } else {
            result.__proto__ = AccountModel.prototype; // errore del compilatore don't worry
        }
        return result;
    }

    private constructor() { }

    static getInstance() : AccountModel {
        return this.accountModelInstance;
    }

    account: Account;
    
    login(email: string, password: string, remember: boolean): Account {
        this.account = new Account();
        this.account.accountname = "nome default";
        this.account.email = email;
        this.account.password = password;
        this.account.preference = true;
        this.save_to_session();
        return this.account;
    }
    
    registrati(email: string, password: string): Account {
        this.account = new Account();
        this.account.accountname = "nome default";
        this.account.email = email;
        this.account.password = password;
        this.account.preference = true;        
        this.save_to_session();
        return this.account;
    }
    
    logout() : void {
        this.account = undefined;
        this.save_to_session();
    }
    
    cambiaPsw(psw_new: string) : void {
        this.account.password = psw_new;
        this.save_to_session();
    }

    cambiaPreferenza(newPref: boolean) {
        this.account.preference = newPref;
        this.save_to_session();
    }

    private save_to_session() {
        window.sessionStorage.setItem('AccountModel', JSON.stringify(this));
    }

}
