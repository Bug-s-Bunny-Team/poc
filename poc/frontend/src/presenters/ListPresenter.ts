import type { Post } from "../models";

export class ListPresenter {
   
    posts: Array<Post> = [];

    refreshPosts() {
        console.log("Sono dentro refreshPost");
        fetch("/dev-api/posts")
            .then((response) => response.json())
            .then((data) => {
                this.posts = data;
            })
            .catch((err) => {
                console.log(err);
                this.posts = [];
            });
    }

}
