import MetadataCard from "../components/HomeArea/MetadataCard";
import ImageDisplayCard from "../components/HomeArea/ImageDisplayCard";
import Histogram from "../components/HomeArea/Histogram";
import { useEffect, useState } from "react";
import type { ImageMetadata } from "../types/imageDataTypes";
import { fetchLatestImageData, fetchNewImageData } from "../services/imageDataService";
import LoadingSpinner from "../components/misc/LoadingSpinner";

export default function HomePage() {
    const [imageMetadata, setImageMetadata] = useState<ImageMetadata | null>(null);
    const [imageFilePath, setImageFilePath] = useState<string | null>(null);
    const [histogramData, setHistogramData] = useState<number[] | null>(null);

    useEffect(() => {
        if (localStorage.getItem("apiToken")) {
            getImageData();
        }
    }, [])

    useEffect(() => {
        const pollingInterval = 10000;

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
        }
        else {
            console.log('no new image data found');
        }
    }

    async function getImageData() {
        const res = await fetchLatestImageData();
        console.log(res);
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
    }
    return (
        <div id="home-page-container" className="h-full">
            <div id="header-container" className="">
                Image Analytics Dashboard
            </div>
            <div id="main-container" className="flex gap-4 h-full">

                <div id="metadata-container" className="h-full w-[20%]">
                    <MetadataCard metadata={imageMetadata} />
                </div>
                <div id="display-container" className="h-full w-[50%]">
                    <ImageDisplayCard imageFilePath={imageFilePath} />
                </div>
                <div id="charts-container" className="h-full w-[30%]">
                    {histogramData ? <Histogram histogram={histogramData} /> : <LoadingSpinner size={12}/>}
                </div>
            </div>
        </div>
    )

}