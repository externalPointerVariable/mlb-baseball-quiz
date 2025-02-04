import { StrictMode } from "react";
import React from "react";
import { createRoot } from "react-dom/client";
import "./index.css";

import ReactDOM from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";

import App from "./App.jsx";
import Login from "./pages/login.jsx";
import Quiz from "./pages/Quiz.jsx";
import Home from "./pages/Home.jsx";
import Error from "./pages/Error.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: "/",
        element: <Login />,
        errorElement: <Error />,
      },
      {
        path: "/quiz",
        element: <Quiz />,
        errorElement: <Error />,
      },
      {
        path: "/Home",
        element: <Home />,
        errorElement: <Error />,
      },
    ],
  },
]);

createRoot(document.getElementById("root")).render(
  <>
    <RouterProvider router={router} />
  </>
);
