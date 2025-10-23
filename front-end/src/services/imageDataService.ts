import { callApi } from "./apiService"

export async function fetchLatestImageData() {
    const res = await callApi("/images/latest", "GET")
    return res
}

export async function fetchNewImageData() {
    try {
        const res = await callApi("/images/check-new", "GET")
        return res.image
    }
    catch (err) {
        console.log(err);        
    }
}