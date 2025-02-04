import { useState, useEffect } from "react";
import {
  FaTrophy,
  FaCrown,
  FaSearch,
  FaChartLine,
  FaMedal,
  FaUserCircle,
  FaPlay,
  FaChevronDown,
} from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import { baseurl } from "../secret.js";

const QuizStart = ({ user_id }) => {
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState("");
  const [sortBy, setSortBy] = useState("rank");
  const [selectedLeague, setSelectedLeague] = useState("");
  const [selectedTeam, setSelectedTeam] = useState("");
  const [selectedPlayer, setSelectedPlayer] = useState("");
  const [leagues, setLeagues] = useState([]);
  const [teams, setTeams] = useState([]);
  const [players, setPlayers] = useState([]);

  const getTeamsId = (teamName) => {
    const team = teams.find((team) => team.name === teamName);
    return team.id;
  };

  const fetchPlayers = async (teamName) => {
    const teamId = getTeamsId(teamName);
    try {
      const response = await fetch(
        `https://statsapi.mlb.com/api/v1/teams/${teamId}/roster`
      );
      const data = await response.json();
      setPlayers(data.roster);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  useEffect(() => {
    async function fetchLeages() {
      try {
        const response = await fetch(
          "https://statsapi.mlb.com/api/v1/league?sportId=1"
        );
        const data = await response.json();
        setLeagues(data.leagues);
      } catch (error) {
        console.error("Error:", error);
      }
    }
    fetchLeages();

    async function fetchTeams() {
      try {
        const response = await fetch(
          "https://statsapi.mlb.com/api/v1/teams?sportId=1"
        );
        const data = await response.json();
        setTeams(data.teams);
      } catch (error) {
        console.error("Error:", error);
      }
    }
    fetchTeams();
  }, []);

  useEffect(() => {
    if (selectedTeam) {
      fetchPlayers(selectedTeam);
    }
  }, [selectedTeam]);

  const quizstarthandler = (e) => {
    e.preventDefault();
    console.log("Starting quiz...");
    navigate("/quiz", {
      state: {
        league: selectedLeague,
        team: selectedTeam,
        player: selectedPlayer,
        user_id: user_id,
      },
    });
  };

  return (
    <>
      {/* Quiz Start Section */}
      <div className="mb-8 bg-white rounded-2xl shadow-xl p-8">
        <h2 className="text-3xl font-bold text-gray-800 mb-6 flex items-center">
          <FaPlay className="mr-3 text-indigo-600" />
          Start New Quiz
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {/* League Selector */}
          <div className="relative">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Select League
            </label>
            <div className="relative">
              <select
                value={selectedLeague}
                onChange={(e) => setSelectedLeague(e.target.value)}
                className="w-full pl-4 pr-10 py-3 border-2 border-gray-200 rounded-xl appearance-none focus:border-indigo-500 focus:outline-none"
              >
                <option value="">Choose League</option>
                {leagues.map((league) => (
                  <option key={league.id} value={league.name}>
                    {league.name}
                  </option>
                ))}
              </select>
              <FaChevronDown className="absolute right-4 top-4 text-gray-400 pointer-events-none" />
            </div>
          </div>

          {/* Team Selector */}
          <div className="relative">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Select Team
            </label>
            <div className="relative">
              <select
                value={selectedTeam}
                onChange={(e) => setSelectedTeam(e.target.value)}
                className="w-full pl-4 pr-10 py-3 border-2 border-gray-200 rounded-xl appearance-none focus:border-indigo-500 focus:outline-none"
                disabled={!selectedLeague}
              >
                <option value="">Choose Team</option>
                {teams.map((team) => (
                  <option key={team.id} value={team.name}>
                    {team.name}
                  </option>
                ))}
              </select>
              <FaChevronDown className="absolute right-4 top-4 text-gray-400 pointer-events-none" />
            </div>
          </div>

          {/* Player Selector */}
          <div className="relative">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Select Player
            </label>
            <div className="relative">
              <select
                value={selectedPlayer}
                onChange={(e) => setSelectedPlayer(e.target.value)}
                className="w-full pl-4 pr-10 py-3 border-2 border-gray-200 rounded-xl appearance-none focus:border-indigo-500 focus:outline-none"
                disabled={!selectedTeam}
              >
                <option value="">Choose Player</option>
                {players.map((player) => (
                  <option key={player.person.id} value={player.person.fullName}>
                    {player.person.fullName}
                  </option>
                ))}
              </select>
              <FaChevronDown className="absolute right-4 top-4 text-gray-400 pointer-events-none" />
            </div>
          </div>
        </div>

        {/* Start Button */}
        <div className="mt-6 flex justify-end">
          <button
            onClick={quizstarthandler}
            className={`flex items-center px-8 py-3 rounded-xl text-white transition-all ${
              selectedLeague && selectedTeam && selectedPlayer
                ? "bg-indigo-600 hover:bg-indigo-700"
                : "bg-gray-400 cursor-not-allowed"
            }`}
            disabled={!selectedLeague || !selectedTeam || !selectedPlayer}
          >
            Start Quiz Now!
            <FaPlay className="ml-2 text-sm" />
          </button>
        </div>
      </div>
    </>
  );
};

export default QuizStart;
