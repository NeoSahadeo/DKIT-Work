# Front End Development Portfolio Website

> THE SITE IS OFFLINE! IT USES COPYRIGHTED MUSIC AND I DON'T WANT TO FREELY PROVIDE MATERIAL I DO NOT OWN.
> IF YOU WOULD LIKE TO DEMO THE SITE READ BELOW

# Instructions to DEMO the SITE

This is a small set of instructions that will tell you how to
demo the site

## 1. Gitlab Setup + Spotipy

You will need to create a Gitlab account and download your music.
This has only been test with [SpotDL](https://github.com/spotDL/spotify-downloader).

Alternatively you can download it with anything but the results of this are unknown.


## 2. After downloading music

**!IMPORTANT**

The repository should be set to public for the API to work.

After your music is downloaded, you will need to create a repo on Gitlab
and create an API access token for that repo. For more information on how
to do this see [Project Access Token Gitlab](https://docs.gitlab.com/user/project/settings/project_access_tokens/).

> Make sure you tick the **API** checkbox to give the token access control for the repo


Next you will also need your project ID. It's a dropdown which can be found next to the star and fork button
in the top right corner of the repository.

Once you've copied the access token and project ID you're ready for step 3.

## 3. Add token to site

If you've cloned the entire repo go to `/website/src/song_api.ts` and open this file

```typescript
const API_ENDPOINT = 'https://gitlab.com/api/v4/projects/64894188/';
const ACCESS_TOKEN = '';
```

- Change the number after projects to your project ID

- Change the access token the one you have created

## 4. Finished

CD into the website directory and install packages `pnpm i`

To run the site: `pnpm run dev`

Site url: `http://localhost:5173/`

## 4.1 Uploading

If you want to have a static site uploaded. Goto `website/src/shared.svelte.ts` and change this line to true.

```typescript
export const PROD = false;
```

Goto `website/src/utils.ts` and change this to your base url

```typescript
return 'https://mysql05.comp.dkit.ie/D00264604/oto/'; // This is mysql
```

# Authors

- [@Neo Sahadeo](https://github.com/NeoSahadeo/)
