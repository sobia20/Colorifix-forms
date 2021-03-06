import Layout from "../components/Layout";
import PageNotFound from "../components/PageNotFound";
import FormSpecs from "../components/FormSpecs";
import Form from "../components/Form";

const routes = [
  { path: "/", redirect: "/forms" },
  {
    path: "/forms",
    component: Layout,
    children: [
      {
        path: "/",
        component: Form,
        props: true
      },
      {
        path: "/forms/:name",
        component: FormSpecs,
        name: "formspecs",
        props: true
      }
    ]
  },
  { path: "*", component: PageNotFound }
];

export default routes;
