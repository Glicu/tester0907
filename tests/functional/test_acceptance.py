from pytest_bdd import scenario, given, parsers, when, then

from src import contacts


class TestAddingEntries:
    def test_basic(self):
        app = contacts.Application()
        app.run("contacts add Jan Kowalski 987654321")

        assert app._contacts == [("Jan Kowalski", "987654321")]

    def test_surnames_with_spaces(self):
        app = contacts.Application()
        app.run("contacts add Jan Kowalski-Kowalski 123456789")
        app.run("contacts add Ludwik Mariusz Kowalski 123456789")

        assert app._contacts == [
            ("Jan Kowalski-Kowalski", "123456789"),
            ("Ludwik Mariusz Kowalski", "123456789")
        ]

    def test_invalid_strings(self):
        app = contacts.Application()
        app.run("contacts add Jan Kowalski asdfasdfsasdf")
        assert app._contacts == []

    def test_international_numbers(self):
        app = contacts.Application()
        app.run("contacts add Yennefer z Wanderbergu +48987654321")

        assert app._contacts == [("Yennefer z Wanderbergu", "+48987654321")]

    def test_reload(self):
        app = contacts.Application()
        app.run("contacts add Yennefer z Wanderbergu +48987654321")

        assert app._contacts == [("Yennefer z Wanderbergu", "+48987654321")]
        app._clear()
        app.load()
        assert app._contacts == [("Yennefer z Wanderbergu", "+48987654321")]

@scenario(r"C:\Users\Glicu\PycharmProjects\tester0907\tests\acceptance\delete_contact.feature",
              "Usunięcie wpisu z książki adresowej")
def test_deleting_contacts():
    pass

@given("mam książkę adresową", target_fixture="contactbook")
def contactbook():
    return contacts.Application()

@given(parsers.parse("Mam wpis dotyczący użytkownika \"{contactname}\""))
def have_a_contact(contactbook, contactname):
    contactbook.add(contactname, "123456789")

@when(parsers.parse("Po wydaniu polecenia \"{command}\""))
def runcommand(contactbook, command):
    contactbook.run(command)

@then("wpis nie będzie już widoczny w książce adresowej")
def emptylist(contactbook):
    assert contactbook._contacts == []


