import MetadataCard from "../components/HomeArea/MetadataCard";
import ImageDisplayCard from "../components/HomeArea/ImageDisplayCard";
import Histogram from "../components/HomeArea/Histogram";
import { useEffect, useState } from "react";
import type { ImageHistoryItemType, ImageMetadata } from "../types/imageDataTypes";
import { fetchImageHistory, fetchLatestImageData, fetchNewImageData } from "../services/imageDataService";
import LoadingSpinner from "../components/misc/LoadingSpinner";
import { useNavigate } from "react-router";
import ImageHistoryCard from "../components/HistoryArea/ImageHistoryCard";

export default function HomePage() {
    const [imageMetadata, setImageMetadata] = useState<ImageMetadata | null>(null);
    const [imageFilePath, setImageFilePath] = useState<string | null>(null);
    const [histogramData, setHistogramData] = useState<number[] | null>(null);
    const [imageHistory, setImageHistory] = useState<ImageHistoryItemType[]>([]);

    const navigate = useNavigate();

    useEffect(() => {
        getImageData();
        getImageHistory();

    }, [])

    useEffect(() => {
        const pollingInterval = 30000;

        const interval = setInterval(() => {
            pollNewImageData();
        }, pollingInterval);

        console.log(`Started polling every ${pollingInterval} ms`);


        return () => {
            clearInterval(interval);
            console.log("polling interval cleared");
        }
    }, []);

    async function pollNewImageData() {
        try {
            const res = await fetchNewImageData();
            if (res) {
                console.log('found new image data, updating...');

                const newMetadata: ImageMetadata = {
                    tc_image_id: res.tc_image_id,
                    created_at: res.created_at,
                    intensity_average: res.intensity_average,
                    classification_label: res.classification_label,
                    focus_score: res.focus_score,
                }
                const newImagePath = res.raw_image_path;

                setHistogramData(res.histogram)
                setImageMetadata(newMetadata);
                setImageFilePath(newImagePath);

                getImageHistory(); // update image history when new image is retrieved
            }
            else {
                console.log('no new image data found');
            }
        } catch (err: any) {
            if (err.cause === 401) {
                console.log("Unauthorized access - redirecting");
                navigate("/login");
            }
        }
    }

    async function getImageData() {
        try {
            const res = await fetchLatestImageData();
            const newMetadata: ImageMetadata = {
                tc_image_id: res.tc_image_id,
                created_at: res.created_at,
                intensity_average: res.intensity_average,
                classification_label: res.classification_label,
                focus_score: res.focus_score,
            }
            const newImagePath = res.raw_image_path;

            setHistogramData(res.histogram)
            setImageMetadata(newMetadata);
            setImageFilePath(newImagePath);
        } catch (err: any) {
            if (err.cause === 401) {
                console.log("Unauthorized access - redirecting");
                navigate("/login");
            }
        }
    }

    async function getImageHistory() {
        try {
            const res = await fetchImageHistory();
            setImageHistory(res);
        } catch (err: any) {
            if (err.cause === 401) {
                console.log("Unauthorized access - redirecting");
                navigate("/login");
            }
        }
    }


    return (
        <div id="home-page-container" className="h-full">
            <div id="header-container" className="text-center mb-6">
                <h1>Image Analytics Dashboard</h1>
            </div>
            <div id="main-container" className="flex gap-4 h-full">

                <div id="metadata-container" className="h-full w-[15%] min-w-[250px]">
                    <MetadataCard metadata={imageMetadata} />
                </div>
                <div id="display-container" className="h-full w-[45%]">
                    <ImageDisplayCard imageFilePath={imageFilePath} />
                </div>
                <div id="charts-container" className="h-full w-[35%] bg-white rounded-xl border border-gray-200">
                    {histogramData ? <Histogram histogram={histogramData} /> : <div className="h-full flex justify-center items-center"><LoadingSpinner size={12} /></div>}
                </div>

                <div id="history-container" className="w-[20%]">
                    <ImageHistoryCard imageHistory={imageHistory} />
                </div>
            </div>
        </div>
    )

}