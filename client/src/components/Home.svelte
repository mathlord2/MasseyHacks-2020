<script>
    import { onMount } from "svelte";
    import { page, loggedIn, currentUser, questions } from "../stores.js";

    let recorder;
    let question;
    let time;
    let audioURL;

    onMount(() => {
        window.$("#history").on("click", function() {
            page.set("History");
        });
    });

    // appends an audio element to playback and download recording
    function createAudioElement(blobUrl) {
        audioURL = blobUrl;
        console.log(audioURL);
        const downloadEl = document.createElement('a');
        downloadEl.style = 'display: block';
        downloadEl.innerHTML = 'download';
        downloadEl.download = 'audio.wav';
        downloadEl.href = blobUrl;
        const audioEl = document.createElement('audio');
        audioEl.controls = true;
        const sourceEl = document.createElement('source');
        sourceEl.src = blobUrl;
        sourceEl.type = 'audio/wav';
        audioEl.appendChild(sourceEl);
        document.getElementById("content").appendChild(audioEl);
        document.getElementById("content").appendChild(downloadEl);
    }

    function record() {
        // request permission to access audio stream
        navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
            // store streaming data chunks in array
            const chunks = [];
            // create media recorder instance to initialize recording
            recorder = new MediaRecorder(stream);
            // function to be called when data is received
            recorder.ondataavailable = e => {
                // add stream data to chunks
                chunks.push(e.data);
                // if recorder is 'inactive' then recording has finished
                if (recorder.state == 'inactive') {
                    // convert stream data chunks to a 'webm' audio format as a blob
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    // convert blob to URL so it can be assigned to a audio src attribute
                    createAudioElement(URL.createObjectURL(blob));
                }
            };
            // start recording with 10 milliseconds of time between receiving 'ondataavailable' events
            recorder.start(10);
            window.$("#record").css("display", "none");
            window.$("#stop").css("display", "block");
            // setTimeout to stop recording after 15 seconds
            //time = 15;
            //let timer = setInterval(function() {
                //time--;
                //if (time == 0) {
                    //recorder.stop();
                    //time = null;
                    //clearInterval(timer);
                //}
            //}, 1000);
        }).catch(console.error);
    }

    function stop() {
        recorder.stop();
        window.$("#stop").css("display", "none");
        window.$("#generate").css("display", "block");
    }

    function generateQuestion() {
        let randomIndex = Math.floor(Math.random() * questions.length);
        question = questions[randomIndex];
        window.$("#generate").css("display", "none");
        window.$("#record").css("display", "block");
    }

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
        <div id="signout">Sign Out</div>
    </nav>
    <div id="content">
        <div id="buttons">
            <button on:click={generateQuestion} id="generate">Generate Random Question</button>
            <button on:click={record} id="record">Record</button>
            <button on:click={stop} id="stop">Stop</button>
            <p>Or</p>
            <form>
                <input type="file" id="audioFile" class="inputFile" name="audioFile" accept=".mp4, .webm">
	            <label for="audioFile">Upload audio <i class="fa fa-upload"></i></label>
            </form>
        </div>
        {#if question != null}
            <h1>Answer the following question in 15 seconds:</h1>
            <h3 style="margin-top: 10px;">{question}</h3>
        {/if}
        {#if time != null}
            <h1>Time left: {time} seconds</h1>
        {/if}
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

    h1 {
        margin-top: 30px;
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

    #content {
        text-align: center;
        margin-top: 100px;
    }

    #buttons {
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    #record {
        display: none;
    }

    #stop {
        display: none;
    }

    .inputFile {
		width: 0.01px;
		height: 0.01px;
		opacity: 0;
		overflow: hidden;
		position: absolute;
		z-index: -1;
    }
    
	.inputFile + label {
		background-color: #5d95c4;
        outline: none;
        border-radius: 10px;
		display: inline-block;
		padding: 20px;
        cursor: pointer;
        margin: 0px 30px;
    }
    
	.inputFile:focus + label,
	.inputFile + label:hover {
		background-color: rgb(233, 246, 255);
	}
</style>