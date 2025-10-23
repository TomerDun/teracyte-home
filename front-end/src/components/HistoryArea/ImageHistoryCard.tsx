import type { ImageHistoryItemType } from "../../types/imageDataTypes";
import ImageHistoryItem from "./ImageHistoryItem";

type props = {
    imageHistory: ImageHistoryItemType[]
    selectedImageId?: string | undefined
}

export default function ImageHistoryCard({imageHistory, selectedImageId}: props) {
    return (
        <div id="history-card" className="bg-white py-6 px-4 rounded-xl shadow-md h-full w-full">
            <div id="title-row" className="mb-12">
                <h1 className="text-lg font-semibold">Image history</h1>
            </div>

            <div id="history-list-container" className="flex flex-col pr-4 pb-7 max-h-[70%] gap-5 overflow-y-scroll">
                
                { imageHistory.length ?
                 imageHistory.map((item, index) => <ImageHistoryItem key={index} selectedImageId={selectedImageId} classification={item.classification_label || ''} imageId={item.tc_image_id} createdAt={item.created_at} />) 
                 : <p className="text-gray-500">No image history available.</p> }
            </div>
        </div>
    )
}