# Τεχνική Αναφορά | Περιγραφή Εκτέλεσης Κώδικα
Τμήμα Ψηφιακών Συστημάτων | Πληροφοριακά Συστήματα : Ναταλία Κολιού, Ε18073
> # Εισαγωγή
> Στην τρέχουσα τεχνική αναφορά, θα περιγράψουμε αναλυτικά τα στάδιο εκτέλεσης του αρχείου app.py. Για τον σκοπό αυτό, θα χρησιμοποιήσουμε τον τερματικό του Linux και την εφαρμογή Postman. Με την εκκίνηση της εικονικής μας μηχανής, θα εκτελέσουμε στον terminal τις ακόλουθες δύο εντολές για να ενεργοποιήσουμε το docker και την βάση mongodb: sudo systemctl enable docker --now και sudo docker start mongodb. Στη συνέχεια, θα γράψουμε την εντολή python3 app.py για να ενεργοποιήσουμε τον debugger και να εκτελέσουμε το python αρχείο μας στον http://0.0.0.0:5000/. Προτείνεται η κατασκευή και των 13 JSON αρχείων που θα εισάγετε στο Postman προς δική σας διευκόλυνση ...

... ανατρέξτε στο αρχείο Indicative_JSON_files.txt της εργασίας στο GitHub.
> # Υλοποίηση του 1ου Endpoint | Δημιουργία Χρήστη
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την POST request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/createUser. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint1.json αρχείο μας στο σύστημα. Όταν φορτωθεί επιτυχώς, πατάμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

Ερμηνεία του Κώδικα: το σύστημα ελέγχει αν υπάρχουν ήδη χρήστες στην συλλογή των Users αξιοποιώντας την συνάρτηση count_documents(). Αν αυτή επιστρέψει 0, τότε αποθηκεύεται στο λεξικό user το name, το email, το password, το category και το orderHistory, που εισάγονται στο data μέσω της εντολής data = json.loads(request.data). Το λεξικό αυτό user μπαίνει στην συλλογή Users και εν τέλει αποστέλλεται μήνυμα επιτυχίας στον χρήστη. Ειδάλλως αν τα στοιχεία που θέλουμε να εισάγουμε, υπάρχουν ήδη στην συλλογή Users, επιστρέφεται το ανάλογο μήνυμα αποτυχίας.
> # Υλοποίηση του 2ου Endpoint | Login ως Standard User
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την POST request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/userLogin. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint2.json αρχείο μας στο σύστημα. Όταν φορτωθεί επιτυχώς, πατάμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

Ερμηνεία του Κώδικα: το σύστημα ελέγχει αν υπάρχουν standard users στην συλλογή των Users με το email και password που εισάγουμε στο Body του Postman. Αν βρεθεί ένας τέτοιος χρήστης τότε καλείται η συνάρτηση create_user_session() προκειμένου να αυθεντικοποιηθεί ο χρήστης. Έτσι επιστρέφεται στον χρήστη ένα λεξικό με keys το user unique identifier (uuid) και το email του χρήστη. Σε περίπτωση που δεν βρεθεί ο ζητούμενος χρήστης επιστρέφεται το ανάλογο μήνυμα αποτυχίας.
> # Υλοποίηση του 3ου Endpoint | Login ως Administrator
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την POST request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/adminLogin. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint3.json αρχείο μας στο σύστημα. Όταν φορτωθεί επιτυχώς, πατάμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

Ερμηνεία του Κώδικα: το σύστημα ελέγχει αν υπάρχουν administrators στην συλλογή των Users με το email και password που εισάγουμε στο Body του Postman. Αν βρεθεί ένας τέτοιος χρήστης τότε καλείται η συνάρτηση create_admin_session() προκειμένου να αυθεντικοποιηθεί ο χρήστης. Έτσι επιστρέφεται στον χρήστη ένα λεξικό με keys το user unique identifier (uuid) και το email του χρήστη. Σε περίπτωση που δεν βρεθεί ο ζητούμενος χρήστης επιστρέφεται το ανάλογο μήνυμα αποτυχίας.
