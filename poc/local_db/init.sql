

Editing diagram bugsbunnyteam/poc_db
Explore
bugsbunnyteam
Log out

CREATE TABLE "location" (
  "id" SERIAL PRIMARY KEY,
  "score" DOUBLE PRECISION
);

CREATE TABLE "socialprofile" (
  "id" SERIAL PRIMARY KEY,
  "username" TEXT NOT NULL
);

CREATE TABLE "post" (
  "id" SERIAL PRIMARY KEY,
  "social_profile" INTEGER NOT NULL,
  "media_type" TEXT NOT NULL,
  "media_s3_key" TEXT NOT NULL,
  "location" INTEGER
);

CREATE INDEX "idx_post__location" ON "post" ("location");

CREATE INDEX "idx_post__social_profile" ON "post" ("social_profile");

ALTER TABLE "post" ADD CONSTRAINT "fk_post__location" FOREIGN KEY ("location") REFERENCES "location" ("id") ON DELETE SET NULL;

ALTER TABLE "post" ADD CONSTRAINT "fk_post__social_profile" FOREIGN KEY ("social_profile") REFERENCES "socialprofile" ("id") ON DELETE CASCADE;

CREATE TABLE "postscore" (
  "id" SERIAL PRIMARY KEY,
  "post" INTEGER NOT NULL,
  "media_score" DOUBLE PRECISION NOT NULL,
  "caption_score" DOUBLE PRECISION
);

CREATE INDEX "idx_postscore__post" ON "postscore" ("post");

ALTER TABLE "postscore" ADD CONSTRAINT "fk_postscore__post" FOREIGN KEY ("post") REFERENCES "post" ("id");

CREATE TABLE "socialprofile_suggested_profiles" (
  "socialprofile" INTEGER NOT NULL,
  "socialprofile_2" INTEGER NOT NULL,
  PRIMARY KEY ("socialprofile", "socialprofile_2")
);

CREATE INDEX "idx_socialprofile_suggested_profiles" ON "socialprofile_suggested_profiles" ("socialprofile_2");

ALTER TABLE "socialprofile_suggested_profiles" ADD CONSTRAINT "fk_socialprofile_suggested_profiles__socialprofile" FOREIGN KEY ("socialprofile") REFERENCES "socialprofile" ("id");

ALTER TABLE "socialprofile_suggested_profiles" ADD CONSTRAINT "fk_socialprofile_suggested_profiles__socialprofile_2" FOREIGN KEY ("socialprofile_2") REFERENCES "socialprofile" ("id")

