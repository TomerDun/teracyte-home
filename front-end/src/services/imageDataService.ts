import { callApi } from "./apiService"

export async function fetchLatestImageData() {
    const res = await callApi("/images/latest", "GET")
    return res


}

export async function fetchNewImageData() {
    const res = await callApi("/images/check-new", "GET")
    return res.image
}

export async function fetchImageHistory() {
    const res = await callApi("/images/history", "GET")
    return res;
}