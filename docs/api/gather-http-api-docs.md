# Gather HTTP API

<aside>
⚠️ WARNING: This API and the map data format are in beta, and are still changing. We will try to send out a heads up via the [forum](https://forum.gather.town/c/developers/api-questions/9) before making any breaking changes.

</aside>

# Setup

Generate an API key for yourself at https://gather.town/apiKeys — you’ll need it for all of the following.

Also, you must have Admin or Builder permissions on the space you’re trying to modify.

# API Endpoints

<aside>
⚠️ NOTE: forward slashes in `spaceId` need to be replaced by backslashes (e.g. `dkj63wrer8/spaceName` becomes `dkj63wrer8\spaceName`)
(also see: [⚠️ `\` and URL encodings](https://www.notion.so/and-URL-encodings-d3d3dd3d72c544a79fcafa4c68e85534?pvs=21))

</aside>

## POST **https://api.gather.town**/api/v2/spaces

For creating new spaces, which always starts by copying a template space

### Params

**Body**

- `name`: Name of space you want to create
- `sourceSpace`: `spaceId` of the space to copy maps out of
- `reason` (optional): determines which usecase-specific features are enabled, e.g. `"Coworkers / remote team"` for remote work features.

**Headers**

- `apiKey`: Your API key

### Example (NodeJS, axios)

```jsx
axios.post(
  "https://api.gather.town/api/v2/spaces",
  {
    sourceSpace: SPACE_ID,
    name: "my new space",
  },
  {
    headers: {
      apiKey: API_KEY,
    },
  }
)
```

(taken from https://github.com/gathertown/api-examples/blob/main/create-space.js)

### Returns

SpaceId of the newly created space, but with a `/` instead of `\` so you can append it to [`https://gather.town`](https://gather.town) and enter.

## GET https://api.gather.town/api/v2/spaces/:spaceId/maps/:mapId

For getting map data

### **Params**

in the URL path:

- spaceId: id of the space for the map you want to get the contents of (URL encoded: see [⚠️ `\` and URL encodings](https://www.notion.so/and-URL-encodings-d3d3dd3d72c544a79fcafa4c68e85534?pvs=21))
- mapId: id of the map within that space (also URL encoded)

headers:

- apiKey: Your API key

### **Example (NodeJS, axios)**

```jsx
axios.get(
  `https://api.gather.town/api/v2/spaces/${encodeURIComponent(SPACE_ID)}/maps/${encodeURIComponent(MAP_ID)}`,
  {
    headers: {
      apiKey: API_KEY,
    },
  }
)
```

(taken from https://github.com/gathertown/api-examples/blob/main/get-map.js)

### **Returns**

JSON of the map data (see: [[DRAFT] Gather Map Data Format](https://www.notion.so/DRAFT-Gather-Map-Data-Format-80a4e90813f441ea8245c62024b454fc?pvs=21))

## POST https://api.gather.town/api/v2/spaces/:spaceId/maps/:mapId

For setting the contents of a map

### **Params**

in the URL path:

- spaceId: id of the space for the map you want to get the contents of (URL encoded: see [⚠️ `\` and URL encodings](https://www.notion.so/and-URL-encodings-d3d3dd3d72c544a79fcafa4c68e85534?pvs=21))
- mapId: id of the map within that space (also URL encoded)

headers:

- apiKey: Your API key

Body:

- `content`: The map data you want to set. Same format as returned from `GET /spaces/:spaceId/map/:mapId` ([[DRAFT] Gather Map Data Format](https://www.notion.so/DRAFT-Gather-Map-Data-Format-80a4e90813f441ea8245c62024b454fc?pvs=21))

### Example (NodeJS, axios)

```jsx
axios.post(
  `https://api.gather.town/api/v2/spaces/${encodeURIComponent(SPACE_ID)}/maps/${encodeURIComponent(MAP_ID)}`,
  {
    content: {
      // example map data -- but you can set much more than this
      backgroundImagePath: "https://cdn.gather.town/storage.googleapis.com/gather-town.appspot.com/uploads/SWaZgxCQMTE6C1lq/pq1oi59fnOqkAYD3Td7u0B",
    },
  },
  {
    headers: {
      apiKey: API_KEY,
    },
  }
)
```

(from https://github.com/gathertown/api-examples/blob/main/set-map.js)

### Returns

Nothing, just status code, or an error.

## GET  https://api.gather.town/api/getEmailGuestlist

For getting the email guestlist for a space

**Takes**

URLEncoded

- apiKey: Your API key
- spaceId: Id of the space you want the guestlist for

**Returns** 

JSON Encoded guestlist, which is an object keyed by email address with object values, with possible string fields name, affiliation, and role for each value

## POST  https://api.gather.town/api/setEmailGuestlist

For setting the email guestlist of a space

**Takes**

JSON Encoded

- apiKey: Your API key
- spaceId: Id of the space you want the guestlist for
- guestlist: an object keyed by email address with object values, with possible string fields name, affiliation, and role for each value
- overwrite (optional): Boolean, true to overwrite the guestlist, false to append/update. False by default

**Returns** nothing

**Example**

```jsx
axios.post("https://api.gather.town/api/setEmailGuestlist", {
  // replace with your data
  apiKey: "yOurAPiKeyHerE",
  spaceId: "rAnDOmchArs\\SpaceName",
  guestlist: {"example@email.com":{"name":"Dr. Example","affiliation":"test","role":""}},
  overwrite: true,
})
```

# Gotchas

## ⚠️ `\` and URL encodings

Many characters need to be escaped when passed as URL params. An incomplete list of gotchas:

- `\` does NOT need to be escaped in the query, but might be for whatever you're using to send the query. E.g. in JS, you'd still have to `fetch('https://gather.town/api/whatever?spaceId=0123456789abcdef\\spaceName')`
- `` (space) should be `%20` (sometimes handled by client you're using)
- etc

an example of a properly formatted query URL is [`https://api.gather.town/api/v2/spaces/SWaZgyCQMTE6C1lq\The Dark Sun/maps/test`](https://api.gather.town/api/v2/spaces/SWaZgyCQMTE6C1lq%5CThe%20Dark%20Sun/maps/test) (for spaceId `SWaZgyCQMTE6C1lq\The Dark Sun` )

## `Content-Type`

you may have to be explicitly set to `application/json`

## CORS for Image URLs

When using setMap, some fields take an image URL which you may be tempted to set as a URL external to Gather. You can do this, but there's one important thing to know here, which is that you need to properly set CORS headers for the external resource to allow "gather.town" and "*.gather.town"

More information on CORS here: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

## sounds

There is a known bug where deleting an object with a `sound` does not end the sound for people already in the space. The workaround is to first set the `sound.src` to null, and then delete the object.

# Usage Examples/Inspiration

### Some example code

right now, just some basic and intermediate map reads and writes

code: https://github.com/gathertown/api-examples

### NeurIPS automation

This was a big conference. They auto-generated a lot of poster sessions, and have graciously open sourced their scripts. No promises on usability or how up to date they are

code: https://github.com/Mini-Conf/Mini-Conf/tree/master/gather

### Old password door (uses http api only)

Door that adds and removes wall tiles to simulate a password protected door.

code: https://github.com/gathertown/door-by-api

# More Questions

Post in our [developer forum](https://forum.gather.town/c/developers/api-questions/9) with any questions!