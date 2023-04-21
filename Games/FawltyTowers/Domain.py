class Reservation:
    def __init__(self, id, nr, name,guests, ad, am, dd, dm):
        self._id = id
        self._nr = nr
        self._name = name
        self._guests=guests
        self._ad = ad
        self._am = am
        self._dd = dd
        self._dm = dm

    def __str__(self):
        return str(self._id) + "," + str(self._nr) + "," + str(self._name) + "," + str(self._guests)+","+str(self._ad) + "." + str(
            self._am) + "-" + str(self._dd) + "." + str(self._dm)

    @property
    def id(self):
        return self._id

    @property
    def nr(self):
        return self._nr

    @property
    def name(self):
        return self._name

    @property
    def ad(self):
        return self._ad

    @property
    def am(self):
        return self._am

    @property
    def dd(self):
        return self._dd

    @property
    def dm(self):
        return self._dm

    @property
    def guests(self):
        return self._guests
