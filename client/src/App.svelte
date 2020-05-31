<script>
	import Home from "./components/Home.svelte";
	import History from "./components/History.svelte";
	import Auth from "./components/Auth.svelte";
	import { page, loggedIn, currentUser, userEmail } from "./stores.js";

	let currentPage;
	let logged;
	let user;

	const unsubscribe1 = page.subscribe(val => {
		currentPage = val;
	});

	const unsubsribe2 = loggedIn.subscribe(val => {
		logged = val;
	});

</script>

<main>
	{#if logged}
		{#if currentPage == "Home"}
			<Home></Home>
			{:else}
			<History></History>
		{/if}
	{:else}
		<Auth></Auth>
	{/if}
</main>

<style>
	main {
		text-align: center;
	}
</style>