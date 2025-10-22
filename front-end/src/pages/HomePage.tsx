import MetadataCard from "../components/HomeArea/MetadataCard";
import ImageDisplayCard from "../components/HomeArea/ImageDisplayCard";

export default function HomePage() {
    return (
        <div id="home-page-container" className="h-full">
            <div id="header-container">
                Image Analytics Dashboard
            </div>
            <div id="main-container" className="flex gap-4 h-full">

                <div id="metadata-container" className="h-full w-[20%]">
                    <MetadataCard />
                </div>
                <div id="display-container" className="h-full w-[50%]">
                    <ImageDisplayCard />
                </div>
                <div id="charts-container" className="h-full w-[20%]">
                    <div className="bg-white border border-gray-200 rounded-md">Charts</div>
                </div>
            </div>
        </div>
    )

}