import type { Post } from "../models";
import { writable, Writable } from "svelte/store";

export class ListPresenter {
    
    // https://svelte.dev/tutorial/writable-stores
    posts: Writable<Post[]> = writable([]);

    refreshPosts() {
        fetch("/dev-api/posts")
            .then((response) => response.json())
            .then((data) => {
                this.posts.set(data);
            })
            .catch((err) => {
                console.log(err);
                this.posts.set([]);
            });
    }

    refresh() {
        this.posts.set(null);
        this.refreshPosts();
    }

}
