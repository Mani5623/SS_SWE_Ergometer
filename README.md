# SS_SWE_Ergometer

# Name und Identifikationsnummer
UC 1.03 (Alarm bei zu hoher Herzfrequenz)

# Beschreibung
Durch diese Funktion wird der/die Proband:in und der/die Diagnostiker:in bei einer zu hohen Herzfrequenz benachrichtigt

# Beteiligte Akteure
Diagnostiker:in, Proband:in

# Status
In Arbeit

# Verwendete Anwendungsfälle
UC 1.01 (Probandin anlegen)
UC 1.02 (Leistungstest anlegen)

# Auslöser
1. Sicherheitsaspekt: Eine extrem hohe Herzfrequenz kann ein Zeichen für Überlastung oder eine unzureichende kardiovaskuläre Anpassung sein, was das Risiko für Herz-Kreislauf-Probleme erhöht.
2. Testgenauigkeit: Wenn die Herzfrequenz aufgrund von Erschöpfung, Dehydrierung oder anderen Faktoren unverhältnismäßig hoch ist, kann das die Ergebnisse des Tests verfälschen und zu falschen Schwellenwerten führen.
3. Physiologische Grenzen: Wenn die Herzfrequenz ungewöhnlich hoch ansteigt, könnte das darauf hindeuten, dass der Athlet bereits über seiner anaeroben Schwelle arbeitet, bevor der eigentliche Testpunkt erreicht ist. Das würde den Test unbrauchbar machen.
4. Regulatorische Vorgaben: In vielen standardisierten Tests gibt es Sicherheitsprotokolle, die einen Abbruch bei einer bestimmten maximalen Herzfrequenz vorschreiben, um gesundheitliche Risiken zu minimieren.

# Vorbedingungen
UC 1.01 (Probandin anlegen)
UC 1.02 (Leistungstest anlegen)

# Invarianten
Dauerhafte Aufzeichnung der Herzfrequenz

# Nachbedingungen/Ergebnis
1. Test wurde sicher beendet: Der Testlauf wurde abgebrochen, bevor eine kritische Überlastung oder gesundheitliche Gefährdung aufgetreten ist.
2. Herzfrequenz wurde protokolliert: Die erreichte maximale Herzfrequenz sowie relevante Daten bis zum Abbruch sind dokumentiert.
3. Testergebnis wird als ungültig oder unvollständig markiert: Da der Test nicht vollständig durchgeführt wurde, können keine belastbaren Schwellenwerte ermittelt werden.
4. Empfehlung für weiteres Vorgehen: Basierend auf den Daten kann eine Empfehlung gegeben werden, ob der Test unter anderen Bedingungen wiederholt werden sollte oder ob eine alternative Diagnostik sinnvoll ist.
5. Athlet befindet sich in stabilem Zustand: Keine anhaltenden negativen Auswirkungen wie Schwindel, extreme Erschöpfung oder Kreislaufprobleme.

# Standardablauf
Leistungstest wird nicht auf Grund einer zu hohen Herzfrequenz abgebrochen.

# Alternative Ablaufschritte
1. HF-Grenzwert wird fast erreicht, aber nicht überschritten. Der Test läuft weiter, aber die Herzfrequenz nähert sich der Abbruchgrenze. Eventuell erfolgt eine automatische Warnung oder eine manuelle Entscheidung über den Fortgang des Tests.
2. Plötzlicher Anstieg der Herzfrequenz durch externe Faktoren. Störfaktoren wie Messfehler, Stress oder eine ungünstige Umgebung (Hitze, Luftfeuchtigkeit) führen zu einem unerwartet hohen HF-Wert. Der Testleiter oder das System entscheidet, ob der Wert plausibel ist oder eine Fehlmessung vorliegt.
3. Athlet zeigt subjektive Erschöpfungssymptome vor Erreichen des HF-Grenzwerts. Der Test wird aufgrund von Schwindel, Unwohlsein oder anderen Beschwerden vorzeitig beendet, obwohl die Herzfrequenz unter der Abbruchgrenze liegt.
4. Test wird trotz hoher Herzfrequenz nicht abgebrochen. Der Athlet oder der Testleiter ignoriert die Grenze und setzt den Test fort (z. B. aufgrund einer Fehlkonfiguration oder bewusster Entscheidung). Es könnte eine Warnung oder ein Hinweis zur Risikoabschätzung erfolgen.
5. Technischer Fehler verhindert den Abbruch. Der Herzfrequenzsensor funktioniert nicht korrekt, sodass der Grenzwert nicht erkannt wird. Der Test läuft weiter, obwohl eigentlich ein Abbruch erfolgen sollte.

# Hinweise
1. Definition der HF-Grenze: Die Abbruchgrenze kann individuell festgelegt sein (z. B. prozentual zur maximalen HF) oder auf Standardwerten basieren (z. B. 90 % der HFmax).
Individuelle Unterschiede: Faktoren wie Trainingszustand, Tagesform, Stress oder Dehydration können die Herzfrequenz stark beeinflussen, was zu variierenden Testergebnissen führt.
2. Messgenauigkeit: Ungenaue Sensoren oder Verzögerungen in der HF-Messung können zu Fehleinschätzungen führen, daher sollte eine kurze Validierungsphase erfolgen.
3. Alternativen bei Abbruch: Falls der Test aufgrund einer zu hohen HF abgebrochen wird, könnte ein alternativer Test mit niedrigerer Belastungssteigerung oder eine Wiederholung unter anderen Bedingungen sinnvoll sein.
4. Gesundheitsrisiken: Ein zu langes Ignorieren hoher Herzfrequenzen kann zu Überlastungen führen, daher ist eine frühzeitige Beurteilung der individuellen Belastbarkeit wichtig.

# Änderungsgeschichte
0.01, Jakob Haas und Manuel Hager, 15.03.2025
