// Icon URLs from Figma design
const imgIcon = "http://localhost:3845/assets/46ebdc5033665f50f6e8621141b693ec36e67e2a.svg";
const imgIcon1 = "http://localhost:3845/assets/e0eaba9f31658f5bda879da9bdcc1349ce427a8a.svg";
const imgIcon2 = "http://localhost:3845/assets/732414e927d4a4367d3c280d887482ffebd5530a.svg";
const imgIcon3 = "http://localhost:3845/assets/46b008d0976e22b01f33cb9b50138ee65ea4292f.svg";

interface MetadataCardProps {
  imageId?: string;
  intensityAverage?: number;
  focusScore?: number;
  classification?: string;
}

export default function MetadataCard({
  imageId = "img_20251022_080256",
  intensityAverage = 93.38,
  focusScore = 0.73,
  classification = "Anomaly"
}: MetadataCardProps = {}) {
  return (
    <div className="bg-white border border-gray-200 rounded-xl h-full w-full flex flex-col gap-12 p-6">
      {/* Header */}
      <div className="shrink-0">
        <h2 className="text-base text-gray-950">Image Metadata</h2>
      </div>

      {/* Metadata Items */}
      <div className="flex flex-col gap-4 shrink-0">
        {/* Image ID */}
        <div className="flex gap-3 items-start">
          <img src={imgIcon} alt="" className="size-5 shrink-0" />
          <div className="flex flex-col items-start">
            <p className="text-sm text-[#6a7282]">Image ID</p>
            <p className="text-base text-[#101828]">{imageId}</p>
          </div>
        </div>

        {/* Intensity Average */}
        <div className="flex gap-3 items-start">
          <img src={imgIcon1} alt="" className="size-5 shrink-0" />
          <div className="flex flex-col items-start">
            <p className="text-sm text-[#6a7282]">Intensity Average</p>
            <p className="text-base text-[#101828]">{intensityAverage}</p>
          </div>
        </div>

        {/* Focus Score */}
        <div className="flex gap-3 items-start">
          <img src={imgIcon2} alt="" className="size-5 shrink-0" />
          <div className="flex flex-col items-start">
            <p className="text-sm text-[#6a7282]">Focus Score</p>
            <p className="text-base text-[#101828]">{focusScore}</p>
          </div>
        </div>

        {/* Classification */}
        <div className="flex gap-3 items-start">
          <img src={imgIcon3} alt="" className="size-5 shrink-0" />
          <div className="flex flex-col items-start gap-1">
            <p className="text-sm text-[#6a7282]">Classification</p>
            <span className="inline-flex items-center justify-center px-2 py-0.5 bg-[#d4183d] text-white text-xs rounded-lg w-fit">
              {classification}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}