# Dateipfad: versionsverwaltung git/benachrichtigung.py

def generiere_benachrichtigung(beantragungsdatum, vorname, nachname):
    """
    Generiert eine Benachrichtigungsnachricht für die Personalausweis-Beantragung.
    
    Args:
        beantragungsdatum (str): Datum der Beantragung im Format "YYYY-MM-DD"
        vorname (str): Vorname der beantragenden Person
        nachname (str): Nachname der beantragenden Person
    
    Returns:
        str: Formatierte Benachrichtigungsnachricht
    """
    # Platzhalter-Daten für mögliche zukünftige Erweiterungen
    bearbeitungszeit = "3-5 Werktage"
    dokumentation_link = "https://www.beamt-deutschland.de/personalausweis"
    
    benachrichtigung = f"""
    Sehr geehrte(r) {vorname} {nachname},
    
    vielen Dank für Ihre Personalausweis-Beantragung am {beantragungsdatum}.
    Wir bearbeiten Ihren Antrag und werden Ihnen binnen {bearbeitungszeit} eine weitere Nachricht zukommen lassen.
    
    Für weitere Informationen besuchen Sie bitte unsere Dokumentation unter:
    {dokumentation_link}
    
    Mit freundlichen Grüßen
    Das Team des Bürgeramts
    """
    return benachrichtigung