export const API_BASE_URL = 'http://localhost:8000/api';
import type { HttpMethod } from '../types/apiTypes';


export async function callApi(endpoint: string, method: HttpMethod, body?: any, addAuthHeader: boolean = true) {
    const url = API_BASE_URL + endpoint;
    const reqBody = body ? JSON.stringify(body) : null;
    const headers: Record<string, string> = {
        'Content-Type': 'application/json',
    };
    // if (addAuthHeader) {
    //     //TODO: Add auth headers
    // }

    const res = await fetch(url, {
        method,
        headers,
        body: reqBody,
    });

    // TODO: Add status code to error
    if (!res.ok) {
        const err = new Error('Api Call Erorr')
        err.message = await res.text();
        throw err;
    }

    return await res.json();
}

