import { callApi } from "./apiService"

export async function fetchLatestImageData() {
    const response = await callApi("/images/latest", "GET")
    return response
}