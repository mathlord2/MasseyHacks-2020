<script>
    import { onMount } from "svelte";
    import { loggedIn, currentUser, userEmail, data } from "../stores.js";

    onMount(() => {
        firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
                console.log("Signed in");
                loggedIn.set(true);
                currentUser.set(user);
                userEmail.set(user.email);
                getData(user.email);
            } else {
                console.log("Signed out");
            }
        });

        var uiConfig = {
            signInOptions: [
                // Leave the lines as is for the providers you want to offer your users.
                firebase.auth.GoogleAuthProvider.PROVIDER_ID,
                firebase.auth.EmailAuthProvider.PROVIDER_ID,
            ],
            // tosUrl and privacyPolicyUrl accept either url string or a callback
            // function.
            // Terms of service url/callback.
            callbacks: {
                signInSuccessWithAuthResult: function(authResult, redirectUrl) {
                    var user = authResult.user;
                    loggedIn.set(true);
                    currentUser.set(user);
                    userEmail.set(user.email);
                    if (authResult.additionalUserInfo.isNewUser) {
                        console.log("New user");
                        createNewObject(user.email);
                    } else {
                        getData(user.email);
                    }
                    return true;
                },
                signInFailure: function(error) {
                    // Some unrecoverable error occurred during sign-in.
                    // Return a promise when error handling is completed and FirebaseUI
                    // will reset, clearing any UI. This commonly occurs for error code
                    // 'firebaseui/anonymous-upgrade-merge-conflict' when merge conflict
                    // occurs. Check below for more details on this.
                    console.log("Error");
                    return handleUIError(error);
                },
            }
        };
        // Initialize the FirebaseUI Widget using Firebase.
        var ui = firebaseui.auth.AuthUI.getInstance() || new firebaseui.auth.AuthUI(firebase.auth());
        // The start method will wait until the DOM is loaded.
        ui.start('#firebaseui-auth-container', uiConfig);
    });

    function createNewObject(email) {
        const userData = {
            userEmail: email,
            Question1: {
                articulationRate: [],
                dates: [],
                duration: [],
                pronunciationScore: []
            },
            Question2: {
                articulationRate: [],
                dates: [],
                duration: [],
                pronunciationScore: []
            },
            Question3: {
                articulationRate: [],
                dates: [],
                duration: [],
                pronunciationScore: []
            }
        }
        db.collection("users").add(userData).catch(function(error) {
            console.error("Error adding document: ", error);
        });
        data.set(userData);
    }

    function getData(email) {
        db.collection("users").get().then(function(querySnapshot) {
            querySnapshot.forEach(function(doc) {
                if (email == doc.data().userEmail) {
                    data.set(doc.data());
                }
            });
        });
    }
</script>

<div id="firebaseui-auth-container"></div>

<style>
    #firebaseui-auth-container {
        margin-top: 10%;
    }
</style>