from __future__ import annotations
from abc import ABC, abstractmethod


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_checkbox(self):
        pass

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()
    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    def create_checkbox(self):
        return MacCheckbox()

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass
    @abstractmethod
    def click(self, collaborator):
        pass

class WinCheckbox(Checkbox):
    def check(self):
        #print('windows switch')
        return 'windows switch'
    def click(self, collaborator):
        result = collaborator.push()
        return f'windows called {result}'

class MacCheckbox(Checkbox):
    def check(self):
        #print('Apple switch')
        return 'Apple switch'
    def click(self, collaborator):
        result = collaborator.push()
        return f'Apple called {result}'

class Button(ABC):
    @abstractmethod
    def push(self):
        pass

class WinButton(Button):
    def push(self):
        # print('Windows push')
        return 'Windows push'

class MacButton(Button):
    def push(self):
        # print('Apple push')
        return 'Apple push'

def client_code(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(f'{checkbox.check()}')
    print(f'{checkbox.click(button)}')

if __name__ == '__main__':
    client_code(WinFactory())
    print()
    client_code(MacFactory())