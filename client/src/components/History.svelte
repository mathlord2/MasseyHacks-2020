<script>
    import { onMount } from "svelte";
    import { page, loggedIn, currentUser, userEmail, questions, data } from "../stores.js";

    let email;
    let userData;

    const unsubscribe1 = userEmail.subscribe(val => {
        email = val;
    });

    const unsubscribe2 = data.subscribe(val => {
        userData = val;
    });

    let previousArticulationRate;
    let previousPronunciationScore;

    onMount(() => {
        window.$("#home").on("click", function() {
            page.set("Home");
        });

        window.$("#signout").on("click", signout);
        getData();
    });

    function signout() {
        firebase.auth().signOut().then(function() {
            loggedIn.set(false);
            currentUser.set(null);
            console.log("Signed out");
        });
    }

    function getData() {
        db.collection("users").get().then(function(querySnapshot) {
            querySnapshot.forEach(function(doc) {
                if (email == doc.data().userEmail) {
                    createTables(doc.data());
                }
            });
        });
    }

    function createTables(data) {
        var history = document.getElementById("logs");
        
        //Question 1
        var question1 = document.createElement("h1");
        var qText1 = document.createTextNode(questions[0]);
        question1.style.marginTop = "40px";
        question1.appendChild(qText1);
        history.appendChild(question1);

        var seeTable1 = document.createElement("h2");
        var text1 = document.createTextNode("Reveal Table ▼");
        seeTable1.appendChild(text1);
        
        var table1 = document.createElement("table");
        table1.style.backgroundColor = "white";
        table1.style.display = "none";
        createHeading(table1);

        const q1 = data.Question1;

        for (var i = 0; i < q1.articulationRate.length; i++) {
            var tr = document.createElement("tr");
            createRow(tr, q1, i);
            table1.appendChild(tr);
        }

        seeTable1.addEventListener("click", function() {
            if (table1.style.display == "none") {
                table1.style.display = "block";
                seeTable1.innerHTML = "Close Table ▲";
            } else {
                table1.style.display = "none";
                seeTable1.innerHTML = "Reveal Table ▼";
            }
        });

        history.appendChild(seeTable1);
        history.appendChild(table1);

        //Question 2
        var question2 = document.createElement("h1");
        var qText2 = document.createTextNode(questions[1]);
        question2.style.marginTop = "40px";
        question2.appendChild(qText2);
        history.appendChild(question2);

        var seeTable2 = document.createElement("h2");
        var text2 = document.createTextNode("Reveal Table ▼");
        seeTable2.appendChild(text2);
        
        var table2 = document.createElement("table");
        table2.style.backgroundColor = "white";
        table2.style.display = "none";
        createHeading(table2);

        const q2 = data.Question2;

        for (var i = 0; i < q2.articulationRate.length; i++) {
            var tr = document.createElement("tr");
            createRow(tr, q2, i);
            table2.appendChild(tr);
        }

        seeTable2.addEventListener("click", function() {
            if (table2.style.display == "none") {
                table2.style.display = "block";
                seeTable2.innerHTML = "Close Table ▲";
            } else {
                table2.style.display = "none";
                seeTable2.innerHTML = "Reveal Table ▼";
            }
        });

        history.appendChild(seeTable2);
        history.appendChild(table2);

        //Question 3
        var question3 = document.createElement("h1");
        var qText3 = document.createTextNode(questions[2]);
        question3.style.marginTop = "40px";
        question3.appendChild(qText3);
        history.appendChild(question3);

        var seeTable3 = document.createElement("h2");
        var text3 = document.createTextNode("Reveal Table ▼");
        seeTable3.appendChild(text3);
        
        var table3 = document.createElement("table");
        table3.style.backgroundColor = "white";
        table3.style.display = "none";
        createHeading(table3);

        const q3 = data.Question3;

        for (var i = 0; i < q3.articulationRate.length; i++) {
            var tr = document.createElement("tr");
            createRow(tr, q3, i);
            table3.appendChild(tr);
        }

        seeTable3.addEventListener("click", function() {
            if (table3.style.display == "none") {
                table3.style.display = "block";
                seeTable3.innerHTML = "Close Table ▲";
            } else {
                table3.style.display = "none";
                seeTable3.innerHTML = "Reveal Table ▼";
            }
        });

        history.appendChild(seeTable3);
        history.appendChild(table3);
    }

    function createRow(tr, question, i) {
        //Date
        var date = document.createElement("td");
        date.style.padding = "20px";
        var dateTxt = document.createTextNode(String(question.dates[i]));
        date.appendChild(dateTxt);

        //Articulation
        var art = document.createElement("td");
        art.style.padding = "20px";
        var artTxt = document.createTextNode(String(question.articulationRate[i]));
        if (i != 0 && hasBetterArticulationRate(previousArticulationRate, question.articulationRate[i])) { //Algorithm for determining better articulation rate
            art.style.backgroundColor = "green";
            art.style.color = "white";
        } else if (i != 0 && hasBetterArticulationRate(previousArticulationRate, question.articulationRate[i]) == false) {
            art.style.backgroundColor = "red";
            art.style.color = "white";
        }

        previousArticulationRate = question.articulationRate[i];
        art.appendChild(artTxt);

        //Duration
        var duration = document.createElement("td");
        duration.style.padding = "20px";
        var durationTxt = document.createTextNode(String(question.duration[i]));
        duration.appendChild(durationTxt);

        //Pronunciation
        var pronun = document.createElement("td");
        pronun.style.padding = "20px";
        var pronunTxt = document.createTextNode(String(question.pronunciationScore[i]));
        if (i != 0 && question.pronunciationScore[i] > previousPronunciationScore) { //Comparing pronunciation scores
            pronun.style.backgroundColor = "green";
            pronun.style.color = "white";
        } else if (i != 0 && question.pronunciationScore[i] < previousPronunciationScore) {
            pronun.style.backgroundColor = "red";
            pronun.style.color = "white";
        }

        previousPronunciationScore = question.pronunciationScore[i];
        pronun.appendChild(pronunTxt);

        tr.appendChild(date);
        tr.appendChild(art);
        tr.appendChild(duration);
        tr.appendChild(pronun);
    }

    function createHeading(table) {
        var tr = document.createElement("tr");

        //Date heading
        var dateHeading = document.createElement("th");
        dateHeading.style.padding = "20px";
        var dateText = document.createTextNode("Date");
        dateHeading.appendChild(dateText);

        //Articulation Rate Heading
        var artHeading = document.createElement("th");
        artHeading.style.padding = "20px";
        var artText = document.createTextNode("Articulation Rate (syllables/second)");
        artHeading.appendChild(artText);

        //Duration Heading
        var durationHeading = document.createElement("th");
        durationHeading.style.padding = "20px";
        var durationText = document.createTextNode("Duration (seconds)");
        durationHeading.appendChild(durationText);

        //Pronunciation score Heading
        var pronunHeading = document.createElement("th");
        pronunHeading.style.padding = "20px";
        var pronunText = document.createTextNode("Pronounciation Score (%)");
        pronunHeading.appendChild(pronunText);

        tr.appendChild(dateHeading);
        tr.appendChild(artHeading);
        tr.appendChild(durationHeading);
        tr.appendChild(pronunHeading);

        table.appendChild(tr);
    }

    function hasBetterArticulationRate(previous, current) {
        //Good articulation rate is at 4 sps - closer to 4 = better
        var art1 = Math.abs(previous-4);
        var art2 = Math.abs(current-4);

        if (art2 < art1) {
            return true;
        } else if (art2 > art1) {
            return false;
        } else {
            return "Neither";
        }
    }

</script>

<div>
    <nav>
        <div id="home">Home</div>
        <div id="history">History</div>
        <div id="signout" on:click={signout}>Sign Out</div>
    </nav>
    <div id="logs">
        <table></table>
    </div>
</div>

<style>
    nav {
		width: 100%;
		padding: 10px;
		position: fixed;
		background-color: rgb(204, 160, 255);
		display: flex;
		left: 0;
        top: 0;
    }
    
    nav div {
        margin: 0px 20px;
    }

    nav div:hover {
        cursor: pointer;
        color: white;
    }

    #signout {
        position: absolute;
        right: 20px;
    }

    #logs {
        margin-top: 100px;
        text-align: left;
    }
</style>