Feature: Funkcjonalność - wyświetlanie listy wpisów do książki adresowej
  Wpisy dodane do książki adresowej mogą być wyświetlone w postaci listy.

  Scenario: Wyświetlanie listy dodanych wpisów do książki adresowej
      Given Mam książkę adresową
      And Mam pierwszy wpis <first>
      And Mam drugi wpis <second>
      When Po wydaniu polecenia "contacts ls"
      Then Dane wyjściowe zawierają listę wpisów <listed_contacts>

    Examples:
    | first   | second | listed_contacts |
    | Mariusz | Ludwik | Mariusz,Ludwik  |
    | Janek   | Jerzy  | Janek, Jerzy    |