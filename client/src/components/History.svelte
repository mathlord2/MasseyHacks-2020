<script>
    import { onMount } from "svelte";
    import { page, loggedIn, currentUser, questions } from "../stores.js";

    onMount(() => {
        window.$("#home").on("click", function() {
            page.set("Home");
        });
    });

    function signout() {
        firebase.auth().signOut().then(function() {
            loggedIn.set(false);
            currentUser.set(null);
            console.log("Signed out");
        });
    }
</script>

<div>
    <nav>
        <div id="home">Home</div>
        <div id="history">History</div>
        <div id="signout" on:click={signout}>Sign Out</div>
    </nav>
    <div id="logs">
        {#each questions as question}
            <h1>{question}</h1>
            <table>
                <tr>
                    <th></th>
                </tr>
            </table>
        {/each}
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

    table, tr, th, td {
        border: none;
    }
</style>