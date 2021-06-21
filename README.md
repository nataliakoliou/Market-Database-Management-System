# Τεχνική Αναφορά | Περιγραφή Εκτέλεσης Κώδικα
Τμήμα Ψηφιακών Συστημάτων | Πληροφοριακά Συστήματα : Ναταλία Κολιού, Ε18073
> # Εισαγωγή
> Στην τρέχουσα τεχνική αναφορά, θα περιγράψουμε αναλυτικά τα στάδιο εκτέλεσης του αρχείου app.py. Για τον σκοπό αυτό, θα χρησιμοποιήσουμε τον τερματικό του Linux και την εφαρμογή Postman. Με την εκκίνηση της εικονικής μας μηχανής, θα εκτελέσουμε στον terminal τις ακόλουθες δύο εντολές για να ενεργοποιήσουμε το docker και την βάση mongodb: sudo systemctl enable docker --now και sudo docker start mongodb. Στη συνέχεια, θα γράψουμε την εντολή python3 app.py για να ενεργοποιήσουμε τον debugger και να εκτελέσουμε το python αρχείο μας στον http://0.0.0.0:5000/. Προτείνεται η κατασκευή και των 13 JSON αρχείων που θα εισάγετε στο Postman προς δική σας διευκόλυνση ...

> ... ανατρέξτε στο αρχείο Indicative_JSON_files.txt της εργασίας στο GitHub.
> # Υλοποίηση του 1ου Endpoint | Δημιουργία Χρήστη
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την POST request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/createUser. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint1.json αρχείο μας στο σύστημα. Όταν φορτωθεί επιτυχώς, πατάμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα ελέγχει αν υπάρχουν ήδη χρήστες στην συλλογή των Users αξιοποιώντας την συνάρτηση count_documents(). Αν αυτή επιστρέψει 0, τότε αποθηκεύεται στο λεξικό user το name, το email, το password, το category και το orderHistory, που εισάγονται στο data μέσω της εντολής data = json.loads(request.data). Το λεξικό αυτό user μπαίνει στην συλλογή Users και εν τέλει αποστέλλεται μήνυμα επιτυχίας στον χρήστη. Ειδάλλως αν τα στοιχεία που θέλουμε να εισάγουμε, υπάρχουν ήδη στην συλλογή Users, επιστρέφεται το ανάλογο μήνυμα αποτυχίας.
> # Υλοποίηση του 2ου Endpoint | Login ως Standard User
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την POST request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/userLogin. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint2.json αρχείο μας στο σύστημα. Όταν φορτωθεί επιτυχώς, πατάμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα ελέγχει αν υπάρχουν standard users στην συλλογή των Users με το email και password που εισάγουμε στο Body του Postman. Αν βρεθεί ένας τέτοιος χρήστης τότε καλείται η συνάρτηση create_user_session() προκειμένου να αυθεντικοποιηθεί ο χρήστης. Έτσι επιστρέφεται στον χρήστη ένα λεξικό με keys το user unique identifier (uuid) και το email του χρήστη. Σε περίπτωση που δεν βρεθεί ο ζητούμενος χρήστης επιστρέφεται το ανάλογο μήνυμα αποτυχίας.
> # Υλοποίηση του 3ου Endpoint | Login ως Administrator
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την POST request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/adminLogin. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint3.json αρχείο μας στο σύστημα. Όταν φορτωθεί επιτυχώς, πατάμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα ελέγχει αν υπάρχουν administrators στην συλλογή των Users με το email και password που εισάγουμε στο Body του Postman. Αν βρεθεί ένας τέτοιος χρήστης τότε καλείται η συνάρτηση create_admin_session() προκειμένου να αυθεντικοποιηθεί ο χρήστης. Έτσι επιστρέφεται στον χρήστη ένα λεξικό με keys το user unique identifier (uuid) και το email του χρήστη. Σε περίπτωση που δεν βρεθεί ο ζητούμενος χρήστης επιστρέφεται το ανάλογο μήνυμα αποτυχίας.
> # Υλοποίηση του 4ου Endpoint | Αναζήτηση Προϊόντων
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/searchProduct. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint4.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως standard χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_user_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει κάποιο product στην συλλογή Products με το id, ή το name ή το category που έλαβε μέσω Postman (το endpoint4.json μπορεί να περιέχει είτε το id, είτε το name είτε το category με βάση το οποίο θα αναζητήσουμε ένα προϊόν). Αν πράγματι βρεθεί ένα ή και περισσότερα τέτοια products, τότε επιστρέφονται τα στοιχεία τους μέσω μιας λίστας λεξικών: products_l | περιέχει τα λεξικά product_d. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το id/name/category δεν αντιστοιχεί σε κάποιο προϊόν, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 5ου Endpoint | Προσθήκη στο Καλάθι
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/addToCart. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint5.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως standard χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_user_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει κάποιο product στην συλλογή Products με το id που έλαβε μέσω Postman. Συγχρόνως απαιτεί αυτό το product να βρίσκεται στο stock σε ποσότητες μεγαλύτερες ή ίσες με το quantity που δηλώνει ο χρήστης στο endpoint5.json. Αν πράγματι το ζητούμενο product είναι διαθέσιμο, τότε τοποθετείται στην λίστα cart μέσω του λεξικού product_d. Για να υπολογίσουμε το συνολικό χρηματικό ποσό των προϊόντων του cart, θα λάβουμε τις εξής δύο περιπτώσεις: το cart να είναι άδειο και το cart να έχει τουλάχιστον ένα product μέσα. Στην πρώτη περίπτωση ελέγχουμε αν το επιθυμητό προϊόν βρίσκεται ήδη στο καλάθι, για να μην το προσθέσουμε ξανά σε αυτό, αλλά να αλλάξουμε απλώς το πεδίο quantity με βάση την νέα παραγγελία. Στην δεύτερη περίπτωση, απλά προσθέτουμε το προϊόν στο καλάθι δίχως περεταίρω ενέργειες. Τέλος, υπολογίζουμε το συνολικό κόστος totalPrice λαμβάνοντας το γινόμενο του κάθε product του cart με την αντίστοιχη quantity στην οποία το συναντάμε σε αυτό. Εμφανίζουμε τα στοιχεία του καλαθιού στον χρήστη και τερματίζουμε το endpoint. Και φυσικά, σε περίπτωση που το uuid είναι μη έγκυρο, ή το id/quantity δεν αντιστοιχεί σε κάποιο διαθέσιμο προϊόν, επιστρέφεται μήνυμα λάθους.
> > # Υλοποίηση του 6ου Endpoint | Εμφάνιση του Καλαθιού
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/displayCart. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως standard χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Προσοχή: δεν εισάγουμε τίποτα στο πεδίο Body. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_user_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν το cart είναι γεμάτο ή άδειο. Σε περίπτωση που είναι άδειο εμφανίζεται το αντίστοιχο μήνυμα απάντησης. Αν πάλι υπάρχουν προϊόντα στο καλάθι, τότε υπολογίζεται κατά τα γνωστά το totalPrice και εμφανίζονται τα στοιχεία του καλαθιού (στοιχεία προϊόντων και συνολικό κόστος). Σε περίπτωση που το uuid είναι μη έγκυρο, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 7ου Endpoint | Διαγραφή από το Καλάθι
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/removeFromCart. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint7.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως standard χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_user_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει κάποιο product στην συλλογή Products με το id που έλαβε μέσω Postman. Αν πράγματι εντοπιστεί το ζητούμενο product, τότε αφαιρείται από την λίστα cart, λαμβάνοντας υπ' όψιν το προσωπικό του id (σύμφωνα με αυτό αναζητείται το προϊόν στο cart). Υπολογίζουμε στην συνέχεια, το συνολικό χρηματικό ποσό των προϊόντων του cart που απομένουν και αποθηκεύουμε το αποτέλεσμα στην μεταβλητή totalPrice. Εμφανίζουμε τα ανανεωμένα στοιχεία του καλαθιού στον χρήστη και τερματίζουμε το endpoint. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το id δεν αντιστοιχεί σε κάποιο προϊόν, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 8ου Endpoint | Αγορά Προϊόντων
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την PATCH request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/buyProduct. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint8.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως standard χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_user_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν το cardNumber του χρήστη είναι ένας δεκαεξαψήφιος κωδικός. Αν λοιπόν ο αριθμός της κάρτας του είναι έγκυρος, προχωράμε επιτυχώς στην διαδικασία της συναλλαγής. Από το users_sessions εντοπίζουμε το email του χρήστη και το αποθηκεύουμε στην μεταβλητή email. Το δεδομένο αυτό θα το χρειαστούμε στην συνέχεια για να κάνουμε update στο πεδίο orderHistory του χρήστη με το δεδομένο email. Αρχικά ελέγχουμε αν το cart είναι άδειο, ή αν έχει τουλάχιστον ένα προϊόν προς αγορά. Στην πρώτη περίπτωση εμφανίζεται το αντίστοιχο μήνυμα απάντησης, ενώ στην δεύτερη το σύστημα κατασκευάζει ένα for loop για να κάνει update στην συλλογή Products για το κάθε ένα product στο cart. Όταν ολοκληρωθεί η διαδικασία του update, τα στοιχεία του κάθε product εισάγονται στην λίστα receipt και συγχρόνως συναθροίζουμε ένα ένα τα prices x quantity μέσα στην μεταβλητή totalPrice. Μέσα στην for υπάρχει το if case που αναλαμβάνει το pdate στο orderHistory της συλλογής Users για το κάθε προϊόν που προστίθεται στην απόδειξη του χρήστη. Αν το προϊόν αυτό έχει προηγουμένως αγοραστεί από αυτόν, δεν ικανοποιούνται οι προϋποθέσεις της if case και άρα το σύστημα δεν μπαίνει ποτέ σε αυτήν. Το καλάθι εν τέλει αδειάζει και η ζητούμενη απόδειξη της συναλλαγής εμφανίζεται στον χρήστη. Και φυσικά, σε περίπτωση που το uuid είναι μη έγκυρο, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 9ου Endpoint | Εμφάνιση Ιστορικού Παραγγελιών
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/showOrderHistory. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως standard χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Προσοχή: δεν εισάγουμε τίποτα στο πεδίο Body. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_user_session_valid(). Αν λάβει θετική απάντηση, προχωράει στον εντοπισμό του email του τρέχοντος χρήστη (μέσω του users_sessions). Όταν το βρούμε, το αποθηκεύουμε κανονικά στην μεταβλητή email. Σύμφωνα με αυτό το δεδομένο, ανατρέχουμε στο πεδίο orderHistory του user με το παραπάνω email και ελέγχουμε αν αυτό είναι άδειο. Αν πράγματι είναι άδειο, τότε εμφανίζεται το ανάλογο μήνυμα απάντησης. Αν πάλι είναι γεμάτο, εμφανίζεται η λίστα των παραγγελιών του χρήστη που είναι αποθηκευμένη σε αυτό το πεδίο. Σε περίπτωση που το uuid είναι μη έγκυρο, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 10ου Endpoint | Διαγραφή Χρήστη
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την DELETE request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/deleteUser. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint1.json αρχείο μας στο σύστημα. Όταν φορτωθεί επιτυχώς, πατάμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_user_session_valid(). Αν λάβει θετική απάντηση, προχωράει στον εντοπισμό του email του τρέχοντος χρήστη (μέσω του users_sessions). Όταν το βρούμε, το αποθηκεύουμε κανονικά στην μεταβλητή email. Σύμφωνα με αυτό το δεδομένο, μπορούμε να διαγράψουμε τον τρέχοντα χρήστη από την συλλογή Users. Αν η διαγραφή εκτελεστεί επιτυχώς επιστρέφεται το ανάλογο μήνυμα απάντησης. Σε περίπτωση που το uuid είναι μη έγκυρο, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 11ου Endpoint | Προσθήκη στο DSMarket
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την PATCH request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/addToMarket. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint11.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως administrator χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην admins_session, καλώντας την συνάρτηση is_admin_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει κάποιο product στην συλλογή Products με το id που έλαβε μέσω Postman. Αν πράγματι το ζητούμενο product υπάρχει ήδη στο stock του καταστήματος, τότε εκτυπώνεται το ανάλογο μήνυμα απάντησης (είναι αδύνατη η εισαγωγή ήδη υπάρχοντος προϊόντος στο σύστημα). Αν πάλι δεν εντοπιστέι στην συλλογή Products, τότε προστίθεται σε αυτή μέσω του λεξικού product_d. Κατά την επιτυχή εισαγωγή στο σύστημα εμφανίζεται το αντίστοιχο μήνυμα επιτυχίας. Σε περίπτωση που το uuid είναι μη έγκυρο, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 12ου Endpoint | Διαγραφή από το DSMarket
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την PATCH request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/removeFromMarket. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint12.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως administrator χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην admins_session, καλώντας την συνάρτηση is_admin_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει κάποιο product στην συλλογή Products με το id που έλαβε μέσω Postman. Αν πράγματι το ζητούμενο product υπάρχει στο stock του καταστήματος, τότε αφαιρείται εντελώς από αυτό και εκτυπώνεται το αντίστοιχο μήνυμα επιτυχίας. Σε περίπτωση που το uuid είναι μη έγκυρο ή το id δεν αντιστοιχεί σε κάποιο υπάρχον προϊόν στην συλλογή Products, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 13ου Endpoint | Ενημέρωση στο DSMarket
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την PATCH request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/updateProduct. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint13.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως administrator χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.

> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην admins_session, καλώντας την συνάρτηση is_admin_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει κάποιο product στην συλλογή Products με το id που έλαβε μέσω Postman. Αν πράγματι το ζητούμενο product υπάρχει στο stock του καταστήματος, τότε ενημερώνεται σύμφωνα με τα data ου εισάγει ο χρήστης και εκτυπώνεται το αντίστοιχο μήνυμα επιτυχίας. Το endpoint11.json μπορεί να περιέχει είτε το νέο id του προϊόντος, είτε το νέο name του, είτε το νέο price του ή ακόμα και το νέο category του (γενικά ενημερώνεται ένα από τα τέσσερα αυτά πεδία του προϊόντος). Σε περίπτωση που το uuid είναι μη έγκυρο ή το id δεν αντιστοιχεί σε κάποιο υπάρχον προϊόν στην συλλογή Products, επιστρέφεται μήνυμα λάθους.
