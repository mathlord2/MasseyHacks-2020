<script>
    import { onMount } from "svelte";
    import { loggedIn, currentUser, userEmail } from "../stores.js";

    onMount(() => {
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
                    //getUserData();
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
</script>

<div id="firebaseui-auth-container"></div>

<style>
    #firebaseio-auth-container {
        margin-top: 10%;
    }
</style>