package main

import "fmt"
import "time"
import "math/rand"

type Account struct {
	id      int
	balance float64
	owners  []Client
	access  chan bool
}

type Client struct {
	id   int
	name string
}

func (account *Account) isOwner(client *Client) bool {
	for _, owner := range account.owners {
		if exists := owner.id == client.id; exists {
			return true
		}
	}

	return false
}

func (client *Client) deposit(account *Account, amt float64) {
	if !account.isOwner(client) {
		panic("You do not have access to this account")
	}

	account.balance += amt
	fmt.Printf("Client %s Depositing $%.2f\n", client.name, amt)
	time.Sleep(time.Second * 1)
	account.access <- true
}

func (client *Client) withdraw(account *Account, amt float64) {
	if !account.isOwner(client) {
		panic("You do not have access to this account")
	}

	account.balance -= amt
	fmt.Printf("Client %s Withdrawing $%.2f\n", client.name, amt)
	time.Sleep(time.Second * 1)
	account.access <- true
}

func createAccount(id int, balance float64, owners []Client) Account {
	return Account{
		id:      id,
		balance: balance,
		owners:  owners,
		access:  make(chan bool)}
}

func createClient(id int, name string) Client {
	return Client{id: id, name: name}
}

func main() {
	dan := createClient(1, "dan")
	jesse := createClient(2, "jesse")
	all_clients := []Client{dan, jesse}

	a := createAccount(1, 2000.0, []Client{dan, jesse})

	action_types := []string{"withdraw", "deposit"}

	for act := 0; act < 10; act++ {
		go func() {
			action := action_types[rand.Intn(len(action_types))]
			client := all_clients[rand.Intn(len(all_clients))]
			amt := rand.Float64() * 100

			if action == "withdraw" {
				client.withdraw(&a, amt)
			} else {
				client.deposit(&a, amt)
			}
		}()

		<-a.access
		fmt.Printf("New Balance: $%.2f\n", a.balance)
	}
	close(a.access)
}
