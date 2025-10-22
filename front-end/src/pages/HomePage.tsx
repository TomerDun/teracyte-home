import MetadataCard from "../components/HomeArea/MetadataCard";

export default function HomePage() {
    return (
        <div id="home-page-container" className="h-svh">
            <div id="header-container">
                Image Analytics Dashboard
            </div>
            <div id="main-container" className="flex gap-4 h-full">

                <div id="metadata-container" className="h-full w-[20%]">
                    <MetadataCard />
                </div>
                <div id="display-container" className="h-full w-[50%]">
                    <div className="bg-white border border-gray-200 rounded-md">Image Display</div>
                </div>
                <div id="charts-container" className="h-full w-[20%]">
                    <div className="bg-white border border-gray-200 rounded-md">Charts</div>
                </div>
            </div>
            #
        </div>
    )

}