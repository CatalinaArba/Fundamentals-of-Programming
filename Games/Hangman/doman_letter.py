class Letter:
    def __init__(self,letter):
        self._letter=letter
        self._visible=0

    @property
    def letter(self):
        return self._letter

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self,item):
        self._visible=item

    def set_visible(self,item):
        self._visible = item

    def __str__(self):
        return str(self._letter)
