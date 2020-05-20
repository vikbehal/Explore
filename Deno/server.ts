import { serve } from "https://deno.land/std/http/server.ts";

const serv = serve({ port: 4300 });

for await (const req of serv) {
    req.respond({ body: "hey Server!" });
}
