# Object Ref
class Wallet:
    def __init__(self):
        self.amount = 0

    def earn(self, a):
        self.amount += a

    def spend(self, a):
        self.amount -= a

    def __str__(self):
        return "Amount = {}".format(self.amount)

if __name__ == '__main__':
    dadWallet = Wallet()
    dadWallet.earn(100)
    print("Dad's Wallet: ", dadWallet)
    momWallet = dadWallet
    print(momWallet is dadWallet)
    momWallet.earn(50)
    print(dadWallet)
    kid = Wallet()
    momWallet = kid
    print(id(dadWallet), id(momWallet), id(kid))
