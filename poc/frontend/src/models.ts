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

class Post implements Model {
    id: number;
    caption: string;
    media_url: string;
    media_score: number;
    caption_score: number;
    profile: SocialProfile;
    location: Location;
}

export { Post, SocialProfile, Location };
