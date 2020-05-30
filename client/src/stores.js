import {writable} from "svelte/store";

export const page = writable("Home");
export const loggedIn = writable(false);
export const currentUser = writable(null);
export const userEmail = writable("");
export const questions = ["Tell me about yourself.", "What is your greatest accomplishment?", "What is your strongest skill?"];