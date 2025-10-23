import { useState } from "react";
import { callApi } from "../services/apiService";
import { loginUser } from "../services/authService";
import { useNavigate } from "react-router";
import LoadingSpinner from "../components/misc/LoadingSpinner";

export default function LoginPage() {
    const [usernameInput, setUsernameInput] = useState('');
    const [passwordInput, setPasswordInput] = useState('');
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const navigate = useNavigate();

    async function onSubmit() {
        setLoading(true);
        const err = await loginUser(usernameInput, passwordInput);
        if (err) {
            setErrorMessage(err.message || 'Login failed. Please try again.');
        }
        else {
            console.log('login success');
            navigate('/');
        }

        setLoading(false);
    }

    return (
        <div id="login-page-container" className="w-full h-full flex justify-center items-center">
            <div id="login-form" className="w-[30%] flex flex-col items-center gap-5 bg-white p-8 rounded-lg shadow-md">
                <h1 className="text-xl font-semibold mb-10 text-gray-700">Please login to use the system</h1>

                <input type="text" name="username" id="username" value={usernameInput} onChange={e => setUsernameInput(e.target.value)} placeholder="username" className="border shadow-sm border-gray-300 p-1 rounded-md w-[70%] text-gray-600" />
                <input type="password" name="password" id="password" value={passwordInput} onChange={e => setPasswordInput(e.target.value)} placeholder="password" className="border border-gray-300 shadow-sm p-1 rounded-md w-[70%] text-gray-600" />

                <div id="button-row" className="mt-12 w-full">
                    <button onClick={onSubmit} className=" w-full bg-transparent text-blue-600 border border-blue-600 transition-all cursor-pointer hover:bg-gradient-to-r from-blue-500 to-blue-600 hover:text-white px-4 py-2 rounded hover:bg-blue-700">
                        Login
                    </button>
                </div>

                <div id="message-row">
                    <p id='error-message' className="p-2 text-sm text-red-500 font-semibold">
                        {loading ? <LoadingSpinner /> : errorMessage}
                    </p>
                </div>
            </div>
        </div>
    )
}