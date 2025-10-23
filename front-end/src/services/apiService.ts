export const API_BASE_URL = 'http://localhost:8000/api';
export const SERVER_BASE_URL = 'http://localhost:8000';
import type { HttpMethod } from '../types/apiTypes';


export async function callApi(endpoint: string, method: HttpMethod = 'GET', body?: any, addAuthHeader: boolean = true) {
    const url = API_BASE_URL + endpoint;
    const reqBody = body ? JSON.stringify(body) : null;
    const headers: Record<string, string> = {
        'Content-Type': 'application/json',
    };
    if (addAuthHeader) {
        const token = localStorage.getItem('apiToken');
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }
    }

    const res = await fetch(url, {
        method,
        headers,
        body: reqBody,
    });

    // TODO: Add status code to error
    if (!res.ok) {
        const err = new Error('Api Call Erorr')
        err.message = await res.json();
        err.cause = res.status
        throw err;
    }

    return await res.json();
}

