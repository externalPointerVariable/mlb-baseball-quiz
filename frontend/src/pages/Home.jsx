import { useState, useEffect } from "react";
import {
  FaTrophy,
  FaCrown,
  FaSearch,
  FaChartLine,
  FaMedal,
  FaUserCircle,
} from "react-icons/fa";
import QuizStart from "./QuizStart.jsx";
import axios from "axios";
import { useLocation } from "react-router-dom";
import { baseurl } from "../secret.js";

const HomePage = () => {
  const location = useLocation();

  const currentuserid = location.state.id ?? {};
  console.log(`Current User ID: ${currentuserid}`);

  const [searchQuery, setSearchQuery] = useState("");
  const [sortBy, setSortBy] = useState("rank");
  const [leaderboard, setleaderboard] = useState([]);
  const [currentUser, setcurrentUser] = useState({});
  const [rank, setRank] = useState(15);

  const getuserrank = () => {
    let pos = 0;
    leaderboard.forEach((user) => {
      if (user.username === currentUser.username) {
        pos = user.rank;
      }
    });
    setRank(pos);
  };

  useEffect(() => {
    console.log("Fetching user data...");
    axios
      .post(`${baseurl}/api/profile/`, {
        user_id: currentuserid,
      })
      .then((response) => response.data)
      .then((data) => {
        setcurrentUser(data[0]);
        // console.log(`currentuser:${currentUser}`);
      })
      .catch((error) => {
        console.log("Error fetching user data");

        console.log(`Error: ${error}`);
      });
  }, []);

  useEffect(() => {
    console.log("Fetching leaderboard data...");

    axios
      .get(`${baseurl}/api/leaderboard/`)
      .then((response) => response.data)
      .then((data) => {
        // console.log(data);
        data.sort((a, b) => parseInt(b.score) - parseInt(a.score));
        setleaderboard(data.map((obj, inx) => ({ ...obj, rank: inx + 1 })));
      })
      .catch((error) => {
        alert("Error fetching leaderboard");
        console.log(error);
      });
  }, []);

  useEffect(() => {
    getuserrank();
  }, [leaderboard]);

  // const currentUser = {
  //   username: "BaseballPro99",
  //   points: 2450,
  //   rank: 15,
  //   achievements: [
  //     "⚡ 10 Win Streak",
  //     "🏆 Rookie Champion",
  //     "🎯 Precision Expert",
  //   ],
  //   recentActivity: [
  //     "Completed Yankees Quiz (95%)",
  //     "Earned 200 points",
  //     "Reached Rank 15",
  //   ],
  //   avatar: null,
  // };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-100 to-gray-200 p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8 bg-indigo-600 text-white rounded-2xl p-6 shadow-xl">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold">
                Welcome Back, {currentUser.username}!
              </h1>
              <p className="mt-2 opacity-90">Your Baseball Knowledge Hub</p>
            </div>
            <div className="flex items-center space-x-4 bg-white/10 p-4 rounded-xl">
              <FaUserCircle className="w-12 h-12" />
              <div>
                <p className="text-sm opacity-90">Current Rank</p>
                <div className="flex items-center space-x-2">
                  <FaCrown className="text-yellow-400" />
                  <span className="text-2xl font-bold">#{rank}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* User Profile Section */}
          <div className="lg:col-span-1 space-y-6">
            {/* Stats Card */}
            <div className="bg-white rounded-2xl p-6 shadow-lg">
              <h2 className="text-xl text-indigo-600 font-bold mb-4 flex items-center">
                <FaChartLine className="mr-2 text-indigo-600" />
                Your Stats
              </h2>
              <div className="space-y-4">
                <div className="flex text-indigo-600 justify-between items-center">
                  <span>Total Points</span>
                  <span className="font-bold text-indigo-600">
                    {currentUser.user_performance}
                  </span>
                </div>
                <div className="flex text-indigo-600 justify-between items-center">
                  <span>Global Rank</span>
                  <span className="font-bold">#{rank}</span>
                </div>
                {/* <div className="pt-4">
                  <div className="flex text-indigo-600 justify-between mb-2 text-sm">
                    <span>Next Rank Progress</span>
                    <span>65%</span>
                  </div>
                  <div className="h-2 bg-gray-200 rounded-full">
                    <div
                      className="h-2 bg-indigo-600 rounded-full transition-all duration-300"
                      style={{ width: "65%" }}
                    />
                  </div>
                </div> */}
              </div>
            </div>
            <QuizStart user_id={currentuserid} />

            {/* Achievements */}
            {/* <div className="bg-white rounded-2xl p-6 shadow-lg">
              <h2 className="text-xl font-bold mb-4 flex items-center">
                <FaMedal className="mr-2 text-yellow-500" />
                Recent Achievements
              </h2>
              <div className="space-y-3">
                {currentUser.achievements.map((achievement, index) => (
                  <div
                    key={index}
                    className="flex items-center p-3 bg-gray-50 rounded-lg"
                  >
                    <span className="text-lg mr-2">
                      {achievement.split(" ")[0]}
                    </span>
                    <span className="text-sm">
                      {achievement.split(" ").slice(1).join(" ")}
                    </span>
                  </div>
                ))}
              </div>
            </div> */}
          </div>
          {/* Leaderboard Section */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl text-indigo-600 font-bold flex items-center">
                  <FaTrophy className="mr-2 text-yellow-500" />
                  Global Leaderboard
                </h2>
                <div className="flex items-center space-x-4">
                  <div className="relative">
                    <FaSearch className="absolute left-3 top-3 text-gray-400" />
                    <input
                      type="text"
                      placeholder="Search users..."
                      className="pl-10 pr-4 py-2 border rounded-lg"
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                    />
                  </div>
                  <select
                    className="border rounded-lg px-4 py-2"
                    value={sortBy}
                    onChange={(e) => setSortBy(e.target.value)}
                  >
                    <option value="rank">Rank</option>
                    <option value="name">Name</option>
                    <option value="score">Score</option>
                  </select>
                </div>
              </div>

              {/* Leaderboard Table */}
              <div className="space-y-4">
                {leaderboard.map((user) => (
                  <div
                    key={user.rank}
                    className={`flex text-indigo-600 items-center justify-between p-4 rounded-xl transition-all ${
                      user.username === currentUser.username
                        ? "bg-indigo-50 border-2 border-indigo-200"
                        : "hover:bg-gray-50"
                    }`}
                  >
                    <div className="flex items-center space-x-4">
                      <span
                        className={`font-bold w-8 ${
                          user.rank === 1
                            ? "text-yellow-500"
                            : user.rank === 2
                            ? "text-gray-400"
                            : user.rank === 3
                            ? "text-amber-600"
                            : "text-gray-600"
                        }`}
                      >
                        #{user.rank}
                      </span>
                      <FaUserCircle className="w-8 h-8 text-gray-400" />
                      <div>
                        <h3 className="font-semibold">{user.username}</h3>
                        <p className="text-sm text-gray-500">
                          {user.user_performance} points
                        </p>
                      </div>
                    </div>
                    <div className="flex items-center space-x-2">
                      {user.trend === "up" && (
                        <FaChartLine className="text-green-500" />
                      )}
                      {user.trend === "down" && (
                        <FaChartLine className="rotate-180 text-red-500" />
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
