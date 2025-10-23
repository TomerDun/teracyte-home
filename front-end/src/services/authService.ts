import { callApi } from "./apiService";

export async function loginUser(username: string, password: string) {
    try {
        const body = { username, password };
        const data = await callApi('/auth/login', 'POST', body, false);

        // Update localhost
        localStorage.setItem('apiToken', data.access_token);
        localStorage.setItem('username', username);

        return true;
    }
    catch (err) {
        return err;
    }
}