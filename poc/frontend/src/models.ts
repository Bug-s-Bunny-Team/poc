interface Model {
    id: number;
}

class SocialProfile implements Model {
    id: number;
    username: string;
}

class Location implements Model {
    id: number;
    name: string;
    lat: number;
    long: number;
    score: number;
}

class PostScore {
    media_score: number;
    caption_score: number;
}

class Post implements Model {
    id: number;
    caption: string;
    media_url: string;
    profile: SocialProfile;
    location: Location | null;
    score: PostScore | null;
}

export { Post, SocialProfile, Location };
