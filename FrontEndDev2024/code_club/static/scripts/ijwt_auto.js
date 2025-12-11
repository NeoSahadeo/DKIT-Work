import { iJWT } from "./ijwt.js";
const ijwt = new iJWT({
  mode: "production",
  site_base: "/D00264604/code_club/",
});
ijwt.update_dom();
