import ImageHistoryItem from "./ImageHistoryItem";

export default function ImageHistoryCard() {
    return (
        <div id="history-card" className="bg-white py-6 px-4 rounded-xl shadow-md h-full w-full">
            <div id="title-row" className="mb-12">
                <h1 className="text-lg font-semibold">Image history</h1>
            </div>

            <div id="history-list-container" className="flex flex-col pr-4 pb-7 max-h-[70%] gap-5 overflow-y-scroll">
                <ImageHistoryItem createdAt={'12121212'} imageId="1234"/>
                <ImageHistoryItem createdAt={'12121212'} imageId="1234"/>
                <ImageHistoryItem createdAt={'12121212'} imageId="1234"/>
                <ImageHistoryItem createdAt={'12121212'} imageId="1234"/>
                <ImageHistoryItem createdAt={'12121212'} imageId="1234"/>
                <ImageHistoryItem createdAt={'12121212'} imageId="1234"/>
            </div>
        </div>
    )
}