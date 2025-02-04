import { useState } from "react";
import { FaGoogle, FaApple, FaTwitter, FaEnvelope } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { baseurl } from "../secret.js";

const AuthForm = () => {
  const navigate = useNavigate();
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [username, setUsername] = useState("");

  const loginhandle = () => {
    let userid = null;
    console.log("Logging in...");

    axios
      .post(`${baseurl}/api/login/`, {
        username: username,
        password: password,
      })
      .then((response) => response.data)
      .then((data) => {
        navigate("/home", { state: { id: data.user_id } });
      })
      .catch((error) => {
        if (error.response) {
          alert(error.response.data.error);
          console.log(error.response);
        }
      });
  };

  const signuphandle = () => {
    console.log("Signing up...");
    axios
      .post(`${baseurl}/api/users/`, {
        username: username,
        password: password,
        email: email,
        favourite_team: "sd",
        favourite_player: "bsaxc",
      })
      .then((response) => response.data)
      .then((data) => {
        navigate("/home", { state: { id: data.user_id } });
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          alert(JSON.stringify(error.response.data));
        }
      });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (isLogin) {
      loginhandle();
    } else {
      signuphandle();
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8">
        {/* Logo */}
        <div className="flex items-center justify-center mb-8">
          <div className="bg-indigo-600 text-white rounded-full p-3">
            <svg
              className="w-8 h-8"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M18.364 5.636L16.95 7.05A7 7 0 0012 5a7 7 0 00-4.95 2.05L5.636 5.636M18.364 5.636a9 9 0 010 12.728M5.636 5.636a9 9 0 000 12.728M13.828 10.172l-4.243 4.243m0 0l-1.414-1.414"
              />
            </svg>
          </div>
          <h1 className="ml-2 text-2xl font-bold text-gray-800">
            Baseball Quiz
          </h1>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-6">
          {!isLogin && (
            <div>
              <label className="block text-gray-700 text-sm font-semibold mb-2">
                Email
              </label>
              <input
                type="text"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-indigo-500"
                placeholder=""
              />
            </div>
          )}
          <div>
            <label className="block text-gray-700 text-sm font-semibold mb-2">
              User Name
            </label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-indigo-500"
              placeholder=""
            />
          </div>
          <div>
            <label className="block text-gray-700 text-sm font-semibold mb-2">
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-indigo-500"
              placeholder=""
            />
          </div>

          <button
            type="submit"
            className="w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700 transition duration-300"
          >
            {isLogin ? "Sign In" : "Sign Up"}
          </button>
        </form>

        {/* Toggle between Login/Signup */}
        <p className="mt-8 text-center text-gray-600">
          {isLogin ? "Don't have an account?" : "Already have an account?"}{" "}
          <button
            onClick={() => setIsLogin(!isLogin)}
            className="text-indigo-600 hover:text-indigo-800 font-semibold"
          >
            {isLogin ? "Sign up" : "Sign in"}
          </button>
        </p>
      </div>
    </div>
  );
};

export default AuthForm;
