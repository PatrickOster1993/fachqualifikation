Reflektion zur Bearbeitung von Aufgabe 2
Erkenntnisse
Die Bearbeitung von Aufgabe 2 hat mir mehrere wichtige Erkenntnisse verschafft:
Wichtigkeit von Kommunikation: Bei der Implementierung von Sub-Features im Team ist eine klare Kommunikation über Datenformate 
und Schnittstellen unerlässlich. Ohne vorherige Absprache über die erwarteten Eingabe- und Ausgabeparameter kann es zu Inkompatibilitäten
zwischen den verschiedenen Modulen kommen.
Vorteile modularer Arbeit: Durch die Aufteilung des Projekts in Sub-Features lässt sich die Komplexität besser manage und es können parallele 
Entwicklungsarbeiten erfolgen. Jedes Sub-Feature kann unabhängig entwickelt, getestet und schließlich in den Hauptzweig integriert werden.
Notwendigkeit von Platzhaltern: Bei der Implementierung von Features, die auf noch nicht fertigen Komponenten basieren, haben Platzhalter-
Daten eine wichtige Funktion. Sie ermöglichen es, die Logik des eigenen Features zu entwickeln, auch wenn die abhängigen Module noch nicht 
vollständig implementiert sind.
Wichtigkeit von Issue-Tracking: Das Erstellen von detaillierten Issues mit klaren Anforderungen, erwarteten Eingaben und Ausgaben hilft dabei, 
Missverständnisse zu vermeiden und einen klaren Überblick über die Entwicklungszustände zu behalten.
Begegnete Probleme und Hürden
Während der Bearbeitung sind folgende Herausforderungen aufgetreten:
Abhängigkeiten zwischen Features: Bei der Implementierung des Benachrichtigungssystems musste ich auf Daten zurückgreifen, die von anderen Sub-
Features bereitgestellt werden. Da diese Features noch in Entwicklung waren, musste ich initially mit Platzhalter-Daten arbeiten und später die 
Schnittstellen an die tatsächlichen Datenformate anpassen.
Datenformat-Konsistenz: Es gab Diskrepanzen in den erwarteten Datenformaten zwischen den verschiedenen Modulen. So wurde beispielsweise das 
Datum der Beantragung in einem Format erwartet, das sich von dem Format unterschied, das von der Dateneingabefunktion geliefert wurde. 
Dies erforderte zusätzliche Konvertierungslogik.
Merge-Konflikte: Bei der Integration des Sub-Feature-Branches in den übergeordneten Feature-Branch traten Merge-Konflikte auf, die manuell 
gelöst werden mussten. Dies zeigte die Notwendigkeit auf, regelmäßig die Änderungen aus dem Hauptzweig zu pullen, um solche Konflikte frühzeitig
zu erkennen und zu bearbeiten.
Dokumentationsbedarf: Einige Funktionen und ihre Rückgabewerte waren nicht ausreichend dokumentiert, was zu Verzögerungen führte, da zusätzliche 
Klarstellungen mit anderen Teammitgliedern notwendig waren.
Zeitmanagement: Die parallele Arbeit an verschiedenen Sub-Features erfordert eine gute Zeitorganisation, um Deadlines einzuhalten und
gleichzeitig die Qualität der Implementierung zu gewährleisten.
Fazit
Die Umsetzung des Feature-Branch-Workflows hat gezeigt, dass dieser Ansatz bei guter Teamkoordination und klaren Kommunikationskanälen 
sehr effektiv sein kann. Allerdings erfordert er eine strukturierte Vorgehensweise bei der Definition von Features, deren Abhängigkeiten 
und den entsprechenden Datenformaten. Ohne diese Struktur kann der Workflow schnell zum "blanken Chaos" werden, wie es in der Aufgabenstellung 
beschrieben wurde.