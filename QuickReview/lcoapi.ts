import { Application, Router } from "https://deno.land/x/oak/mod.ts";

interface Course {
    name: string;
    price: number;
    certification: boolean;
}

let courses: Array<Course> = [
    {
        name: "Machine learning",
        price: 1.0,
        certification: false
    },
    {
        name: "Deep learning",
        price: 2.0,
        certification: false
    }
];

export const getCourses = (
    { response }: {
        response: any
    }
) => {
    response.body = courses;
}

export const addCourses = async (
    { request, response }: {
        request: any;
        response: any;
    }
) => {
    const body = await request.body();
    const course: Course = body.value;

    courses.push(course);
    response.body = { courseAdded: "Success" };
    response.status = 200;
};

const router = new Router();
const app = new Application();
const PORT = 4300;

router
    .get("/learn", getCourses)
    .post("/create", addCourses);

app.use(router.routes());
app.use(router.allowedMethods());

await app.listen({port: 8000});